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
#import pygame
#import benpy
import networkx
import field as fld


class Agent(object):
	#actions = #define class for this? No, use graphsynth if possible.

	currentID = 0
	def __init__(self, location):
		if type(location) is tuple:
			self.location = location
		else:
		 	raise TypeError("Location should be a tuple of floats.")
		#using benpy for graphs here, but maybe graphsynth is a 
		#	better idea for now
		#self.truss_node = benpy.TrussNode(manager.truss_structure, identifier)
		self._id = self.currentID #truss_node.ID
		self.currentID += 1
		self.proximity = None

	@property
	def ID(self):
		return self._id

	def serialize(self):
		"""convert agent into a python dictionary for yaml"""
		#code this last
		pass

	def choose(self, options):
		#return favorite option
		pass

	def act(self, option=None):
		"""apply, needs to be written for any test system"""
		#should there be a "big board," or should agents recognize locally?
		D = self.proximity(self.location, self._id)
		self.location = tuple(x - 0.1*d for x, d in zip(self.location, D))


class BoundedUniform(object):
	def __init__(self, bounds):
		#upper and lower may be sequences
		#if they are, this generator provides a sequence of values
		self.bounds = bounds

	def __call__(self):
		return tuple(random.uniform(a,b) for a, b in self.bounds)

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


class AgentManager(object):
	def __init__(self, location_generator=BoundedUniform( ((0.0, 1.0),) ),
				 	   field=None, graph=None):
		self.location_generator = location_generator
		self.agents = {}
		#self.truss_structure = benpy.TrussGraph()
		self.field = (fld.VectorField(self.agents, fld.MexicanHatGradient())
						if field is None else field)
		self.graph = networkx.Graph() if graph is None else graph

	def __getitem__(self, ID):
		return self.agents[ID]

	def positions(self):
		return {ID: agent.location for ID, agent in self.agents.iteritems()}
	
	def spawn_agent(self, connectivity=0.2):
		new_location = self.location_generator()
		new_agent = Agent(new_location)
		new_agent.proximity = self.field.field_value
		self.graph.add_node(new_agent.ID, agent=new_agent)
		if connectivity < 1:
			for ID, agent in self.agents.iteritems():
				if random.random() < connectivity:
					d = fld.euclidean_distance(new_agent.location, 
											   agent.location)
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

	def recognize(self):
		""" Build and return the big board of options.
			The returned object should overload __getitem__."""
		pass

