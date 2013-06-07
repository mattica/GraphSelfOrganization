#!/usr/bin/python

import random

class Simulation(object):
	def __init__(self, iterations=100):
		self.agents = {i: Agent(i, (0.0,0.0)) for i in range(8)} 
		self.field = MexicanHatField(self.agents)
		self.graph = networkx.Graph()
		self.K = iterations
		self.environment = None #for now
		self.rules = #or some graphsynth object to encapusulate more details
		#need some way for agents to link back to self.field
		for agent in self.agents.itervalues():
			agent.proximity = self.field.field_value
			self.graph.add(agent)
		#loop to initialize topology of graph

	def run(self):
		start = time.clock()
		k = 0
		while not self.converged(k):
			options = graphsynth.recognize(self.graph, rules) #the big board
			#options.build_agent_assignments()
			for agent in random.shuffle(self.agents.itervalues()):
				agent.choose(options[agent.ID])
				#add options callback to remove already-used options
				agent.apply_rule()
			self.environment.step()
			k += 1
		print "elapsed:", time.clock() - start

	def converged(self, k):
		return k > K

sim = Simulation()
sim.run()

