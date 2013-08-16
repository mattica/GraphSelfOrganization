import numpy

class Option(object):
	def __init__(self, IDs, apply_function=None):
		self._IDs = set(IDs)
		self.apply = apply_function

	def __contains__(self, ID):
		return ID in self._IDs
	

class Spread(object):
	def __init__(self, step=0.3):
		self.step = step

	def _apply(self, agent):	
		agent.location += self.step * agent.field_callback(agent.location, 
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
	
