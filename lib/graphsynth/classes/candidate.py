"""Base class for candidates.
The candidate class is a little more than wrapper to NetworkX Graph.
While the graph is essentially what we are interested in, the
candidate also includes some other essential information. For example,
what is the worth of the graph (performance parameters), and what is
the recipe, or list of options that were called to create the graph (recipe).

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

__author__ = """\n""".join(['Matt Campbell (mattica@gmail.com)'])


class Candidate(object):

	# a candidate can be made with nothing or by passing the graph that will be set
	# * to its current state.
	def __init__(self, _graph, numRuleSets):
		""" Initializes a new instance of the candidate class."""
		self._prevStates = []
		# All the previous states of the graph are stored within a candidate. This makes candidate a
		#   'heavy' class, but it allows us to go back to how it existed quickly.
		self._GenerationStatus = []
		#   Just like the discussion for activeRuleSetIndex, GenerationStatus stores what has
		#   happened during the RCA generation loop. The is one for each ruleSet as each ruleSet
		#   may have ended in a different way.
		self._performanceParams = []
		#   a list of numbers used to define a candidate's worth. While this is a public field, 
		#   it may be less buggy to write code using the properties f0, f1, f2, f3, and f4 stored
		self._recipe = []
		#   the recipe is a list of all the options that were chosen to create the candidate.
		#   Option is stored under representation. Each option contains, the rulesetindex,
		#   the number of the rule, a reference to the rule, and the location of where the rule
		#   was applied.
		
		# </summary>
		self._designParameters = [] #   a list of numbers used to define a candidate's design or decision variables. This is
		#   typically used to define parameters within the graph.
		graph = _graph
		#   Gets or sets the graph. Stating a candidate's graph is simply it's current state. 
		#   However, if this property is used in to set the graph to a new one, then we move 
		#   the current state onto the prevStates list.
		i = 0
		while i != numRuleSets:
			self._GenerationStatus.Add(GenerationStatuses.Unspecified)
			i += 1

	def get_graph(self):

	def set_graph(self, value):

	graph = property(get_graph, set_graph)

	def get_graphFileName(self):

	def set_graphFileName(self, value):

	graphFileName = property(fget=get_graphFileName, fset=set_graphFileName)

	def get_activeRuleSetIndex(self):

	def set_activeRuleSetIndex(self, value):

	activeRuleSetIndex = property(fget=get_activeRuleSetIndex, fset=set_activeRuleSetIndex)

	def get_age(self):

	def set_age(self, value):

	age = property(fget=get_age, fset=set_age)

	def get_numRulesCalled(self):
		return self._recipe.Count

	numRulesCalled = property(fget=get_numRulesCalled)

	def get_lastRuleSetIndex(self):
		if self._recipe.Count == 0:
			return -1
		return self._recipe.Last().ruleSetIndex

	lastRuleSetIndex = property(fget=get_lastRuleSetIndex)

	def get_f0(self):
		if self._performanceParams.Count < 1:
			return Double.NaN
		return self._performanceParams[0]

	def set_f0(self, value):
		if self._performanceParams.Count < 1:
			self._performanceParams.Add(value)
		else:
			self._performanceParams[0] = value

	f0 = property(fget=get_f0, fset=set_f0)

	def get_f1(self):
		if self._performanceParams.Count < 2:
			return Double.NaN
		return self._performanceParams[1]

	def set_f1(self, value):
		if self._performanceParams.Count < 2:
			self.f0 = self.f0
			self._performanceParams.Add(value)
		else:
			self._performanceParams[1] = value

	f1 = property(fget=get_f1, fset=set_f1)

	def get_f2(self):
		if self._performanceParams.Count < 3:
			return Double.NaN
		return self._performanceParams[2]

	def set_f2(self, value):
		if self._performanceParams.Count < 3:
			self.f0 = self.f0
			self.f1 = self.f1
			self._performanceParams.Add(value)
		else:
			self._performanceParams[2] = value

	f2 = property(fget=get_f2, fset=set_f2)

	def get_f3(self):
		if self._performanceParams.Count < 4:
			return Double.NaN
		return self._performanceParams[3]

	def set_f3(self, value):
		if self._performanceParams.Count < 4:
			self.f0 = self.f0
			self.f1 = self.f1
			self.f2 = self.f2
			self._performanceParams.Add(value)
		else:
			self._performanceParams[3] = value

	f3 = property(fget=get_f3, fset=set_f3)

	def get_f4(self):
		if self._performanceParams.Count < 5:
			return Double.NaN
		return self._performanceParams[4]

	def set_f4(self, value):
		if self._performanceParams.Count < 5:
			self.f0 = self.f0
			self.f1 = self.f1
			self.f2 = self.f2
			self.f3 = self.f3
			self._performanceParams.Add(value)
		else:
			self._performanceParams[4] = value

	f4 = property(fget=get_f4, fset=set_f4)

	def get_ruleNumbersInRecipe(self):
		rNIR = Array.CreateInstance(int, self._recipe.Count)
		i = 0
		while i != self._recipe.Count:
			rNIR[i] = self._recipe[i].ruleNumber
			i += 1
		return rNIR

	ruleNumbersInRecipe = property(fget=get_ruleNumbersInRecipe)

	def get_ruleSetIndicesInRecipe(self):
		rSIIR = Array.CreateInstance(int, self._recipe.Count)
		i = 0
		while i != self._recipe.Count:
			rSIIR[i] = self._recipe[i].ruleSetIndex
			i += 1
		return rSIIR

	ruleSetIndicesInRecipe = property(fget=get_ruleSetIndicesInRecipe)

	def get_optionNumbersInRecipe(self):
		oNIR = Array.CreateInstance(int, self._recipe.Count)
		i = 0
		while i != self._recipe.Count:
			oNIR[i] = self._recipe[i].optionNumber
			i += 1
		return oNIR

	optionNumbersInRecipe = property(fget=get_optionNumbersInRecipe)

	def get_parametersInRecipe(self):
		pIR = Array.CreateInstance(List, self._recipe.Count)
		i = 0
		while i != self._recipe.Count:
			if self._recipe[i].parameters.Count > 0:
				pIR[i].AddRange(self._recipe[i].parameters)
			i += 1
		return pIR

	parametersInRecipe = property(fget=get_parametersInRecipe)

	def saveCurrent(self):
		""" <summary>
		   Saves a copy of the current state to the list of previous states.
		 </summary>
		"""
		if self.graph != None:
			self._prevStates.Add(self.graph.copy())

	def addToRecipe(self, currentOpt):
		""" <summary>
		   Adds to recipe. This is called (currently only) from the RCA loop. This happens
		   directly after the rule is APPLIED. A rule application updates
		   the currentstate, so this correspondingly adds the option to the recipe.
		 </summary>
		 <param name = "currentOpt">The currentrule.</param>
		"""
		self._recipe.Add(currentOpt.copy())

	def undoLastRule(self):
		""" <summary>
		   Undoes the last rule. This is perhaps the whole reason previous states are used.
		   Rules cannot be guaranteed to work in reverse as they work
		   forward, so this simply resets the candidate to how it looked
		   prior to calling the last rule.
		 </summary>
		"""
		if self._prevStates.Count <= 0:
			return 
		self.activeRuleSetIndex = self.lastRuleSetIndex
		self.graph = self._prevStates.Last()
		self._prevStates.RemoveAt(self._prevStates.Count - 1)
		self._recipe.RemoveAt(self._recipe.Count - 1)
		i = 0
		while i != self._performanceParams.Count:
			self._performanceParams[i] = Double.NaN
			i += 1
		self.age = 0

	def copy(self):
		""" Copies this instance of a candidate. Very similar to designGraph copy.
		   We make sure to not do a shallow copy (ala Clone) since we are unsure
		   how each candidate may be changed in the future.
		 """
        return deepcopy(self)
