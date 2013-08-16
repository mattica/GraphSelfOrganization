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
		#Determine which options apply to this agent.
		applicable = [option for option in options if self.ID in option]
		#Return favorite option.
		return random.choice(applicable) #uniform random for now


