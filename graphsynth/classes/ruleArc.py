# ************************************************************************
# *     This ruleArc file & class is part of the GraphSynth.BaseClasses
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
# here we define additional qualities used only by arcs in the grammar rules.
class ruleArc(arc):
	""" <summary>
	   The ruleArc class is an inherited class from arc which includes additional details
	   necessary to correctly perform recognition. This mostly hinges on the "subset or equal"
	   Booleans.
	 </summary>
	"""
	def __init__(self, a):
		""" <summary>
		   Initializes a new instance of the <see cref = "ruleArc" /> class with a particular name.
		 </summary>
		 <param name = "newName">The new name.</param>
		"""
		# <summary>
		#   Initializes a new instance of the <see cref = "ruleArc" /> class.
		# </summary>
		# <summary>
		# Initializes a new instance of the <see cref="ruleArc"/> class.
		#   Converts an arc to a ruleArc and returns it with default Booleans.
		#   The original arc is unaffected.
		# </summary>
		# <param name="a">A.</param>
		# <summary>
		#   Returns a copy of this instance.
		# </summary>
		# <returns>the copy of the arc.</returns>
		# <summary>
		#   Copies this instance into the (already intialized) copyOfArc.
		# </summary>
		# <param name = "copyOfArc">A new copy of arc.</param> # <summary>
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
		TargetType = a.GetType().ToString()
		directed = a.directed
		DisplayShape = a.DisplayShape
		doublyDirected = a.doublyDirected
		From = a.From
		To = a.To
		localLabels.AddRange(a.localLabels)
		localVariables.AddRange(a.localVariables)

	def __init__(self, a):
		self.__targetType = ""
		TargetType = a.GetType().ToString()
		directed = a.directed
		DisplayShape = a.DisplayShape
		doublyDirected = a.doublyDirected
		From = a.From
		To = a.To
		localLabels.AddRange(a.localLabels)
		localVariables.AddRange(a.localVariables)

	def __init__(self, a):
		self.__targetType = ""
		TargetType = a.GetType().ToString()
		directed = a.directed
		DisplayShape = a.DisplayShape
		doublyDirected = a.doublyDirected
		From = a.From
		To = a.To
		localLabels.AddRange(a.localLabels)
		localVariables.AddRange(a.localVariables)

	def copy(self):
		copyOfArc = ruleArc()
		self.copy(copyOfArc)
		return copyOfArc

	def copy(self, copyOfArc):
		self.copy(copyOfArc)
		if :
			rcopy = copyOfArc
			rcopy.containsAllLocalLabels = containsAllLocalLabels
			rcopy.directionIsEqual = directionIsEqual
			rcopy.nullMeansNull = nullMeansNull
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
 # The following booleans capture the possible ways in which an arc may/may not be a subset
	# * (boolean set to false) or is equal (in this respective quality) to the host (boolean set
	# * to true). These are special subset or equal booleans used by recognize. For this
	# * fundamental arc classes, only these three possible conditions exist.
	# <summary>
	#   Gets or sets a value indicating whether the directionality within the arc is to match
	#   perfectly. If false then all (singly)-directed arcs
	#   will match with doubly-directed arcs, and all undirected arcs will match with all
	#   directed and doubly-directed arcs. Of course, a directed arc going one way will 
	#   still not match with a directed arc going the other way.
	#   If true, then undirected only matches with undirected, directed only with directed (again, the
	#   actual direction must match too), and doubly-directed only with doubly-directed.
	# </summary>
	# <value><c>true</c> if [direction is equal]; otherwise, <c>false</c>.</value>
	def get_directionIsEqual(self):

	def set_directionIsEqual(self, value):

	directionIsEqual = property(fget=get_directionIsEqual, fset=set_directionIsEqual)

	# <summary>
	#   Gets or sets a value indicating whether dangling (the null reference to node) arc are only
	#   to match with dangling arcs.If this is set to false, then we are saying a 
	#   null reference on an arc can be matched with a null in the graph or any node in the graph. 
	#   Like the above, a false value is like a subset in that null is a subset of any actual node. 
	#   And a true value means it must match exactly or in otherwords, "null means null" - null 
	#   matches only with a null in the host. If you want the rule to be recognized only when an actual
	#   node is present simply add a dummy node with no distinguishing characteristics. That would
	#   in turn nullify this boolean since this boolean only applies when a null pointer exists in
	#   the rule.
	# </summary>
	# <value><c>true</c> if [null means null]; otherwise, <c>false</c>.</value>
	def get_nullMeansNull(self):

	def set_nullMeansNull(self, value):

	nullMeansNull = property(fget=get_nullMeansNull, fset=set_nullMeansNull)