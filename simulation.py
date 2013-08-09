#!/usr/bin/python

import time
import random 
import matplotlib.pyplot as plt
import networkx
import field as fld
import agent as agt

#set up folder architecture to leave space for user-defined agents, rules, etc.
#relative imports to reflect subfolders

class Simulation(object):
	#use max_iterations, Kmax, Kcurrent
	def __init__(self, num_agents=10, iterations=10, connectivity=0.2):
		#make an argument for converged function
		self.manager = agt.AgentManager(location_generator=
										agt.BoundedUniform( ((-4,4),(-4, 4)) ))
		for i in range(num_agents):
			#initial agent location randomized
			new_agent = self.manager.spawn_agent(connectivity)
		self.K = iterations
		#plotting bounds properly belongs in environment object, refactor!
		#self.environment = None #for now (when? if simulation needs dynamic state outside of the agents, add examples)
		#add a field to environment
		#self.ruleset = #or some graphsynth object to encapusulate more details
		#ruleset return a single list of possible options, agents will have to choose from ALL

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
		return k > self.K


