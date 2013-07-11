#!/usr/bin/python

import time
import random 
import matplotlib.pyplot as plt
import networkx
import field as fld
import agent as agt

class Simulation(object):
	def __init__(self, num_agents=10, iterations=10, connectivity=0.2):
		self.manager = agt.AgentManager(location_generator=
										agt.BoundedUniform( ((-4,4),(-4, 4)) ))
		for i in range(num_agents):
			#initial agent location randomized
			new_agent = self.manager.spawn_agent(connectivity)
		self.K = iterations
		#self.environment = None #for now
		#self.rules = #or some graphsynth object to encapusulate more details

	def run(self):
		#plt.ion()
		#fig = plt.figure()
		#ax = fig.add_subplot()
		start = time.clock()
		k = 0
		positions = self.manager.positions()
		while not self.converged(k):
			#options = graphsynth.recognize(self.graph, rules) #the big board
			#options.build_agent_assignments()
			self.manager.field.update()
			plt.hold(False)
			networkx.draw(self.manager.graph, pos=positions) 
			plt.xlim((-10,10))
			plt.ylim((-10,10))
			plt.draw()
			#plt.show()
			agent_queue = self.manager.agents.items()
			random.shuffle(agent_queue)
			for ID, agent in agent_queue:
				#agent.choose(options[agent.ID])
				#add options callback to remove already-used options
				agent.act()
				positions[ID] = agent.location
			#self.environment.step()
			k += 1
		print "elapsed:", time.clock() - start

	def converged(self, k):
		return k > self.K


