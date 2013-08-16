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

import numpy

class Option(object):
	def __init__(self, IDs, apply_function=None):
		self._IDs = set(IDs)
		self.apply = apply_function

	def __contains__(self, ID):
		return ID in self._IDs
	

class Spread(object):
	def __init__(self, field, step=0.3):
		self.step = step
		self.field_callback = field.field_value

	def _apply(self, agent):	
		agent.location += self.step * self.field_callback(agent.location, 
														  agent.ID)

	def recognize(self, graph):
		return [Option([ID], self._apply) for ID in graph.nodes_iter()]


class NormalizeLinks(object):
	def __init__(self, graph, step=0.3):
		self.step = step
		self.graph = graph

	def _apply(self, agent):
		num_links = 0
		position_sum = numpy.zeros(2)
		for a, b in self.graph.edges_iter(agent.ID):
			other = (self.graph.node[b]['agent'] if a == agent.ID 
					 else self.graph.node[a]['agent'])
			position_sum += other.location
			num_links += 1
		target = position_sum / num_links
		agent.location += self.step*(target - agent.location)

	def recognize(self, graph):
		return [Option([ID], self._apply) for ID in graph.nodes_iter()]
	
