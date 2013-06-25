#!/usr/bin/python

import time
import random 
import networkx
import field as fld
import agent as agt

class Simulation(object):
	def __init__(self, num_agents=8, iterations=100, num_links=20):
		self.graph = networkx.Graph()
		self.agents = {}
		for i in range(num_agents):
			#initial agent location randomized
			new_agent = agt.Agent((random.uniform(-4,4), random.uniform(-4,4)))
			self.agents[i] = new_agent
			self.graph.add_node(new_agent.ID, agent=new_agent)
		self.field = fld.VectorField(self.agents, fld.MexicanHatGradient())
		self.K = iterations
		#self.environment = None #for now
		#self.rules = #or some graphsynth object to encapusulate more details
		#link agents back to self.field
		for agent in self.agents.itervalues():
			agent.proximity = self.field.field_value
		#loop to initialize topology of graph
		IDlist = self.agents.keys()
		for i in range(num_links):
			a = random.choice(IDlist)
			b = random.choice(IDlist)
			d = fld.euclidean_distance(self.agents[a].location, 
									   self.agents[b].location)
			self.graph.add_edge(a, b, length=d)

	def run(self):
		start = time.clock()
		k = 0
		positions = {ID: agent.location 
					 for ID, agent in self.agents.iteritems()}
		while not self.converged(k):
			#options = graphsynth.recognize(self.graph, rules) #the big board
			#options.build_agent_assignments()
			networkx.draw(self.graph, pos=positions)
			for ID, agent in random.shuffle(self.agents.items()):
				#agent.choose(options[agent.ID])
				#add options callback to remove already-used options
				agent.act()
				positions[ID] = agent.location
			#self.environment.step()
			k += 1
		print("elapsed:", time.clock() - start)

	def converged(self, k):
		return k > self.K


