#!/usr/bin/python

import time
import random 
import numpy
import matplotlib.pyplot as plt
import networkx
import fields.field as fld
import agents.agent as agt
import rulesets.rules as rules

class BoundedUniform(object):
	"""
	A probability distribution uniform over the given bounds. 
	"""
	def __init__(self, bounds):
		"""
		Takes a numpy array with two columns and n rows.
		n is the number of dimensions for the distribution.
		Each row is [lower_bound, upper_bound].
		"""
		self.bounds = bounds

	def __call__(self):
		""" Return a single sample from the pdf. """
		result = numpy.random.random(self.bounds.shape[0]) #rand [0,1)
		result *= self.bounds[:,1] - self.bounds[:,0] #scale
		return result + self.bounds[:,0] #shift

	@property
	def bounds(self):
		return self._bounds
	
	@bounds.setter
	def bounds(self, new_bounds):
		""" Basic format checking. """
		try:
			assert not any(new_bounds[:,0] >= new_bounds[:,1])
			assert new_bounds.shape[-1] == 2
		except:
			raise ValueError("Bounds should be a numpy array where the "
					+ "innermost dimension is length-2, and pairs over "
					+ "the outer dimensions follow a < b for [a, b].")
		self._bounds = new_bounds


class Environment(object):
	""" 
	This example environment object puts up walls and enforces them
	with a penalty function. The penalty function is meant to be applied
	without giving the agent a choice (it's not a rule!).
	"""
	def __init__(self, bounds, function=None):
		""" 
		Initialize with a set of cartesian bounds (same format as 
		BoundedUniform) and a penalty function. The penalty function
		should be compatible with element-wise operations.
		"""
		self.bounds = numpy.array(bounds)
		self.function = function or (lambda a, b: 0.2/((b-a)**2))

	def field_value(self, point):
		""" Push away from the walls according to an inverse square law. """
		b = numpy.array(self.bounds)
		return self.function(b[:,0], point) + self.function(point, b[:,1])

	def update(self):
		#no internal states to track, so there's nothing to do here for now
		pass


class Simulation(object):
	"""
	The simulation object encapsulates all parameters of a simulation
	for easy offline manipulation. This one is a demonstration of different
	elements of CSO simulation. It does not solve any engineering problem.
	It should draw a graph animation with the nodes bouncing around randomly.
	"""
	def __init__(self, num_agents=10, max_iterations=10, connectivity=0.2):
		""" Sets up a simulation. """
		self.agents = {} #empty dict to be populated later
		self.max_iterations = max_iterations
		
		#The environment encapuslates any behavior that does not concern 
		#the agents directly. This one adds walls with a penalty field.
		#Agents are involuntarily push away from the walls.
		self.environment = Environment([(-6, 6), (-6, 6)]) 

		#Connectivity is the probability that any given link exists
		#between agents. The next line ensures that the probability is not 
		#greater than one or less than zero.
		self.connectivity = abs(connectivity if abs(connectivity) < 1 
											 else 1.0/connectivity)

		#The default networkx graph is simple and undirected, empty by default. 
		#Agent IDs serve as the nodes, and each agent object is associated with
		#its node in the graph. See the networkx docs for details.
		self.graph = networkx.Graph()

		
		#location_generator is a functor that samples from a probability 
		#distribution; it's used to initialize agent locations.
		location_bounds = (self.environment.bounds + 
						   numpy.array([[2, -2], [2, -2]])) #margins
		self.location_generator = BoundedUniform(location_bounds) 

		#A field is a function with a unique value for each position. This 
		#field depends on the positions of agents.
		self.field = fld.VectorField(self.agents, fld.MexicanHatGradient(3))

		#This field depends on the environment.
		#MAKE A NEW FIELD HERE
		
		#Rule objects should have a recognize method
		#that returns a list of options. Agents will
		#choose from ALL options.
		self.ruleset = [rules.Spread(self.field, step=0.3), 
				   		rules.NormalizeLinks(self.graph, step=0.2)]

		#Populate the dict of agents...
		#agents = {spawn_agent() for i in range(num_agents)} #using a set?
		for i in range(num_agents):
			self.spawn_agent()

	def spawn_agent(self, location=None):
		#Generate a location if none was given, and use it to instantiate 
		#the new agent.
		new_location = location or self.location_generator()
		new_agent = agt.Agent(new_location)

		#Add the new agent to the graph.
		self.graph.add_node(new_agent.ID, agent=new_agent)
		for ID, agent in self.agents.iteritems():
			#Create an link with probability = connectivity.
			if random.random() < self.connectivity:
				self.graph.add_edge(new_agent.ID, ID)

		#Add the new agent to the address dict. Doing this after adding it
		#to the graph means that no self-links are created.
		self.agents[new_agent.ID] = new_agent
		return new_agent

	def run(self):
		#Turn on interactive plotting (automatically update plots).
		plt.ion() 

		#Record the current time for comparison after the simulation.
		start = time.clock() #for timing the algorithm

		#Create a dict of agent positions. Need this for networkx plotting.
		positions = {ID: agent.location.tolist() 
					 for ID, agent in self.agents.iteritems()}

		#main simulation loop
		iteration = 0
		while not self.converged(iteration):
			#Plot the state of the simulation (agents + environment).
			plt.hold(False)
			networkx.draw(self.graph, pos=positions) #sole use of 'positions'
			plt.xlim(self.environment.bounds[0,:]) 
			plt.ylim(self.environment.bounds[1,:])
			plt.draw()

			#Update [proximity] field.
			self.field.update(self.agents)

			#Generate list (one element/rule) of lists of options.
			options = []
			for rule in self.ruleset:
				options.extend(rule.recognize(self.graph))

			#plt.show() #needed only if matplotlib interactive mode is off
			agent_queue = self.agents.items() #actually need the list here
			random.shuffle(agent_queue)
			for ID, agent in agent_queue:
				agent.location += self.environment.field_value(agent.location)
				choice = agent.choose(options)
				choice.apply(agent)
				positions[ID] = agent.location.tolist() #updates plot positions
			self.environment.update() #need if environment has state
			iteration += 1
		print "elapsed:", time.clock() - start

	def converged(self, current_iteration):
		return current_iteration > self.max_iterations


def run():
	""" Show an example simulation. """
	sim = Simulation(num_agents=20, max_iterations=40, connectivity=.3)
	sim.run()

