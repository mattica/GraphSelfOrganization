"""Base class for grammar rule.

The host graph is stored as an internal (private) field to a rule
during recognition.  Since recognition just reads from it, this
simplifies the need to pass it along to every recognition function. 
"""
#    Copyright (C) 2013 by
#    Matt Campbell <mattica@gmail.com>
__author__ = """\n""".join(['Matt Campbell (mattica@gmail.com)'])
#    This file and the enclosing project (GraphSynth for NetworkX) is protected and
#    copyright under the MIT License.
#    Permission is hereby granted, free of charge, to any person obtain-
#    ing a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction, incl-
#    uding without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGE-
#    MENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
#    FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
#    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#    Please find further details and contact information on GraphSynth
#    at http://www.GraphSynth.com.
from copy import deepcopy
import networkx as nx
from networkx.exception import NetworkXError
import networkx.convert as convert

class GrammarRule(object):
	def __init__(self):
		# <summary>
		# the host graph is stored as an internal (private) field to a rule during recognition. 
		# Since recognition just reads from it, this simplifies the need to pass it along to every
		# recognition function. 
		# </summary>
		# <summary>
		#   any mathematical operations are fair game for the recognize and apply local variables.
		#   At the end of a graph recognition, we check all the recognize functions, if any yield a 
		#   positive number than the rule is infeasible. This is done in case1LocationFound.
		# </summary>
		# <summary>
		#   a list of MethodInfo's corresponding to the strings in applyFunctions
		# </summary>
		self._applyFuncs = List[MethodInfo]()
		# <summary>
		#   These are place holders when the user has clicked OrderedGlobalLabels. There may, in fact,
		#   be multiple locations for the globalLabels to be recognized. The are determined in the 
		#   OrderLabelsMatch function.
		# </summary>
		self._globalLabelStartLocs = List[int]()
		# <summary>
		#   this is where we store the subgraphs or locations of where the
		#   rule can be applied. It's global to a particular L but it is invoked
		#   only at the very bottom of the recursion tree - see the end of
		#   recognizeRecursion().
		# </summary>
		self._options = List[option]()
		# <summary>
		#   a list of MethodInfo's corresponding to the strings in recognizeFunctions
		# </summary>
		self._recognizeFuncs = List[MethodInfo]()

	# <summary>
	#   Gets or sets the name of the rule.
	# </summary>
	# <value>The name.</value>
	def get_name(self):

	def set_name(self, value):

	name = property(fget=get_name, fset=set_name)

	# <summary>
	#   Gets or sets a comment about the rule.
	# </summary>
	# <value>The comment.</value>
	def get_comment(self):

	def set_comment(self, value):

	comment = property(fget=get_comment, fset=set_comment)

	# <summary>
	#   Gets or sets a value indicating whether this <see cref = "grammarRule" /> is termination.
	# </summary>
	# <value><c>true</c> if termination; otherwise, <c>false</c>.</value>
	def get_termination(self):

	def set_termination(self, value):

	termination = property(fget=get_termination, fset=set_termination)

	# <summary>
	#   Gets or sets the embedding rules.
	# </summary>
	# <value>The embedding rules.</value>
	def get_embeddingRules(self):
		return self.__embeddingRules == (self.__embeddingRules = List[embeddingRule]())

	def set_embeddingRules(self, value):
		self.__embeddingRules = value

	embeddingRules = property(fget=get_embeddingRules, fset=set_embeddingRules)

	# after double pushout runs its course, we'd like to account for dangling arcs that were victims
	# * of the G - (L - R) pushout. these rules are defined here following the edNCE approach (edge-directed
	# * Neighborhood Controlled Embedding) and discussed in more detail below.
	# <summary>
	#   Gets or sets the additional recognize functions names.
	# </summary>
	# <value>The recognize functions.</value>
	def get_recognizeFunctions(self):
		return self.__recognizeFunctions == (self.__recognizeFunctions = List[str]())

	def set_recognizeFunctions(self, value):
		self.__recognizeFunctions = value

	recognizeFunctions = property(fget=get_recognizeFunctions, fset=set_recognizeFunctions)

	# <summary>
	#   Gets or sets the apply functions.
	# </summary>
	# <value>The apply functions.</value>
	def get_applyFunctions(self):
		return self.__applyFunctions == (self.__applyFunctions = List[str]())

	def set_applyFunctions(self, value):
		self.__applyFunctions = value

	applyFunctions = property(fget=get_applyFunctions, fset=set_applyFunctions)

	# <summary>
	#   Gets or sets  the left-hand-side of the rule. It is a graph that is to be 
	#   recognized in the host graph.
	# </summary>
	# <value>The L.</value>
	def get_L(self):

	def set_L(self, value):

	L = property(fget=get_L, fset=set_L)

	# .
	# <summary>
	#   Gets or sets the right-hand-side of the rule. It is a graph that is to be 
	#   inserted (glued) into the host graph.
	# </summary>
	# <value>The R.</value>
	def get_R(self):

	def set_R(self, value):

	R = property(fget=get_R, fset=set_R)

	# these are special booleans used by recognize. In many cases, the L will be a subset of the
	# * host in all respects (a proper subset - a subgraph which is anything but equal). However,
	# * there may be times when the user wants to restrict the number of recognized locations, by
	# * looking for an EQUAL conditions as opposed to simply a SUBSET. The following booleans
	# * capture the possible ways in which the subgraph may/may not be a subset (boolean set to false)
	# * or is equal (in this respective quality) to the host (boolean set to true).
	# <summary>
	#   Gets or sets a value indicating whether this <see cref = "grammarRule" /> is spanning.
	# </summary>
	# <value><c>true</c> if spanning; otherwise, <c>false</c>.</value>
	def get_spanning(self):

	def set_spanning(self, value):

	spanning = property(fget=get_spanning, fset=set_spanning)

	# if true then all nodes in L must be in host and vice-verse - NOT a proper subset
	# /* if false then proper subset.
	# <summary>
	#   Gets or sets a value indicating whether this <see cref = "grammarRule" /> is induced.
	# </summary>
	# <value><c>true</c> if induced; otherwise, <c>false</c>.</value>
	def get_induced(self):

	def set_induced(self, value):

	induced = property(fget=get_induced, fset=set_induced)

	# if true then all arcs between the nodes in L must be in host and no more
	# * - again not a proper SUBSET
	# * if false then proper subset.
	# * this following function is the only to use induced and is only called early
	# * in the Location Found case, and only then when induced is true. As its name implies it
	# * simply checks to see if there are any arcs in the host between the nodes recognized.
	# <summary>
	#   Gets or sets the negating labels - labels that must NOT exist in the host.
	# </summary>
	# <value>The negating labels.</value>
	def get_negateLabels(self):
		return self.__negateLabels == (self.__negateLabels = List[str]())

	def set_negateLabels(self, value):
		self.__negateLabels = value

	negateLabels = property(fget=get_negateLabels, fset=set_negateLabels)

	# <summary>
	#   Gets or sets a value indicating whether the host must contains only the
	#   global labels of the rule. Said another way, the rule must contain all global labels
	#   in the host to be a valid match. If false, then a subset of global labels is sufficient.
	# </summary>
	# <value>
	#   <c>true</c> if [contains all global labels]; otherwise, <c>false</c>.
	# </value>
	def get_containsAllGlobalLabels(self):

	def set_containsAllGlobalLabels(self, value):

	containsAllGlobalLabels = property(fget=get_containsAllGlobalLabels, fset=set_containsAllGlobalLabels)

	# <summary>
	#   Gets or sets a value indicating whether the host must contain the
	#   global labels in the presented order. This is mainly to allow for the creation of traditional
	#   string grammars.
	# </summary>
	# <value><c>true</c> if [ordered global labels]; otherwise, <c>false</c>.</value>
	def get_OrderedGlobalLabels(self):

	def set_OrderedGlobalLabels(self, value):

	OrderedGlobalLabels = property(fget=get_OrderedGlobalLabels, fset=set_OrderedGlobalLabels)

	def makeUniqueNodeName(self, stub):
		""" <summary>
		   Makes a unique name of a node.
		 </summary>
		 <returns></returns>
		"""
		stub = stub.TrimEnd('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		i = 0
		while (self.L.nodes.Exists()) or (self.R.nodes.Exists()):
			i += 1
		return stub + i

	def makeUniqueArcName(self, stub):
		""" <summary>
		   Makes a unique name of an arc.
		 </summary>
		 <returns></returns>
		"""
		stub = stub.TrimEnd('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		i = 0
		while (self.L.arcs.Exists()) or (self.R.arcs.Exists()):
			i += 1
		return stub + i

	def makeUniqueHyperarcName(self, stub):
		""" <summary>
		   Makes a unique name of a hyperarc.
		 </summary>
		 <returns></returns>
		"""
		stub = stub.TrimEnd('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		i = 0
		while (self.L.hyperarcs.Exists()) or (self.R.hyperarcs.Exists()):
			i += 1
		return stub + i

	def get_LDegreeSequence(self):
		return List[int]()

	LDegreeSequence = property(fget=get_LDegreeSequence)

	def get_LHyperArcDegreeSequence(self):
		return List[int]()

	LHyperArcDegreeSequence = property(fget=get_LHyperArcDegreeSequence)
