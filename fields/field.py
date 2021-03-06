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


class InverseSquare(object):
	""" 
	A functor that returns the inverse square of the distance between
	two points, scaled by a 'height' parameter. 
	"""
	def __init__(self, height=1.0):
		self.height = height #simple scaling factor

	def __call__(self, a, b):
		"""Inputs must be numpy arrays."""
		return self.height / (numpy.linalg.norm(b-a)**2)


class MexicanHat(object):
	"""
	Functor representing the Mexican Hat function. It uses the distance
	between two points as the independent variable. Width is the only
	parameter.
	"""
	def __init__(self, sigma=1.0):
		self.sigma = sigma #width of radial function
	
	def __call__(self, a, b):
		"""Inputs must be numpy arrays."""
		distance = numpy.linalg.norm(a - b)
		d_norm = (distance / self.sigma)**2
		return ( (1 - d_norm) * math.exp(-0.5*d_norm) *
				2/(math.sqrt(3.0*self.sigma) * math.pi**0.25) )


class MexicanHatGradient(MexicanHat):
	"""
	Functor representing the derivative of the Mexican Hat function.
	As with MexicanHat, the distance between two points is the independent 
	variable, and width is a parameter.
	"""
	def __call__(self, a, b):
		"""Inputs must be numpy arrays."""
		distance = numpy.linalg.norm(b - a) 
		d_norm = (distance / self.sigma)**2
		magnitude = ( (distance**3 - 3*distance*self.sigma**2) * 
				  		math.exp(-0.5*d_norm) * 2 / (math.sqrt(3.0) *
						math.pi**0.25 * self.sigma**4.5) )
		return magnitude 


class Field(object):
	"""
	Represents a scalar field computed from the sum of agent effects. 
	Each agent's component of the field is a local function, and the 
	components are simply added. 
	"""
	def __init__(self, agents, function):
		self.function = function #neighborhood function for each agent
		self.points = {}
		self.update(agents)

	def field_value(self, point, pointID=None):
		"""
		Returns the value of the field as generated by all agents. If
		a pointID is provided, that point will be ignored. This way
		an agent can sample a field without interfering with itself.
		"""
		result = 0
		for ID, location in self.points.iteritems():
			if ID is not pointID:
				result += self.function(point, location)
		return result

	def update(self, agents):
		""" Updates internal storage of point data """
		for ID, agent in agents.iteritems():
			self.points[ID] = agent.location


class VectorField(Field):
	"""
	Similar to the Field object, but each point in the field is a vector
	instead of a scalar. The radial function now gives the magnitude of 
	each agent's vector contribution. Each subvector points away from the
	agent it comes from. Any other pattern of vectors around each agent
	would require a new class.
	"""
	def field_value(self, point, pointID=None):
		""" 
		Like the method from Field it replaces, except it returns a vector.
		A particular agent's contribution can again be ignored by passing 
		a value to pointID. All agent contributions point away from the agent.
		"""
		result = numpy.zeros(len(point))
		for ID, location in self.points.iteritems():
			if ID is not pointID:
				#Vector difference should point away from each location.
				#difference depends on elementwise operations like numpy.array
				result += (location - point)*self.function(point, location)
		return result
	

