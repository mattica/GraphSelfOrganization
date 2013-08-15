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
		self.location_generator = BoundedUniform([(-4, 4), (-4, 4)])
		self.connectivity = (connectivity if connectivity < 1 
										 else 1.0/connectivity)
		self.agents = {}
		self.graph = networkx.Graph()
		self.field = fld.VectorField(self.agents, fld.MexicanHatGradient(3))
		for i in range(num_agents):
			#spawn location is randomized according to location_generator
			self.spawn_agent()
		self.max_iterations = max_iterations
		#plotting bounds properly belongs in environment object, refactor!
		#self.environment = None #for now (when? if simulation needs dynamic state outside of the agents, add examples)
		#add a field to environment
		#self.ruleset = #or some graphsynth object to encapusulate more details
		#ruleset return a single list of possible options, agents will have to choose from ALL

	def spawn_agent(self, location=None):
		if location is None:
			new_location = self.location_generator()
		else:
			new_location = location
		new_agent = agt.Agent(new_location, self.field.field_value)
		self.graph.add_node(new_agent.ID, agent=new_agent)
		for ID, agent in self.agents.iteritems():
			if random.random() < self.connectivity:
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
		positions = {ID: agent.location.tolist() 
					 for ID, agent in self.agents.iteritems()}
		#no rules yet, but add them as a skeleton
		options = [agt.Spread(), 
				   agt.NormalizeLinks(self.graph, self.agents, step=0.2)]
		#for i in self.converged(): #Using a generator!
		while not self.converged(k):
			#options = graphsynth.recognize(self.graph, rules) #the big board
			#options.build_agent_assignments()
			self.field.update()
			#roll a recorder object
			plt.hold(False)
			networkx.draw(self.graph, pos=positions) #only time positions gets used
			plt.xlim((-10,10))
			plt.ylim((-10,10))
			plt.draw()
			#plt.show()
			agent_queue = self.agents.items() #actually need the list here
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

