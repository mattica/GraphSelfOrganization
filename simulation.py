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
		Takes a sequence of length-2 tuples.
		len(bounds) is the number of dimensions for the distribution.
		Each length-2 tuple is (lower_bound, upper_bound)
		"""
		self.bounds = bounds

	def __call__(self):
		""" Return a single sample from the pdf. """
		result = numpy.zeros(len(self.bounds))
		for i, interval in enumerate(self.bounds):
			result[i] = random.uniform(*interval) 
		return result

	@property
	def bounds(self):
		return self._bounds
	
	@bounds.setter
	def bounds(self, new_bounds):
		try:
			for a, b in new_bounds:
				assert a < b
		except:
			raise ValueError("Bounds should be a sequence of pairs (a, b)," 
								+ "where a < b.")
		self._bounds = new_bounds


class Simulation(object):
	def __init__(self, num_agents=10, max_iterations=10, connectivity=0.2):
		""" Sets up a simulation. """
		self.agents = {} #empty dict to be populated later
		self.max_iterations = max_iterations

		#Connectivity is the probability that any given link exists
		#between agents. The next line ensures that the probability is not 
		#greater than one or less than zero.
		self.connectivity = abs(connectivity if abs(connectivity) < 1 
										 else 1.0/connectivity)

		#The default networkx graph is simple and undirected, empty by default. 
		self.graph = networkx.Graph()

		#The environment encapuslates any behavior that does not concern 
		#the agents directly.
		self.environment = None #add walls and a penalty field (with bounds)

		#location_generator is a functor that samples from a probability 
		#distribution; it's used to initialize agent locations.
		self.location_generator = BoundedUniform([(-4, 4), (-4, 4)]) 

		#A field is a function with a unique value for each position. This 
		#field depends on the positions of agents.
		self.field = fld.VectorField(self.agents, fld.MexicanHatGradient(3))

		#This field depends on the environment.
		#MAKE A NEW FIELD HERE
		
		#Rule objects should have a recognize method
		#that returns a list of options. Agents will
		#choose from ALL options.
		self.ruleset = [rules.Spread(step=0.3), 
				   		rules.NormalizeLinks(self.graph, step=0.2)]

		#Populate the dict of agents...
		#agents = {spawn_agent() for i in range(num_agents)} #using a set?
		for i in range(num_agents):
			self.spawn_agent()

	def spawn_agent(self, location=None):
		new_location = location or self.location_generator()
		new_agent = agt.Agent(new_location, self.field.field_value)
		self.graph.add_node(new_agent.ID, agent=new_agent)
		for ID, agent in self.agents.iteritems():
			#Create an link with probability = connectivity.
			if random.random() < self.connectivity:
				#d = numpy.linalg.norm(new_agent.location - agent.location)
				self.graph.add_edge(new_agent.ID, ID)
		self.agents[new_agent.ID] = new_agent
		return new_agent

	def run(self):
		plt.ion()
		start = time.clock() #for timing the algorithm
		iteration = 0
		positions = {ID: agent.location.tolist() 
					 for ID, agent in self.agents.iteritems()}
		#no rules yet, but add them as a skeleton

		#main simulation loop
		while not self.converged(iteration):
			#plot state
			plt.hold(False)
			networkx.draw(self.graph, pos=positions) #sole use of positions
			plt.xlim((-10,10)) #these should come from environment
			plt.ylim((-10,10))
			plt.draw()

			#update [proximity] field
			self.field.update()

			#generate list (one element/rule) of lists of options
			options = []
			for rule in self.ruleset:
				options.extend(rule.recognize(self.graph))

			#plt.show() #needed only if matplotlib interactive mode is off
			agent_queue = self.agents.items() #actually need the list here
			random.shuffle(agent_queue)
			for ID, agent in agent_queue:
				choice = agent.choose(options)
				choice.apply(agent)
				positions[ID] = agent.location.tolist() #updates plot positions
			#self.environment.step() #need if environment has state
			iteration += 1
		print "elapsed:", time.clock() - start

	def converged(self, current_iteration):
		return current_iteration > self.max_iterations

