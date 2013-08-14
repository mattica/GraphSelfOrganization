#!/usr/bin/python

import time
import random 
import numpy
import matplotlib.pyplot as plt
import networkx
import field as fld
import agent as agt

#set up folder architecture to leave space for user-defined agents, rules, etc.
#relative imports to reflect subfolders

class BoundedUniform(object):
	def __init__(self, bounds):
		#upper and lower may be sequences
		#if they are, this generator provides a sequence of values
		self.bounds = bounds

	def __call__(self):
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
		self.location_generator = location_generator
		self.connectivity = connectivity if connectivity < 1 
										 else 1.0/connectivity
		self.agents = {}
		self.field = (fld.VectorField(self.agents, fld.MexicanHatGradient(3))
						if field is None else field)
		for i in range(num_agents):
			#spawn location is randomized according to location_generator
			new_agent = self.spawn_agent()
		self.max_iterations = max_iterations
		#plotting bounds properly belongs in environment object, refactor!
		#self.environment = None #for now (when? if simulation needs dynamic state outside of the agents, add examples)
		#add a field to environment
		#self.ruleset = #or some graphsynth object to encapusulate more details
		#ruleset return a single list of possible options, agents will have to choose from ALL

	def spawn_agent(self):
		if location is None:
			new_location = self.location_generator()
		else:
			new_location = location
		new_agent = agt.Agent(new_location)
		new_agent.proximity = self.field.field_value
		self.graph.add_node(new_agent.ID, agent=new_agent)
		for ID, agent in self.agents.iteritems():
			if random.random() < connectivity:
				d = numpy.linalg.norm(new_agent.location - agent.location)
				self.graph.add_edge(new_agent.ID, ID)
		self.agents[new_agent.ID] = new_agent
		return new_agent

	def run(self):
		plt.ion()
		#print "running..."
		#fig = plt.figure()
		#ax = fig.add_subplot()
		start = time.clock()
		k = 0
		positions = self.manager.positions() #explain
		#no rules yet, but add them as a skeleton
		options = [agt.Spread(), 
				   agt.NormalizeLinks(self.manager, step=0.2)]
		#for i in self.converged(): #Using a generator!
		while not self.converged(k):
			#options = graphsynth.recognize(self.graph, rules) #the big board
			#options.build_agent_assignments()
			self.manager.field.update()
			#roll a recorder object
			plt.hold(False)
			networkx.draw(self.manager.graph, pos=positions) #only time positions gets used
			plt.xlim((-10,10))
			plt.ylim((-10,10))
			plt.draw()
			#plt.show()
			agent_queue = self.manager.agents.items()
			random.shuffle(agent_queue)
			#options = rules.recognize(self.manager.graph)
			for ID, agent in agent_queue:
				#agent.choose(options[agent.ID])
				#add options callback to remove already-used options
				choice = agent.choose(options)
				agent.act(choice)
				positions[ID] = agent.location.tolist() #updates
			#self.environment.step()
			k += 1
		print "elapsed:", time.clock() - start

	def converged(self, k):
		return k > self.max_iterations


class AgentManager(object):
	def __init__(self, location_generator=BoundedUniform( ((0.0, 1.0),) ),
				 	   field=None, graph=None):
		self.location_generator = location_generator
		self.agents = {}
		#self.truss_structure = benpy.TrussGraph()
		self.field = (fld.VectorField(self.agents, fld.MexicanHatGradient(3))
						if field is None else field)
		self.graph = networkx.Graph() if graph is None else graph

	def __getitem__(self, ID):
		return self.agents[ID]

	def positions(self):
		return {ID: agent.location.tolist() 
				for ID, agent in self.agents.iteritems()}
	
	def spawn_agent(self, connectivity=0.2, location=None):
		if location is None:
			new_location = self.location_generator()
		else:
			new_location = location
		new_agent = agt.Agent(new_location)
		new_agent.proximity = self.field.field_value
		self.graph.add_node(new_agent.ID, agent=new_agent)
		if connectivity < 1:
			for ID, agent in self.agents.iteritems():
				if random.random() < connectivity:
					d = numpy.linalg.norm(new_agent.location - agent.location)
					self.graph.add_edge(new_agent.ID, ID)
		else:
			raise ValueError("connectivity is a probability")
		self.agents[new_agent.ID] = new_agent
		return new_agent

	def step_all(self):
		options = self.recognize()
		pairs = list(self.agents.iter_items())
		random.shuffle(pairs)
		for ID, agent in pairs:
			agent.act(options[ID])


