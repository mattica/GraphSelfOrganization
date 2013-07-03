# ************************************************************************
# *     This ruleHyperarc file & class is part of the GraphSynth.BaseClasses
# *     Project which is the foundation of the GraphSynth Application.
# *     GraphSynth.BaseClasses is protected and copyright under the MIT
# *     License.
# *     Copyright (c) 2011 Matthew Ira Campbell, PhD.
# *
# *     Permission is hereby granted, free of charge, to any person obtain-
# *     ing a copy of this software and associated documentation files
# *     (the "Software"), to deal in the Software without restriction, incl-
# *     uding without limitation the rights to use, copy, modify, merge,
# *     publish, distribute, sublicense, and/or sell copies of the Software,
# *     and to permit persons to whom the Software is furnished to do so,
# *     subject to the following conditions:
# *
# *     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# *     EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# *     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGE-
# *     MENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# *     FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# *     CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# *     WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# *
# *     Please find further details and contact information on GraphSynth
# *     at http://www.GraphSynth.com.
# ************************************************************************
from System import *
from System.Collections.Generic import *
from System.Linq import *
# here we define additional qualities used only by hyperarcs in the grammar rules.
class ruleHyperarc(hyperarc):
	""" <summary>
	   The ruleHyperArc class is an inherited class from hyperarc which includes additional details
	   necessary to correctly perform recognition. This mostly hinges on the "subset or equal"
	   Booleans.
	 </summary>
	"""
	def __init__(self, ha):
		""" <summary>
		   Initializes a new instance of the <see cref = "ruleHyperarc" /> class.
		 </summary>
		 <param name = "newName">The new name.</param>
		"""
		# <summary>
		#   Initializes a new instance of the <see cref = "ruleHyperarc" /> class.
		# </summary>
		# <summary>
		# Initializes a new instance of the <see cref="ruleHyperarc"/> class.
		# Converts a hyperarc to a ruleHyperArc and returns it with default Booleans.
		# The original hyperarc is unaffected.
		# </summary>
		# <param name="ha">The hyperarc, ha.</param>
		# <returns></returns>
		# <summary>
		#   Returns a copy of this instance.
		# </summary>
		# <returns>the copy of the arc.</returns>
		# <summary>
		#   Copies this instance into the (already intialized) copyOfHyperArc.
		# </summary>
		# <param name = "copyOfHyperArc">The copy of node.</param> # <summary>
		#   Gets the negating labels. The labels that must not exist for correct recognition.
		# </summary>
		# <value>The negate labels.</value>
		# <summary>
		# Gets or sets a value indicating whether the element should not exist in the
		# host graph.
		# </summary>
		# <value><c>true</c> if [not exist]; otherwise, <c>false</c>.</value>
		# <summary>
		#   Gets or sets a value indicating whether arc must contain all the local labels of the matching element.
		# </summary>
		# <value>
		#   <c>true</c> if [contains all local labels]; otherwise, <c>false</c>.
		# </value>
		# if true then all the localLabels in the rule element much match with those in the host
		# * element, if false then the rule element labels only need to be a subset on host elt. localLabels.
		# <summary>
		#   Gets or sets the type (as a string) for the matching graph element.
		# </summary>
		# <value>The string describing the type of graph element.</value>
		# if the user typed a Type but we can't find it, it is likely that
		# * * it is being compiled within GraphSynth, so prepend with various
		# * * namespaces.
		#    throw new Exception("The Type: "+value+ " is not known.");
		self.__targetType = ""
		DisplayShape = ha.DisplayShape
		TargetType = ha.GetType().ToString()
		localLabels.AddRange(ha.localLabels)
		localVariables.AddRange(ha.localVariables)
		nodes.AddRange(ha.nodes)

	def __init__(self, ha):
		self.__targetType = ""
		DisplayShape = ha.DisplayShape
		TargetType = ha.GetType().ToString()
		localLabels.AddRange(ha.localLabels)
		localVariables.AddRange(ha.localVariables)
		nodes.AddRange(ha.nodes)

	def __init__(self, ha):
		self.__targetType = ""
		DisplayShape = ha.DisplayShape
		TargetType = ha.GetType().ToString()
		localLabels.AddRange(ha.localLabels)
		localVariables.AddRange(ha.localVariables)
		nodes.AddRange(ha.nodes)

	def copy(self):
		copyOfNode = ruleHyperarc()
		self.copy(copyOfNode)
		return copyOfNode

	def copy(self, copyOfHyperArc):
		self.copy(copyOfHyperArc)
		if :
			rcopy = copyOfHyperArc
			rcopy.containsAllLocalLabels = containsAllLocalLabels
			rcopy.strictNodeCountMatch = strictNodeCountMatch
			enumerator = negateLabels.GetEnumerator()
			while enumerator.MoveNext():
				label = enumerator.Current
				rcopy.negateLabels.Add(label)

	def get_negateLabels(self):
		return self.__negateLabels == (self.__negateLabels = List[str]())

	negateLabels = property(fget=get_negateLabels)

	def get_NotExist(self):

	def set_NotExist(self, value):

	NotExist = property(fget=get_NotExist, fset=set_NotExist)

	def get_containsAllLocalLabels(self):

	def set_containsAllLocalLabels(self, value):

	containsAllLocalLabels = property(fget=get_containsAllLocalLabels, fset=set_containsAllLocalLabels)

	def get_TargetType(self):
		return self.__targetType

	def set_TargetType(self, value):
		t = None
		if value != None:
			t = Type.GetType(value)
		if t == None:
			t = Type.GetType("GraphSynth." + value)
		if t == None:
			t = Type.GetType("GraphSynth.Representation." + value)
		if t != None:
			self.__targetType = t.ToString()
		else:
			self.__targetType = value

	TargetType = property(fget=get_TargetType, fset=set_TargetType)
 # <summary>
	# Gets or sets a value indicating whether [strict node count match].
	# </summary>
	# <value>
	# 	<c>true</c> if [strict node count match]; otherwise, <c>false</c>.
	# </value>
	def get_strictNodeCountMatch(self):

	def set_strictNodeCountMatch(self, value):

	strictNodeCountMatch = property(fget=get_strictNodeCountMatch, fset=set_strictNodeCountMatch)

	# this boolean is to distinguish that a particular hyperarc
	# * of L has all of the nodes of the host hyperarc. Again,
	# * if true then use equal if false then use subset
	# <summary>
	# Gets the degree of the hyperarcs - the number of nodes that it connects to.
	#  A slight difference exists for ruleNode since we don't want to count "NotExist" arcs.
	# </summary>
	# <value>The degree.</value>
	def get_degree(self):
		return nodes.Count()

	degree = property(fget=get_degree)