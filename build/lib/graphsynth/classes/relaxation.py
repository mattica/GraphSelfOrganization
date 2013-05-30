"""Base class for a relaxation rule.

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

class Relaxation(object):
class Relaxation(IEnumerable, IEnumerable):
	""" <summary>
	 
	 </summary>
	"""
	def __init__(self, NumberAllowable):
		""" <summary>
		 Initializes a new instance of the <see cref="Relaxation"/> class.
		 </summary>
		 <param name="prescribedItems">The prescribed items.</param>
		 <param name="NumberAllowable">The number allowable.</param>
		"""
		# <summary>
		# Initializes a new instance of the <see cref="Relaxation"/> class.
		# </summary>
		# <param name="NumberAllowable">The number allowable.</param>
		self._NumberAllowable = self._initialNumberAllowable = NumberAllowable
		if NumberAllowable > 0:
			self._items = List[RelaxItem](RelaxItem(Relaxations.Any, NumberAllowable))

	def __init__(self, NumberAllowable):
		self._NumberAllowable = self._initialNumberAllowable = NumberAllowable
		if NumberAllowable > 0:
			self._items = List[RelaxItem](RelaxItem(Relaxations.Any, NumberAllowable))
 # <summary>
	# Gets the allowable relaxes.
	# </summary>
	def get_InitialAllowableRelaxes(self):

	def set_InitialAllowableRelaxes(self, value):

	InitialAllowableRelaxes = property(fget=get_InitialAllowableRelaxes, fset=set_InitialAllowableRelaxes)

	# <summary>
	# Gets the number allowable relaxations that are left (not initially prescribed).
	# </summary>
	def get_NumberAllowable(self):

	def set_NumberAllowable(self, value):

	NumberAllowable = property(fget=get_NumberAllowable, fset=set_NumberAllowable)

	# <summary>
	# The prescribed relaxation items.
	# </summary>
	# <summary>
	# Gets the fulfilled items.
	# </summary>
	def get_FulfilledItems(self):
		return self._fulfilledItems == (self._fulfilledItems = List[RelaxItem]())

	FulfilledItems = property(fget=get_FulfilledItems)

	# <summary>
	# Gets the summary of relaxation that were used to make the match.
	# </summary>
	def get_RelaxationSummary(self):
		result = ""
		enumerator = fulfilledItems.GetEnumerator()
		while enumerator.MoveNext():
			f = enumerator.Current
			result += "\n" + f.RelaxationType.ToString().Replace('_', ' ')
			result += " on the "
			if f.GraphElement == None:
				result += "LHS graph"
			else:
				result += f.GraphElement.GetType().BaseType.Name + " named " + f.GraphElement.name
			if f.Datum != None:
				result += ": " + f.Datum
		result += ".\n"
		return result.Remove(0, 1)

	RelaxationSummary = property(fget=get_RelaxationSummary)

	def GetEnumerator(self):
		""" <summary>
		 Returns an enumerator that iterates through the collection.
		 </summary>
		 <returns>
		 A <see cref="T:System.Collections.Generic.IEnumerator`1"/> that can be used to iterate through the collection.
		 </returns>
		"""
		return self._items.GetEnumerator()

	def GetEnumerator(self):
		""" <summary>
		 Returns an enumerator that iterates through a collection.
		 </summary>
		 <returns>
		 An <see cref="T:System.Collections.IEnumerator"/> object that can be used to iterate through the collection.
		 </returns>
		"""
		return self.GetEnumerator()

	def copy(self):
		""" <summary>
		 Copies this instance.
		 </summary>
		 <returns></returns>
		"""
		self._items = self._items == (self._items = List[RelaxItem]())
		return Relaxation(fulfilledItems = List[RelaxItem](self.FulfilledItems), InitialAllowableRelaxes = self.InitialAllowableRelaxes, items = self._items.Select().ToList(), NumberAllowable = self.NumberAllowable, initialNumberAllowable = self._initialNumberAllowable)

	def Reset(self):
		""" <summary>
		 Resets the relaxation back to the way it was originally defined.
		 </summary>
		"""
		self.NumberAllowable = self._initialNumberAllowable
		self._fulfilledItems = None
		i = 0
		while i < self.InitialAllowableRelaxes.GetLength(0):
			self._items[i].NumberAllowed = self.InitialAllowableRelaxes[i]
			i += 1

class RelaxItem(object):
	""" <summary>
	 The RelaxItem describes the manner in which one can relax a rule or ruleset.
	 A list of these is defined for the Relaxation class.
	 </summary>
	"""
	# <summary>
	# Gets the elt.
	# </summary>
	def get_GraphElement(self):

	def set_GraphElement(self, value):

	GraphElement = property(fget=get_GraphElement, fset=set_GraphElement)

	# <summary>
	# Gets the type of the relaxation.
	# </summary>
	# <value>
	# The type of the relaxation.
	# </value>
	def get_RelaxationType(self):

	def set_RelaxationType(self, value):

	RelaxationType = property(fget=get_RelaxationType, fset=set_RelaxationType)

	# <summary>
	# Gets the datum.
	# </summary>
	def get_Datum(self):

	def set_Datum(self, value):

	Datum = property(fget=get_Datum, fset=set_Datum)

	# <summary>
	# Gets the applies to.
	# </summary>
	def get_AppliesTo(self):

	def set_AppliesTo(self, value):

	AppliesTo = property(fget=get_AppliesTo, fset=set_AppliesTo)

	class RelaxAppliesTo(object):
		def __init__(self):

	# <summary>
	# Gets or sets the number of relaxations of this type that are allowed.
	# </summary>
	# <value>
	# The number allowed.
	# </value>
	def get_NumberAllowed(self):

	def set_NumberAllowed(self, value):

	NumberAllowed = property(fget=get_NumberAllowed, fset=set_NumberAllowed)

	def __init__(self):
		""" <summary>
		 Initializes a new instance of the <see cref="RelaxItem"/> class.
		 </summary>
		 <param name="RelaxationType">Type of the relaxation.</param>
		 <param name="NumberAllowed">The number allowed.</param>
		 <param name="GraphElement">The graph element.</param>
		 <param name="Datum">The datum.</param>
		"""

	def Matches(self, rType, g, datum):
		if (not str.IsNullOrWhiteSpace(self.Datum)) and (self.Datum != datum):
			return False
		if self.NumberAllowed <= 0:
			return False
		if self.RelaxationType == Relaxations.Any:
			return True
		if bothRevokeAndImpose:
			if not rType.ToString().StartsWith(prefixForAltered):
				return False
		elif self.RelaxationType != rType:
			return False
		if g == None:
			return True
		if self.GraphElement != None:
			return (self.GraphElement == g)
		# in the remaining cases, g is not null, but GraphElement is, so we need to look at "Applies To"
		if self.AppliesTo == RelaxAppliesTo.element:
			return True
		return (( and self.AppliesTo == RelaxAppliesTo.node) or ( and self.AppliesTo == RelaxAppliesTo.arc) or ( and self.AppliesTo == RelaxAppliesTo.hyperarc))

class Relaxations(object):
	""" <summary>
	 The enumerator of the Relaxation Types
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 The enumerator of the Relaxation Types
		 </summary>
		"""

	# <summary>
	# Any is a wildcard for any of the following specific types of relaxations
	# </summary> # <summary>
	# the contains all global labels condition is revoked
	# </summary>
	# <summary>
	# the ordered global labels condition is revoked 
	# </summary>
	# <summary>
	# a global label as indicated by |DATUM| is revoked.
	# </summary>
	# <summary>
	# a global negating label as indicated by |DATUM| is revoked.
	# </summary>
	# <summary>
	# the spanning restriction is revoked
	# </summary> # <summary>
	# A particular additional functions as indicated by |DATUM| is revoked.
	# </summary>
	# <summary>
	# all shape restrictions are revoked
	# </summary>
	# <summary>
	# the induced condition is revoked (set to false)
	# </summary> # <summary>
	# the contains all local labels condition of the |GraphElement| is revoked
	# </summary>
	# <summary>
	# the contains all local labels condition of the |GraphElement| is imposed 
	# to prevent a match for negative (NOT_EXIST) elements.
	# </summary>
	# <summary>
	# the contains all local labels condition of the |GraphElement| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# a label of the |GraphElement| as named in |DATUM| is revoked.
	# </summary>
	# <summary>
	# a label of the |GraphElement| as named in |DATUM| is imposed 
	# to prevent a match for negative (NOT_EXIST) elements. 
	# </summary>
	# <summary>
	# a label of the |GraphElement| as named in |DATUM| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# the negating label of the |GraphElement| as named in |DATUM| is revoked.
	# </summary>
	# <summary>
	# the negating label of the |GraphElement| as named in |DATUM| is imposed 
	# to prevent a match for negative (NOT_EXIST) elements.
	# </summary>
	# <summary>
	# the negating label of the |GraphElement| as named in |DATUM| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# the NullMeansNull condition of the arc indicated by |GraphElement| is revoked
	# (treated as false).
	# </summary>
	# <summary> 
	# the NullMeansNull condition of the arc indicated by |GraphElement| is imposed 
	# (set as true) to prevent a match for negative (NOT_EXIST) elements.
	# </summary>
	# <summary>
	# the NullMeansNull condition of the arc indicated by |GraphElement| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# the DirectionIsEqual condition of the arc indicated by |GraphElement| is revoked
	# </summary>
	# <summary>
	# the DirectionIsEqual condition of the arc indicated by |GraphElement| is imposed 
	# to prevent a match for negative (NOT_EXIST) elements.
	# </summary>
	# <summary>
	# the DirectionIsEqual condition of the arc indicated by |GraphElement| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# Strict Degree Match of the node indicated by |GraphElement| is revoked
	# </summary>
	# <summary>
	# Strict Degree Match of the node indicated by |GraphElement| is imposed 
	# to prevent a match for negative (NOT_EXIST) elements.
	# </summary>
	# <summary>
	# Strict Degree Match of the node indicated by |GraphElement| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# Strict Node Count of the hyperarc indicated by |GraphElement| is revoked
	# </summary>
	# <summary>
	# Strict Node Count of the hyperarc indicated by |GraphElement| is imposed 
	# to prevent a match for negative (NOT_EXIST) elements.
	# </summary>
	# <summary>
	# Strict Node Count of the hyperarc indicated by |GraphElement| can be
	# either revoked (for positivie elements) or imposed (for negative elements).
	# </summary>
	# <summary>
	# hyperarc preclusion is revoked, meaning that a node actually
	# connects to a hyperarc (as indicated by |DATUM|) in L (even 
	# though L shows them disconnected).
	# </summary>
	# <summary>
	# the target type of the |GraphElement| is revoked
	# </summary> # <summary>
	# the NOTEXIST condition of |GraphElement| is revoked, but it must be found
	# as if a positive element.
	# </summary>
	# <summary>
	# the element as indicated by |GraphElement| is removed from L
	# </summary>
