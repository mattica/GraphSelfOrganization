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

import math
import numpy


def euclidean_distance(a, b):
	return math.sqrt( sum(x-y for x, y in zip(a, b)) ) 


class InverseSquare(object):
	def __init__(self, height=1.0):
		self.height = height

	def __call__(self, a, b):
		return self.height / (euclidean_distance(a, b)**2)


class MexicanHat(object):
	""" mexican hat functor """
	def __init__(self, sigma=1.0):
		self.sigma = sigma
	
	def __call__(self, a, b):
		distance = euclidean_distance(a, b)
		d_norm = (distance / self.sigma)**2
		return ( (1 - d_norm) * math.exp(-0.5*d_norm) *
				2/(math.sqrt(3.0*self.sigma) * math.pi**0.25) )


class Field(object):
	def __init__(self, agents, proximity=InverseSquare()):
		self.agents = agents
		self.proximity = proximity
		self.update()

	def field_value(self, point, pointID=None):
		""" returns total field intensity following an inverse square
			law in distance """
		result = 0
		for ID, location in self.points.iteritems():
			if ID is not pointID:
				result += self.proximity(point, location)
		return result

	def update(self):
		""" updates internal storage of point data """
		for ID, agent in self.agents.iter_items():
			self.points[key] = agent.location 


class VectorField(Field):
	def field_value(self, point, pointID=None):
		""" Returns the vector (numpy array) corresponding to the
			given point. If a pointID is provided, that agent is
			ignored. Expects agent locations to also be numpy arrays."""
		p = numpy.array(point)
		result = numpy.zeros(len(p))
		for ID, location in self.points.iteritems():
			#Compute the euclidian distance
			magnitude = self.proximity(p, location)
			if ID is not pointID:
				#Vector difference should point away from each location.
				#difference depends on elementwise operations like numpy.array
				result += magnitude * (p - location) 
		return result
	

