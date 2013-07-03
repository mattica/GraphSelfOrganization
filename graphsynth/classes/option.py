"""Base class for option.
A rule is not enough - the Option class captures all the details of
an decision option from one point in the search process. The list of
options are presented in the choice for which rule to apply. Option
contains references to the location where the rule is applicable,
the rule itself, along with its number in the ruleSet and the ruleSet's
number when there are multiple ruleSets.
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

class option(object):
	# <summary>
	#   A list of parameters chosen and used by the apply fuctions of the rule.
	# </summary>
	# <summary />
	# <summary />
	# <summary />
	# <summary>
	#   Gets or sets the arcs.
	# </summary>
	# <value>The arcs.</value>
	def get_arcs(self):
		return self.__arcs == (self.__arcs = List[arc]())

	def set_arcs(self, value):
		self.__arcs = value

	arcs = property(fget=get_arcs, fset=set_arcs)

	# <summary>
	#   Gets the nodes.
	# </summary>
	# <value>The nodes.</value>
	def get_nodes(self):
		return self.__nodes == (self.__nodes = List[node]())

	def set_nodes(self, value):
		self.__nodes = value

	nodes = property(fget=get_nodes, fset=set_nodes)

	# <summary>
	#   Gets the hyperarcs.
	# </summary>
	# <value>The hyperarcs.</value>
	def get_hyperarcs(self):
		return self.__hyperarcs == (self.__hyperarcs = List[hyperarc]())

	def set_hyperarcs(self, value):
		self.__hyperarcs = value

	hyperarcs = property(fget=get_hyperarcs, fset=set_hyperarcs)

	# <summary>
	#   Gets or sets the option number.
	# </summary>
	# <value>The option number.</value>
	def get_optionNumber(self):

	def set_optionNumber(self, value):

	optionNumber = property(fget=get_optionNumber, fset=set_optionNumber)

	# <summary>
	#   Gets or sets the index of the rule set.
	# </summary>
	# <value>The index of the rule set.</value>
	def get_ruleSetIndex(self):

	def set_ruleSetIndex(self, value):

	ruleSetIndex = property(fget=get_ruleSetIndex, fset=set_ruleSetIndex)

	# <summary>
	#   Gets or sets the rule number.
	# </summary>
	# <value>The rule number.</value>
	def get_ruleNumber(self):

	def set_ruleNumber(self, value):

	ruleNumber = property(fget=get_ruleNumber, fset=set_ruleNumber)

	def get_rule(self):

	def set_rule(self, value):

	rule = property(fget=get_rule, fset=set_rule)

	# <summary>
	#   Gets or sets the rule.
	# </summary>
	# <value>The rule.</value>
	# <summary>
	#   Gets or sets the global label start loc.
	# </summary>
	# <value>The global label start loc.</value>
	def get_globalLabelStartLoc(self):

	def set_globalLabelStartLoc(self, value):

	globalLabelStartLoc = property(fget=get_globalLabelStartLoc, fset=set_globalLabelStartLoc)

	def get_positionTransform(self):

	def set_positionTransform(self, value):

	positionTransform = property(fget=get_positionTransform, fset=set_positionTransform)

	# <summary>
	#   Gets or sets the position transform.
	# </summary>
	# <value>The position transform.</value>
	# <summary>
	#   Gets or sets the confluence.
	# </summary>
	# <value>The confluence.</value>
	def get_confluence(self):

	def set_confluence(self, value):

	confluence = property(fget=get_confluence, fset=set_confluence)

	# <summary>
	#   Gets or sets the probability.
	# </summary>
	# <value>The probability.</value>
	def get_probability(self):

	def set_probability(self, value):

	probability = property(fget=get_probability, fset=set_probability)

	def __init__(self):
		""" <summary>
		 Initializes a new instance of the <see cref="option"/> class.
		 </summary>
		 <param name="rule">The rule.</param>
		"""
		self._parameters = List[Double]()

	def apply(self, host, Parameters):
		""" <summary>
		   Applies the option to the specified host. It is essentially
		   a shorthand instead of calling 
		   option.rule.apply(option.location, host, parameters); we call
		   option.apply(host, parameters).
		 </summary>
		 <param name = "host">The host.</param>
		 <param name = "Parameters">The parameters.</param>
		"""
		self.rule.apply(host, self, Parameters)

	def copy(self):
		""" <summary>
		   Returns a copy of this instance of option. Note that location is a 
		   shallow copy and applies to the same host.
		 </summary>
		 <returns></returns>
		"""
		copyOfOption = option(globalLabelStartLoc = self.globalLabelStartLoc, nodes = List[node](self.nodes), arcs = List[arc](self.arcs), hyperarcs = List[hyperarc](self.hyperarcs), optionNumber = self.optionNumber, parameters = List[Double](self._parameters), positionTransform = self.positionTransform, probability = self.probability, Relaxations = self.Relaxations.copy(), rule = self.rule, ruleNumber = self.ruleNumber, ruleSetIndex = self.ruleSetIndex)
		return copyOfOption

	def assignRuleInfo(self, ruleIndex, RuleSetIndex):
		self.ruleNumber = ruleIndex
		self.ruleSetIndex = RuleSetIndex
		return self

	def findLMappedElement(self, GraphElementName):
		""" <summary>
		 Finds the L mapped element.
		 </summary>
		 <param name="GraphElementName">Name of the graph element.</param>
		 <returns></returns>
		 <exception cref="System.Exception">Graph element named \ + GraphElementName + \ was not found in the L-mapping of rule  + GraphElementName</exception>
		"""
		elt = self.rule.L[GraphElementName]
		if elt != None:
			return self.findLMappedElement(elt)
		raise Exception("Graph element named \"" + GraphElementName + "\" was not found in the L-mapping of rule " + GraphElementName)

	def findLMappedElement(self, x):
		""" <summary>
		 Finds the L mapped element.
		 </summary>
		 <param name="x">The x.</param>
		 <returns></returns>
		 <exception cref="System.Exception">Graph element not found in rule's left-hand-side (GrammarRule.findMappedElement)</exception>
		"""
		if :
			return self.findLMappedHyperarc(x)
		if :
			return self.findLMappedNode(x)
		if :
			return self.findLMappedArc(x)
		raise Exception("Graph element not found in rule's left-hand-side (GrammarRule.findMappedElement)")

	def findLMappedNode(self, x):
		""" <summary>
		 Finds the L mapped node.
		 </summary>
		 <param name="x">The x.</param>
		 <returns></returns>
		"""
		return self.nodes[self.rule.L.nodes.IndexOf(x)]

	def findLMappedArc(self, x):
		""" <summary>
		 Finds the L mapped arc.
		 </summary>
		 <param name="x">The x.</param>
		 <returns></returns>
		"""
		return self.arcs[self.rule.L.arcs.IndexOf(x)]

	def findLMappedHyperarc(self, x):
		""" <summary>
		 Finds the L mapped hyperarc.
		 </summary>
		 <param name="x">The x.</param>
		 <returns></returns>
		"""
		return self.hyperarcs[self.rule.L.hyperarcs.IndexOf(x)]

	def AssignOptionConfluence(options, cand, confluenceAnalysis):
		""" <summary>
		 Create lists on integers within each option that indicates what other
		 options in that list it is confluent with. As discussed below confluence
		 is commutative which saves a little time in this function, but it is not
		 transitive - meaning is A is confluent with B and C. It is not necessarily
		 true that B is confluent with C.
		 </summary>
		 <param name="options">The list of options to assign confluence</param>
		 <param name="cand">The cand.</param>
		 <param name="confluenceAnalysis">The confluence analysis.</param>
		 <returns></returns>
		"""
		numOpts = options.Count
		invalidationMatrix = option.MakeInvalidationMatrix(options, cand, confluenceAnalysis)
		enumerator = options.GetEnumerator()
		while enumerator.MoveNext():
			o = enumerator.Current
			o.confluence = List[int]()
		i = 0
		while i < numOpts - 1:
			j = i + 1
			while j < numOpts:
				if confluenceAnalysis == ConfluenceAnalysis.OptimisticSimple:
					if invalidationMatrix[i][j] <= 0 and invalidationMatrix[j][i] <= 0:
						options[i].confluence.Add(j)
						options[j].confluence.Add(i)
					elif invalidationMatrix[i][j] < 0 and invalidationMatrix[j][i] < 0:
						options[i].confluence.Add(j)
						options[j].confluence.Add(i)
				j += 1
			i += 1
		return invalidationMatrix

	AssignOptionConfluence = staticmethod(AssignOptionConfluence)

	def MakeInvalidationMatrix(options, cand, confluenceAnalysis):
		""" <summary>
		 Makes the invalidation matrix.
		 </summary>
		 <param name="options">The options.</param>
		 <param name="cand">The cand.</param>
		 <param name="confluenceAnalysis">The confluence analysis.</param>
		 <returns></returns>
		"""
		numOpts = options.Count
		invalidationMatrix = Array.CreateInstance(int, numOpts, numOpts)
		i = 0
		while i < numOpts:
			j = 0
			while j < numOpts:
				invalidationMatrix[i][j] = option.doesPInvalidateQ(options[i], options[j], cand, confluenceAnalysis)
				j += 1
			i += 1

	MakeInvalidationMatrix = staticmethod(MakeInvalidationMatrix)

	def doesPInvalidateQ(p, q, cand, confluenceAnalysis):
		""" <summary>
		 Predicts whether the option p is invalidates option q.
		 This invalidata is a tricky thing. For the most part, this function
		 has been carefully coded to handle almost all cases. The only exceptions
		 are from what the additional recognize and apply functions require or modify.
		 This is handled by actually testing to see if this is true.
		 </summary>
		 <param name="p">The p.</param>
		 <param name="q">The q.</param>
		 <param name="cand">The cand.</param>
		 <param name="confluenceAnalysis">The confluence analysis.</param>
		 <returns></returns>
		"""
		pIntersectLabels = p.rule.L.globalLabels.Intersect(p.rule.R.globalLabels)
		pRemovedLabels = List[str](p.rule.L.globalLabels)
		pRemovedLabels.RemoveAll()
		pAddedLabels = List[str](p.rule.R.globalLabels)
		pAddedLabels.RemoveAll() # first check that there are no labels deleted that the other depeonds on
		if (q.rule.L.globalLabels.Intersect(pRemovedLabels).Any()) or 		# adding labels is problematic if the other rule was recognized under
		# * the condition of containsAllLocalLabels.
((q.rule.containsAllGlobalLabels) and (pAddedLabels.Any())) or 		# adding labels is also problematic if you add a label that negates the
		# * other rule.
(pAddedLabels.Intersect(q.rule.negateLabels).Any()):
			return 1 # first we check the nodes. If two options do not share any nodes, then
		# * the whole block of code is skipped. q is to save time if comparing many
		# * options on a large graph. However, since there is some need to understand what
		# * nodes are saved in rule execution, the following two lists are defined outside
		# * of q condition and are used in the Arcs section below.
		# why are the following three parameters declared here and not in scope with the
		# * other node parameters below? This is because they are used in the induced and
		# * shape restriction calculations below - why calculate twice?
		Num_pKNodes = 0
		pNodesKNames = None
		pKNodes = None
		commonNodes = q.nodes.Intersect(p.nodes)
		if commonNodes.Any():
			# if there are no common nodes, then no need to check the details.
			# the following arrays of nodes are within the rule not the host.
			pNodesLNames = 
			pNodesRNames = 
			pNodesKNames = pNodesRNames.Intersect(pNodesLNames).ToArray()
			Num_pKNodes = pNodesKNames.GetLength(0)
			pKNodes = Array.CreateInstance(node, Num_pKNodes)
			i = 0
			while i < p.rule.L.nodes.Count:
				index = Array.IndexOf(pNodesKNames, p.rule.L.nodes[i].name)
				if index >= 0:
					pKNodes[index] = p.nodes[i]
				elif commonNodes.Contains(p.nodes[i]):
					return 1
				i += 1 # in the above regions where deletions are checked, we also create lists for potentially
			# * modified nodes, nodes common to both L and R. We will now check these. There are several
			# * ways that a node can be modified:
			# * 1. labels are removed
			# * 2. labels are added (and potentially in the negabels of the other rule).
			# * 3. number of arcs connected, which affect strictDegreeMatch
			# * 4. variables are added/removed/changed
			# *
			# * There first 3 conditions are check all at once below. For the last one, it is impossible
			# * to tell without executing extra functions that the user may have created for rule
			# * recognition. Therefore, additional functions are not check in q confluence check.
			enumerator = commonNodes.GetEnumerator()
			while enumerator.MoveNext():
				commonNode = enumerator.Current
				qNodeL = q.rule.L.nodes[q.nodes.IndexOf(commonNode)]
				pNodeL = p.rule.L.nodes[p.nodes.IndexOf(commonNode)]
				pNodeR = p.rule.R[pNodeL.name]
				pIntersectLabels = pNodeL.localLabels.Intersect(pNodeR.localLabels)
				pRemovedLabels = List[str](pNodeL.localLabels)
				pRemovedLabels.RemoveAll()
				pAddedLabels = List[str](pNodeR.localLabels)
				pAddedLabels.RemoveAll() # first check that there are no labels deleted that the other depeonds on
				if (qNodeL.localLabels.Intersect(pRemovedLabels).Any()) or 				# adding labels is problematic if the other rule was recognized under
				# * the condition of containsAllLocalLabels.
((qNodeL.containsAllLocalLabels) and (pAddedLabels.Any())) or 				# adding labels is also problematic if you add a label that negates the
				# * other rule.
(pAddedLabels.Intersect(qNodeL.negateLabels).Any()) or 				# if one rule uses strictDegreeMatch, we need to make sure the other rule
				# * doesn't change the degree.
(qNodeL.strictDegreeMatch and (pNodeL.degree != pNodeR.degree)) or 				# actually, the degree can also change from free-arc embedding rules. These
				# * are checked below.
(qNodeL.strictDegreeMatch and (p.rule.embeddingRules.FindAll().Count > 0)):
					return 1
		commonArcs = q.arcs.Intersect(p.arcs)
		if commonArcs.Any():
			# if there are no common arcs, then no need to check the details.
			# the following arrays of arcs are within the rule not the host.
			pArcsLNames = 
			pArcsRNames = 
			pArcsKNames = List[str](pArcsRNames.Intersect(pArcsLNames))
			pKArcs = Array.CreateInstance(arc, pArcsKNames.Count())
			i = 0
			while i < p.rule.L.arcs.Count:
				if pArcsKNames.Contains(p.rule.L.arcs[i].name):
					pKArcs[pArcsKNames.IndexOf(p.rule.L.arcs[i].name)] = p.arcs[i]
				elif commonArcs.Contains(p.arcs[i]):
					return 1
				i += 1
			enumerator = commonArcs.GetEnumerator()
			while enumerator.MoveNext():
				commonArc = enumerator.Current
				qArcL = q.rule.L.arcs[q.arcs.IndexOf(commonArc)]
				pArcL = p.rule.L.arcs[p.arcs.IndexOf(commonArc)]
				pArcR = p.rule.R[pArcL.name]
				pIntersectLabels = pArcL.localLabels.Intersect(pArcR.localLabels)
				pRemovedLabels = List[str](pArcL.localLabels)
				pRemovedLabels.RemoveAll()
				pAddedLabels = List[str](pArcR.localLabels)
				pAddedLabels.RemoveAll() # first check that there are no labels deleted that the other depeonds on
				if (qArcL.localLabels.Intersect(pRemovedLabels).Any()) or 				# adding labels is problematic if the other rule was recognized under
				# * the condition of containsAllLocalLabels.
((qArcL.containsAllLocalLabels) and (pAddedLabels.Any())) or 				# adding labels is also problematic if you add a label that negates the
				# * other rule.
(pAddedLabels.Intersect(qArcL.negateLabels).Any()) or 				# if one rule uses strictDegreeMatch, we need to make sure the other rule
				# * doesn't change the degree.
				# if one rule requires that an arc be dangling for correct recognition (nullMeansNull)
				# * then we check to make sure that the other rule doesn't add a node to it.
((qArcL.nullMeansNull) and (((qArcL.From == None) and (pArcR.From != None)) or ((qArcL.To == None) and (pArcR.To != None)))) or 				# well, even if the dangling isn't required, we still need to ensure that p
				# * doesn't put a node on an empty end that q is expecting to belong
				# * to some other node.
((pArcL.From == None) and (pArcR.From != None) and (qArcL.From != None)) or 				# check the To direction as well
((pArcL.To == None) and (pArcR.To != None) and (qArcL.To != None)) or 				# in q, the rule is not matching with a dangling arc, but we need to ensure that
				# * the rule doesn't remove or re-connect the arc to something else in the K of the rule
				# * such that the recogniation of the second rule is invalidated. q may be a tad strong
				# * (or conservative) as there could still be confluence despite the change in connectivity.
				# * How? I have yet to imagine. But clearly the assumption here is that change in
				# * connectivity prevent confluence.
((pArcL.From != None) and (pNodesKNames != None and pNodesKNames.Contains(pArcL.From.name)) and ((pArcR.From == None) or (pArcL.From.name != pArcR.From.name))) or ((pArcL.To != None) and (pNodesKNames != None and pNodesKNames.Contains(pArcL.To.name)) and ((pArcR.To == None) or (pArcL.To.name != pArcR.To.name))) or 				# Changes in Arc Direction
				# 
				# /* finally we check that the changes in arc directionality (e.g. making
				# * directed, making doubly-directed, making undirected) do not affect
				# * the other rule.
				# Here, the directionIsEqual restriction is easier to check than the
				# * default case where directed match with doubly-directed and undirected
				# * match with directed.
((qArcL.directionIsEqual) and ((not qArcL.directed.Equals(pArcR.directed)) or (not qArcL.doublyDirected.Equals(pArcR.doublyDirected)))) or ((qArcL.directed and not pArcR.directed) or (qArcL.doublyDirected and not pArcR.doublyDirected)):
					return 1 # Onto hyperarcs! q is similiar to nodes - more so than arcs.
		commonHyperArcs = q.hyperarcs.Intersect(p.hyperarcs)
		if commonHyperArcs.Any():
			pHyperArcsLNames = 
			pHyperArcsRNames = 
			pHyperArcsKNames = List[str](pHyperArcsRNames.Intersect(pHyperArcsLNames))
			pKHyperarcs = Array.CreateInstance(hyperarc, pHyperArcsKNames.Count())
			i = 0
			while i < p.rule.L.hyperarcs.Count:
				if pHyperArcsKNames.Contains(p.rule.L.hyperarcs[i].name):
					pKHyperarcs[pHyperArcsKNames.IndexOf(p.rule.L.hyperarcs[i].name)] = p.hyperarcs[i]
				elif commonHyperArcs.Contains(p.hyperarcs[i]):
					return 1
				i += 1
			enumerator = commonHyperArcs.GetEnumerator()
			while enumerator.MoveNext():
				commonHyperArc = enumerator.Current
				qHyperArcL = q.rule.L.hyperarcs[q.hyperarcs.IndexOf(commonHyperArc)]
				pHyperArcL = p.rule.L.hyperarcs[p.hyperarcs.IndexOf(commonHyperArc)]
				pHyperArcR = p.rule.R[pHyperArcL.name]
				pIntersectLabels = pHyperArcL.localLabels.Intersect(pHyperArcR.localLabels)
				pRemovedLabels = List[str](pHyperArcL.localLabels)
				pRemovedLabels.RemoveAll()
				pAddedLabels = List[str](pHyperArcR.localLabels)
				pAddedLabels.RemoveAll() # first check that there are no labels deleted that the other depends on
				if (qHyperArcL.localLabels.Intersect(pRemovedLabels).Any()) or 				# adding labels is problematic if the other rule was recognized under
				# * the condition of containsAllLocalLabels.
((qHyperArcL.containsAllLocalLabels) and (pAddedLabels.Any())) or 				# adding labels is also problematic if you add a label that negates the
				# * other rule.
(pAddedLabels.Intersect(qHyperArcL.negateLabels).Any()) or 				# if one rule uses strictDegreeMatch, we need to make sure the other rule
				# * doesn't change the degree.
(qHyperArcL.strictNodeCountMatch and (pHyperArcL.degree != pHyperArcR.degree)):
					# actually, the degree can also change from free-arc embedding rules. These
					# * are checked below.
					return 1
		if commonNodes.Any(): # if q is induced then p will invalidate it, if it adds arcs between the
			# * common nodes.
			if q.rule.induced:
				pArcsLNames = 
				if ().Any():
					return 1
			# is there another situation in which an embedding rule in p may work against
			# * q being an induced rule? It doesn't seem like it would seem embedding rules
			# * reattach free-arcs. oh, what about arc duplication in embedding rules? nah.
			i = 0
			while i < Num_pKNodes:
				pNode = pKNodes[i]
				if commonNodes.Contains(pNode):
					continue
				pname = pNodesKNames[i]
				lNode = p.rule.L[pname]
				rNode = p.rule.R[pname]
				if q.rule.UseShapeRestrictions and p.rule.TransformNodePositions and not (MatrixMath.sameCloseZero(lNode.X, rNode.X) and MatrixMath.sameCloseZero(lNode.Y, rNode.Y) and MatrixMath.sameCloseZero(lNode.Z, rNode.Z)):
					return 1
				if (q.rule.RestrictToNodeShapeMatch and p.rule.TransformNodeShapes) and not (MatrixMath.sameCloseZero(lNode.DisplayShape.Height, rNode.DisplayShape.Height) and MatrixMath.sameCloseZero(lNode.DisplayShape.Width, rNode.DisplayShape.Width) and MatrixMath.sameCloseZero(p.positionTransform[0][0], 1) and MatrixMath.sameCloseZero(p.positionTransform[1][1], 1) and MatrixMath.sameCloseZero(p.positionTransform[1][0]) and MatrixMath.sameCloseZero(p.positionTransform[0][1])):
					return 1
				i += 1
		# you've run the gauntlet of easy check
		# * except (1) if there is something caught by additional recognition functions,
		# * or (2) NOTExist elements now exist. These can only be solving by an empirical
		# * test, which will be expensive.
		# * So, now we switch from conditions that return false to conditions that return true.
		# 
		if q.rule.ContainsNegativeElements or q.rule.recognizeFuncs.Count > 0 or p.rule.applyFuncs.Count > 0:
			if confluenceAnalysis == ConfluenceAnalysis.Full:
				return option.fullInvalidationCheck(p, q, cand)
			else:
				return 0
		return -1

	doesPInvalidateQ = staticmethod(doesPInvalidateQ)

	def fullInvalidationCheck(p, q, cand):
		""" <summary>
		 Does a full invalidation check through empirical evidence. That is, it makes
		 a copy of the graph and tests to see if this is true.
		 </summary>
		 <param name="p">The p.</param>
		 <param name="q">The q.</param>
		 <param name="cand">The cand.</param>
		 <returns></returns>
		"""
		testGraph = cand.graph.copy()
		qCopy = q.copy()
		pCopy = p.copy()
		SearchProcess.transferLmappingToChild(testGraph, cand.graph, pCopy)
		SearchProcess.transferLmappingToChild(testGraph, cand.graph, qCopy)
		pCopy.apply(testGraph, None)
		newOptions = q.rule.recognize(testGraph)
		if newOptions.Any():
			return -1
		else:
			#  find if there is an option in newOptions that is the SAME elements as q.location
			# then return false - p does NOT invalidate q
			return 1

	fullInvalidationCheck = staticmethod(fullInvalidationCheck)

	def sameLocation(qOption, newOption):
		""" <summary>
		 Sames the location.
		 </summary>
		 <param name="qOption">The q option.</param>
		 <param name="newOption">The new option.</param>
		 <returns></returns>
		"""
		if qOption.nodes.Where().Any():
			return False
		if qOption.arcs.Where().Any():
			return False
		if qOption.hyperarcs.Where().Any():
			return False
		return True

	sameLocation = staticmethod(sameLocation)
