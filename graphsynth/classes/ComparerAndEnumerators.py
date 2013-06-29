# ************************************************************************
# *     This file includes definitions for fundamental enumerators and the
# *     OptimizeSort Comparer which are part of the GraphSynth.BaseClasses
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
from System.Collections.Generic import *

class choiceMethods(object):
	""" <summary>
	 Defines whether the choice method of a particular ruleset is done
	 by some design agent (human or computer) or is automatic - meaning 
	 once a rule is found to be recognized on a host, it is invoked.
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 Defines whether the choice method of a particular ruleset is done
		 by some design agent (human or computer) or is automatic - meaning 
		 once a rule is found to be recognized on a host, it is invoked.
		 </summary>
		"""

	# <summary>
	# A set of options are first defined by an exhaustive recognition
	# of all rules in the ruleset. The decision of which option to 
	# choose is left to some design agent.
	# </summary>
	# <summary>
	# Whenever a rule is recognized it is invoked. Rules invoked in 
	# the order presented in the ruleset.
	# </summary>
class feasibilityState(object):
	""" <summary>
	 Defines whether the candidates created by a particular ruleset 
	 are feasible candidates and hence ready for evaluation, or
	 developing candidates which are yet to completed.
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 Defines whether the candidates created by a particular ruleset 
		 are feasible candidates and hence ready for evaluation, or
		 developing candidates which are yet to completed.
		 </summary>
		"""

	# <summary/>
	# <summary>
	# Candidates are not yet complete, they are still 
	# developing; not ready for evaluation.
	# </summary>
	# <summary>
	# Candidates are feasible and ready for evaluation.
	# </summary>
class nextGenerationSteps(object):
	""" <summary>
	 Defines how the generation process is to continue.
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 Defines how the generation process is to continue.
		 </summary>
		"""
		self._Unspecified = 		# <summary />
-5
		self._Stop = 		# <summary>
		# stop the generation process
		# </summary>
-4
		self._Loop = 		# <summary>
		# loop within current ruleset
		# </summary>
-3
		self._GoToPrevious = 		# <summary>
		# go to the previous ruleset
		# </summary>
-2
		self._GoToNext = 		# <summary>
		# go to the next ruleset
		# </summary>
-1
		self._GoToRuleSet0 = 		# <summary>
		# go to ruleset #0
		# </summary>
0
		self._GoToRuleSet1 = 		# <summary>
		# go to ruleset #1
		# </summary>
1
		self._GoToRuleSet2 = 		# <summary>
		# go to ruleset #2
		# </summary>
2
		self._GoToRuleSet3 = 		# <summary>
		# go to ruleset #3
		# </summary>
3
		self._GoToRuleSet4 = 		# <summary>
		# go to ruleset #4
		# </summary>
4
		self._GoToRuleSet5 = 		# <summary>
		# go to ruleset #5
		# </summary>
5
		self._GoToRuleSet6 = 		# <summary>
		# go to ruleset #6
		# </summary>
6
		self._GoToRuleSet7 = 		# <summary>
		# go to ruleset #7
		# </summary>
7
		self._GoToRuleSet8 = 		# <summary>
		# go to ruleset #8
		# </summary>
8
		self._GoToRuleSet9 = 		# <summary>
		# go to ruleset #9
		# </summary> 
9
		self._GoToRuleSet10 = 		# <summary>
		# go to ruleset #10
		# </summary>
10

class GenerationStatuses(object):
	""" <summary>
	 Enumerator Declaration for How Generation Ended, GenerationStatus 
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 Enumerator Declaration for How Generation Ended, GenerationStatus 
		 </summary>
		"""
		self._Unspecified = 		# <summary />
-1

	# <summary>
	# Following a normal cycle through the RCA loop.
	# </summary>
	# <summary>
	# Following the choosing step of the RCA loop.
	# </summary>
	# <summary>
	# Following the a maximum number of cycle through the RCA loop.
	# </summary>
	# <summary>
	# Following no rules having been recognized.
	# </summary>
	# <summary>
	# Following the application of a trigger rule.
	# </summary>
class optimize(object):
	"""<summary>
	 Enumerator for Search functions that have generality
	 to either minimize or maximize (e.g. PNPPS, stochasticChoose). */
	</summary>
	"""
	def __init__(self):
		"""<summary>
		 Enumerator for Search functions that have generality
		 to either minimize or maximize (e.g. PNPPS, stochasticChoose). */
		</summary>
		"""
		self._minimize = 		# <summary>
		# Minimize in the search - smaller is better.
		# </summary>
-1
		self._maximize = 		# <summary>
		# Maximize in the search - bigger is better.
		# </summary>
1

class ConfluenceAnalysis(object):
	""" <summary>
	 Calculating the confluence between options is a complex task which may take an
	 unintended amount of time to determine. In order to control this three possible
	 analyses are defined. 
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 Calculating the confluence between options is a complex task which may take an
		 unintended amount of time to determine. In order to control this three possible
		 analyses are defined. 
		 </summary>
		"""

	# <summary>
	# A simple analysis that may produce a number of "unknown" states. Any unknown
	# states are regarded as NOT confluent, even though they may be.
	# </summary>
	# <summary>
	# A simple analysis that may produce a number of "unknown" states. Any unknown
	# states are regarded as confluent, even though they may not be.
	# </summary>
	# <summary>
	# The full analysis will run the empirical test for invalidation between a pair
	# of options. This is potentially time-consuming.
	# </summary>
class OptimizeSort(IComparer):
	""" <summary>
	 A comparer for optimization that can be used for either 
	 minimization or maximization.
	 </summary>
	"""
	# an internal integer equal to the required sort direction.
	def __init__(self, direction):
		""" <summary>
		 Initializes a new instance of the <see cref="OptimizeSort"/> class.
		 </summary>
		 <param name="direction">The direction.</param>
		"""
		self._direction = direction

	def Compare(self, x, y):
		""" <summary>
		 Compares two objects and returns a value indicating whether the 
		 first one is better than the second one. "Better than" is defined
		 by the optimize direction provided in the constructor. In order to
		 avoid errors in the sorting, we make sure that only -1 or 1 is 
		 returned. If they are equal, we return 1. This makes newer items to
		 the list appear before older items. It is slightly more efficient than 
		 returning -1 and conforms with the philosophy of always exploring or
		 preferring new concepts. See: SA's Metropolis Criteria.
		 </summary>
		 <returns>
		 A signed integer that indicates the relative values of <paramref name="x"/> and <paramref name="y"/>, as shown in the following table.Value Meaning Less than zero<paramref name="x"/> is less than <paramref name="y"/>.Zero<paramref name="x"/> equals <paramref name="y"/>.Greater than zero<paramref name="x"/> is greater than <paramref name="y"/>.
		 </returns>
		 <param name="x">The first object to compare.</param><param name="y">The second object to compare.</param>
		"""
		if x == y:
			return 1
		if x < y:
			return self._direction
		return -1 * self._direction

class transfromType(object):
	""" <summary>
	 Defines the constraint on how shapes/coordinates are transformed. 
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 Defines the constraint on how shapes/coordinates are transformed. 
		 </summary>
		"""

	# <summary>
	# This type of transform is not recognized/performed.
	# </summary>
	# <summary>
	# This type of transform is recognized/performed only in the X-direction.
	# </summary>
	# <summary>
	# This type of transform is recognized/performed only in the Y-direction.
	# </summary>
	# <summary>
	# This type of transform is recognized/performed uniformly in both X and Y.
	# </summary>
	# <summary>
	# This type of transform is recognized/performed in both X and Y independently.
	# </summary>