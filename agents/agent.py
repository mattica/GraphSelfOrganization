#GraphSelfOrganization
#Copyright (C) 2013  Matthew Ira Campbell, John Wendell Hall
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#The author may be reached at jackhall@utexas.edu.

#import yaml
#import multiprocessing #will be used to split threads, avoiding the python GIL
import random 
import numpy
#import pygame
#import benpy
import networkx
import field as fld

#make sure methods have verbs, attributes have nouns!

class Spread(object):
	def __init__(self, step=0.3):
		self.step = step

	def __call__(self, agent):
		agent.location += self.step * agent.field_callback(agent.location, 
														   agent.ID)


class NormalizeLinks(object):
	def __init__(self, graph, agents, step=0.3):
		self.graph = graph
		self.agents = agents
		self.step = step

	def __call__(self, agent):
		num_links = 0
		position_sum = numpy.zeros(2)
		for a, b in self.graph.edges_iter(agent.ID):
			other = self.agents[b] if a == agent.ID else self.agents[a]
			position_sum += other.location
			num_links += 1
		target = position_sum / num_links
		agent.location += self.step*(target - agent.location)
				

class Agent(object):
	_currentID = 0
	def __init__(self, location, field_callback=None):
		if type(location) is numpy.ndarray:
			self.location = location
		else:
			self.location = numpy.array(location)
		self._id = self._currentID 
		Agent._currentID += 1
		self.field_callback = field_callback

	@property
	def ID(self):
		return self._id

	def choose(self, options):
		#return favorite option (what is allowed for this part of the concept?)
		return random.choice(options) #uniform random for now
		#return options[1]

	#remove, just call option
	def act(self, option):
		"""apply, needs to be written for any test system"""
		#should there be a "big board," or should agents recognize locally?
		option(self)


