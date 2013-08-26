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
	"""
	An option is an instance of a rule applied once in a specified place. 

	That specified place can be specified in any number of ways. This object
	associates itself with a set of agents by their ID numbers. It is invoked
	by calling 'option_instance.apply(agent_instanec)', which mutates the
	agent(s) in question.
	"""
	def __init__(self, IDs, apply_function=None):
		""" Takes an iterable of agent IDs and an application callback. That
			apply function should be provided by the rule. """
		self._IDs = set(IDs)
		self.apply = apply_function

	def __contains__(self, ID):
		""" Lets the user type things like 'agent.ID in option_instance' to
			determine whether the option instance is associated with the agent
			in question. """
		return ID in self._IDs
	

class Spread(object):
	"""
	A rule that moves an agent along the vector field given, for a distance
	given by step*[vector magnitude].
	"""
	def __init__(self, field, step=0.3):
		""" Takes a field object and a step size. """
		self.step = step
		self.field_callback = field.field_value

	def _apply(self, agent):
		""" 
		Callback function to apply the rule to a given agent. Assigned
		to options when they are created and called when the options are
		assigned. This one moves the agent along the vector given at its
		location in the field. In simulation.py currently, the vector
		field is the gradient of Mexican Hat functions summed over all agents.
		"""
		agent.location += self.step * self.field_callback(agent.location, 
														  agent.ID)

	def recognize(self, graph):
		""" 
		Recognize functions should return a complete list of valid options
		for the rule's application. This one could potentially apply to 
		any agent, so it returns an option for each agent. 
		"""
		#assigns _apply function - does not call it!
		return [Option([ID], self._apply) for ID in graph.nodes_iter()]


class NormalizeLinks(object):
	"""
	A rule that moves an agent toward the centroid of its link partners. It
	computes the average position of the agents connected to it via the graph,
	and moves itself [step] of the way to that position. 
	"""
	def __init__(self, graph, step=0.3):
		self.step = step
		self.graph = graph

	def _apply(self, agent):
		""" 
		Callback function to apply the rule to a given agent. Assigned
		to options when they are created and called when the options are
		assigned. This one, as described above, moves the agent toward
		the centroid of link partners. 
		"""
		num_links = 0
		#sum the positions of partner agents
		position_sum = numpy.zeros(2)
		for a, b in self.graph.edges_iter(agent.ID):
			other = (self.graph.node[b]['agent'] if a == agent.ID 
					 else self.graph.node[a]['agent'])
			position_sum += other.location
			num_links += 1
		#divide by the number of partner agents
		target = position_sum / num_links
		#move the agent toward this average position
		agent.location += self.step*(target - agent.location)

	def recognize(self, graph):
		""" 
		As with Spread.recognize, all agents are automatically recognized
		by this rule. That will not be true for all rules.
		"""
		return [Option([ID], self._apply) for ID in graph.nodes_iter()]
	
