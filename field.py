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
	

