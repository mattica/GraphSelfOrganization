import math
import numpy

class ProximityField(object):
	def __init__(self, agents, width=1.0, height=1.0):
		self.agents = agents #dict mapping IDs to agents
		#Build self.points
		self.update()
		self.width = width
		self.height = height

	def field_value(self, point, pointID=None):
		""" Returns the vector (numpy array) corresponding to the
			given point. If a pointID is provided, that agent is
			ignored. """
		p = numpy.array(point)
		result = numpy.zeros(len(p))
		for ID, location in self.points.iter_items():
			#Compute the euclidian distance
			distance = sqrt( sum([x-y for x, y in zip(p, location)]) ) 
			if distance < 5.0*self.width and ID is not pointID:
				magnitude = self.height * self._proximity_fcn(distance)
				#Vector difference should point away from each location.
				result += magnitude * (point - location)
		return result

	def _proximity_fcn(self, d):
		"""returns a simple distance scaled by self.width"""
		return d / self.width

	def update(self):
		for ID, agent in self.agents.iter_items():
			self.points[key] = agent.location


class MexicanHatField(ProximityField):
	def _proximity_fcn(self, d):
		"""The mexican hat function with sigma = self._width"""
		d_norm = (d / self.width)**2
		return ( (1 - d_norm) * math.exp(-0.5*d_norm) *
				2/(math.sqrt(3.0*self.width) * math.pi**0.25) )

