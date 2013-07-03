# ************************************************************************
# *     This grammarRule.RecognizeApply.cs file partially defines the
# *     grammarRule class (also partially defined in grammarRule.Basic.cs,
# *     grammarRule.ShapeMethods.cs and grammarRule.NegativeRecognize.cs)
# *     and is part of the GraphSynth.BaseClasses Project which is the
# *     foundation of the GraphSynth Application.
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
from System.Collections import *
from System.Collections.Generic import *
from System.Linq import *
from System.Threading.Tasks import *
# Get ready, this file is complicated. All the recognize and apply functions are found
# * here. There is a recognize function in ruleSet, and an apply in option but those are simply
# * macros for the functions found here within grammarRule.
class grammarRule(object):
	""" <summary>
	 A partial description of the grammar rule class. In addition to storing designGraphs
	 for both the left and right hand sides, there are a variety of functions for describing
	 how a rule recognizes on a host, and how it makes changes via apply.
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 A partial description of the grammar rule class. In addition to storing designGraphs
		 for both the left and right hand sides, there are a variety of functions for describing
		 how a rule recognizes on a host, and how it makes changes via apply.
		 </summary>
		"""
 # The next 300 lines define the recognize functions.
	def recognize(self, host, InParallel, RelaxationTemplate):
		""" <summary>
		 Determines locations where the rule is recognized on the specified host.
		 here is the big one! Although it looks fairly short, a lot of time can be spent in
		 the recursion that it invokes. Before we get to that, we want to make sure that
		 our time there is well spent. As a result, we try to rule out whether the rule
		 can even be applied at first -- hence the series of if-thens. If you don't
		 meet the first, leave now! likewise for the second. The third is a little trickier.
		 if there are no nodes or arcs in this rule, then it has already proven to be valid
		 by the global labels - thus return a single location.
		 The real work happens in the findNewStartElement which is time-consuming so we first
		 do some simply counting to see if the host is bigger than the LHS.
		 When findNewStartElement recurses down and divides, a number of options may be created
		 in the final method (LocationFound). If there are multiple locations within the
		 global labels then we merge the two together.
		 </summary>
		 <param name="host">The host.</param>
		 <param name="InParallel">if set to <c>true</c> [in parallel].</param>
		 <param name="RelaxationTemplate">The relaxation template.</param>
		 <returns></returns>
		"""
		self.__host = host
		self.__in_parallel_ = InParallel
		location = option(self)
		if RelaxationTemplate != None:
			location.Relaxations = RelaxationTemplate.copy()
		options.Clear()
		if not self.InitialRuleCheck() and not self.InitialRuleCheckRelaxed(location):
			return List[option]()
		if ContainsNegativeElements:
			self.FindPositiveStartElementAvoidNegatives(location)
		else:
			self.findNewStartElement(location)
		# if OrderedGlobalLabels is checked and there are multiple locations in the
		# * string of labels then we need to convolve the two set of locations together.
		if OrderedGlobalLabels:
			origLocs = List[option](options)
			options.Clear()
			i = globalLabelStartLocs.Count - 1
			while i >= 0:
				enumerator = origLocs.GetEnumerator()
				while enumerator.MoveNext():
					opt = enumerator.Current
					localOption = opt
					if i > 0:
						localOption = opt.copy()
					localOption.globalLabelStartLoc = globalLabelStartLocs[i]
				i -= 1
		return options

	def findNewStartElement(self, location): # this is the only way to properly exit the recursive loop.
		if not location.nodes.Contains(None) and not location.arcs.Contains(None) and not location.hyperarcs.Contains(None):
			# as a recursive function, we first check how the recognition process terminates. If all nodes,
			# * hyperarcs and arcs within location have been filled with references to elements in the host,
			# * then we've found a location...well maybe. More details are described in the LocationFound function.
			if self.FinalRuleChecks(location) or self.FinalRuleCheckRelaxed(location):
				locCopy = location.copy()
			return  # the quickest approach to finding a new element in the LHS to host subgraph matching is to build
		# * directly off of elements found so far. This is because we don't need to check amongst ALL elements in the
		# * host (as is the case in the last three cases below). In this case we start with any hyperarcs
		# * that have already been matched to one in the host, and see if it connects to any nodes that
		# * have yet to be matched.
		startHyperArc = L.hyperarcs.Find()
		if startHyperArc != None:
			hostHyperArc = location.findLMappedHyperarc(startHyperArc)
			newLNode = startHyperArc.nodes.Find()
			enumerator = hostHyperArc.nodes.Where().GetEnumerator()
			while enumerator.MoveNext():
				n = enumerator.Current
				self.checkNode(location.copy(), newLNode, n)
			return  # as stated above, the quickest approach is to build from elements that have already been found.
		# * Therefore, we see if there are any nodes already matched to a node in L that has an arc in L
		# * that has yet to be matched with a host arc. This is more efficient than the last 3 cases
		# * because they look through the entire host, which is potentially large.
		startNode = L.nodes.Find()
		# is there a node already matched (which would only occur if your recursed to get here) that has an
		# * unrecognized arc attaced to it. If yes, try all possible arcs in the host with the one that needs
		# * to be fulfilled in L.
		if startNode != None:
			newLArc = startNode.arcs.Find()
			if :
				self.checkHyperArc(location, startNode, location.findLMappedNode(startNode), newLArc)
			elif :
				self.checkArc(location, startNode, location.findLMappedNode(startNode), newLArc)
			return  # if the above cases didn't match we try to match a hyperarc in the L to any in the host. Since the
		# * prior three cases have conditions which require some non-nulls in the location, this is likely where the
		# * process will start when invoked from line 87 of recognize above. Hyperarcs are most efficient to start from
		# * since there are likely fewer hyperarcs in the host than nodes, or arcs.
		startHyperArc = L.hyperarcs.Find()
		if startHyperArc != None:
			if self.__in_parallel_:
				Parallel.ForEach(_host.hyperarcs, )
			else:
				enumerator = _host.hyperarcs.Where().GetEnumerator()
				while enumerator.MoveNext():
					hostHyperArc = enumerator.Current
					self.checkHyperArc(location.copy(), startHyperArc, hostHyperArc)
			return  # If no other hyperarcs can be recognized, then look to a unlocated node. If one gets here then none of the above
		# * three conditions were met (obviously) but this also implies that there are multiple components in the
		# * LHS, and we are now jumping to a new one with this. This is potentially time intensive if there are
		# * a lot of nodes in the host. We allow for the possibility that this recognition can be done in parallel.
		startNode = L.nodes.Find()
		if startNode != None:
			if self.__in_parallel_:
				Parallel.ForEach(_host.nodes, )
			else:
				enumerator = _host.nodes.Where().GetEnumerator()
				while enumerator.MoveNext():
					hostNode = enumerator.Current
					self.checkNode(location.copy(), startNode, hostNode)
			return 
		looseArc = L.arcs.Find()
		# the only way one can get here is if there are one or more arcs NOT connected to any nodes
		# * in L - a floating arc, dangling on both sides, like an eyelash.
		if looseArc != None:
			if self.__in_parallel_:
				Parallel.ForEach(_host.arcs, )
			else: #relaxelt
				enumerator = _host.arcs.GetEnumerator()
				while enumerator.MoveNext():
					hostArc = enumerator.Current
					if (not location.arcs.Contains(hostArc)) and (not location.nodes.Contains(hostArc.From)) and (not location.nodes.Contains(hostArc.To)) and (self.arcMatches(looseArc, hostArc) or self.arcMatchRelaxed(looseArc, hostArc, location)): #relaxelt
						newLocation = location.copy()
						newLocation.arcs[L.arcs.IndexOf(looseArc)] = hostArc
						self.findNewStartElement(newLocation)

	def checkNode(self, location, LNode, hostNode):
		if not self.nodeMatches(LNode, hostNode, location) and not self.nodeMatchRelaxed(LNode, hostNode, location):
			return 
		location.nodes[L.nodes.IndexOf(LNode)] = hostNode
		newLArc = LNode.arcs.Find()
		if newLArc == None:
			self.findNewStartElement(location)
		elif :
			self.checkHyperArc(location, LNode, hostNode, newLArc)
		elif :
			self.checkArc(location, LNode, hostNode, newLArc)

	def checkHyperArc(self, location, LHyperArc, hostHyperArc):
		if not self.hyperArcMatches(LHyperArc, hostHyperArc) and not self.hyperArcMatchRelaxed(LHyperArc, hostHyperArc, location):
			return 
		location.hyperarcs[L.hyperarcs.IndexOf(LHyperArc)] = hostHyperArc
		newLNode = LHyperArc.nodes.Find()
		if newLNode == None:
			self.findNewStartElement(location)
		else:
			enumerator = hostHyperArc.nodes.Where().GetEnumerator()
			while enumerator.MoveNext():
				n = enumerator.Current
				self.checkNode(location.copy(), newLNode, n)

	def checkHyperArc(self, location, fromLNode, fromHostNode, newLHyperArc):
		otherConnectedNodes = ().Cast()
		oCNNum = otherConnectedNodes.Count()
		hostHyperArcs = ().Cast()
		# at this stage hostHyperArcs are hyperarcs connected to fromHostNode, the same way that
		# * newLHyperArc is connected to fromLNode. However, this is not enough! What about nodes also
		# * connected to newLHyperArc that have already been recognized. We need to remove any instances
		# * from hostHyperArcs which don't connect to mappings of these already recognized nodes.
		enumerator = hostHyperArcs.GetEnumerator()
		while enumerator.MoveNext():
			hostHyperArc = enumerator.Current
			self.checkHyperArc(location.copy(), newLHyperArc, hostHyperArc)

	def checkArc(self, location, fromLNode, fromHostNode, newLArc):
		currentLArcIndex = L.arcs.IndexOf(newLArc)
		# so, currentLArcIndex now, points to a LArc that has yet to be recognized. What we do from
		# * this point depends on whether that LArc points to an L node we have yet to recognize, an L
		# * node we have recognized, or null.
		nextLNode = newLArc.otherNode(fromLNode)
		# first we must match the arc to a possible arc leaving the fromHostNode .
		nextHostNode = None if (nextLNode == None) else location.findLMappedNode(nextLNode)
		neighborHostArcs = fromHostNode.arcs.FindAll().Cast()
		#relaxelt
		if (nextHostNode != None) or newLArc.nullMeansNull:
			enumerator = neighborHostArcs.GetEnumerator()
			while enumerator.MoveNext():
				HostArc = enumerator.Current
				newLocation = location.copy()
				newLocation.arcs[currentLArcIndex] = HostArc
				self.findNewStartElement(newLocation)
		else:
			enumerator = neighborHostArcs.GetEnumerator()
			while enumerator.MoveNext():
				HostArc = enumerator.Current
				nextHostNode = HostArc.otherNode(fromHostNode)
				if not location.nodes.Contains(nextHostNode):
					newLocation = location.copy()
					newLocation.arcs[currentLArcIndex] = HostArc
					if nextLNode == None:
						self.findNewStartElement(newLocation)
					else:
						self.checkNode(newLocation, nextLNode, nextHostNode)

	def findRMappedElement(self, RMapping, GraphElementName):
		elt = R[GraphElementName]
		if :
			return RMapping.hyperarcs[R.hyperarcs.IndexOf(elt)]
		if :
			return RMapping.nodes[R.nodes.IndexOf(elt)]
		if :
			return RMapping.arcs[R.arcs.IndexOf(elt)]
		raise Exception("Graph element not found in rule's right-hand-side (GrammarRule.findMappedElement)")

	def findRMappedNode(self, location, n):
		return location.nodes[R.nodes.IndexOf(n)]

	def apply(self, host, Lmapping, parameters):
		""" <summary>
		   Applies the rule to the specified host.
		 </summary>
		 <param name = "host">The host.</param>
		 <param name = "Lmapping">The lmapping.</param>
		 <param name = "parameters">The parameters.</param>
		"""
		# First, update the global labels and variables.
		if OrderedGlobalLabels:
			self.updateOrderedGlobalLabels(Lmapping.globalLabelStartLoc, L.globalLabels, R.globalLabels, host.globalLabels)
		else:
			self.updateLabels(L.globalLabels, R.globalLabels, host.globalLabels)
		self.updateVariables(L.globalVariables, R.globalVariables, host.globalVariables)
		# Second set up the Rmapping, which is a list of nodes within the host
		# * that corresponds in length and position to the nodes in R, just as
		# * Lmapping contains lists of nodes and arcs in the order they are
		# * referred to in L.
		Rmapping = designGraph.CreateEmptyLocationGraph(R.nodes.Count, R.arcs.Count, R.hyperarcs.Count)
		self.removeLdiffKfromHost(Lmapping, host, )
		newElements = self.addRdiffKtoD(Lmapping, host, Rmapping, Lmapping.positionTransform)
		# these two lines correspond to the two "pushouts" of the double pushout algorithm.
		# *     L <--- K ---> R     this is from freeArc embedding (aka edNCE)
		# *     |      |      |        |      this is from the parametric update
		# *     |      |      |        |       |
		# *   host <-- D ---> H1 ---> H2 ---> H3
		# * The first step is to create D by removing the part of L not found in K (the commonality).
		# * Second, we add the elements of R not found in K to D to create the updated host, H. Note,
		# * that in order to do this, we must know what subgraph of the host we are manipulating - this
		# * is the location mapping found by the recognize function.
		newElements.AddRange(self.freeArcEmbedding(Lmapping, host, Rmapping, danglingNeighbors.Where().Cast()))
		newElements.AddRange(self.freeArcEmbedding(Lmapping, host, Rmapping, danglingNeighbors.Where().Cast()))
		# however, there may still be a need to embed the graph with other arcs left dangling,
		# * as in the "edge directed Node Controlled Embedding approach", which considers the neighbor-
		# * hood of nodes and arcs of the recognized Lmapping.
		self.updateAdditionalFunctions(Lmapping, host, Rmapping, parameters)
		enumerator = newElements.GetEnumerator()
		while enumerator.MoveNext():
			elt = enumerator.Current
			if  and host.nodes.Any():
				elt.name = host.makeUniqueNodeName(elt.name)
			elif  and host.arcs.Any():
				elt.name = host.makeUniqueArcName(elt.name)
			elif  and host.hyperarcs.Any():
				elt.name = host.makeUniqueHyperArcName(elt.name)

	def updateOrderedGlobalLabels(stringStart, LLabels, RLabels, hostLabels):
		hostLabels.RemoveRange(stringStart, LLabels.Count)
		hostLabels.InsertRange(stringStart, RLabels)

	updateOrderedGlobalLabels = staticmethod(updateOrderedGlobalLabels)

	def updateVariables(Lvariables, Rvariables, hostvariables):
		enumerator = Lvariables.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current # do the same now, for the variables.
			hostvariables.Remove(a) # removing the labels in L but not in R...
		hostvariables.AddRange(Rvariables)

	updateVariables = staticmethod(updateVariables)

	def updateLabels(Llabels, Rlabels, hostlabels):
		enumerator = Llabels.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			hostlabels.Remove(a)
		hostlabels.AddRange(Rlabels)

	updateLabels = staticmethod(updateLabels)

	def removeLdiffKfromHost(self, Lmapping, host, danglingNeighbors):
		# foreach node in L - see if it "is" also in R - if it is in R than it "is" part of the
		# * commonality subgraph K, and thus should not be deleted as it is part of the connectivity
		# * information for applying the rule. Note that what we mean by "is" is that there is a
		# * node with the same name. The name tag in a node is not superficial - it contains
		# * useful connectivity information. We use it as a stand in for referencing the same object
		# * this is different than the local lables which are used for recognition and the storage
		# * any important design information.
		danglingNeighbors = List[graphElement]()
		enumerator = L.nodes.Where().GetEnumerator()
		while enumerator.MoveNext():
			n = enumerator.Current
			nodeToRemove = Lmapping.findLMappedNode(n)
			danglingNeighbors = danglingNeighbors.Union(nodeToRemove.arcs).ToList()
			host.removeNode(nodeToRemove, False)
		# if a node with the same name does not exist in R, then it is safe to remove it.
		# * The removeNode should is invoked with the "false false" switches of this function.
		# * This causes the arcs to be unaffected by the deletion of a connecting node. Why
		# * do this? It is important in the edNCE approach that is appended to the DPO approach
		# * (see the function freeArcEmbedding) in connecting up a new R to the elements of L
		# * a node was connected to.
		# arcs and hyperarcs are removed in a similar way.
		enumerator = L.arcs.Where().GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			host.removeArc(Lmapping.findLMappedArc(a))
		enumerator = L.hyperarcs.Where().GetEnumerator()
		while enumerator.MoveNext():
			h = enumerator.Current
			host.removeHyperArc(Lmapping.findLMappedHyperarc(h))

	def addRdiffKtoD(self, Lmapping, D, Rmapping, positionT):
		newElements = List[graphElement]()
		# in this adding and gluing function, we are careful to distinguish
		# * the Lmapping or recognized subgraph of L in the host - heretofore
		# * known as Lmapping - from the mapping of new nodes and arcs of the
		# * graph, which we call Rmapping. This is a complex function that goes
		# * through 4 key steps:
		# * 1. add the new nodes that are in R but not in L.
		# * 2. update the remaining nodes common to L&R (aka K nodes) that might
		# *    have had some label changes.
		# * 3. add the new arcs that are in R but not in L. These may connect to
		# *    either the newly connected nodes from step 1 or from the updated nodes
		# *    of step 2. Also do this for the hyperarcs
		# * 4. update the arcs common to L&R (aka K arcs) which might now be connected
		# *    to new nodes created in step 1 (they are already connected to
		# *    nodes in K). Also make sure to update their labels just as K nodes were
		# *    updated in step 2.
		i = 0
		while i != R.nodes.Count:
			rNode = R.nodes[i]
			if not L.nodes.Exists():
				D.addNode(Type.GetType(rNode.TargetType, False)) # create a new node.
				Rmapping.nodes[i] = D.nodes.Last() # make sure it's referenced in Rmapping.
				# labels cannot be set equal, since that merely sets the reference of this list
				# * to the same value. So, we need to make a complete copy.
				rNode.copy(D.nodes.Last())
				# give that new node a name and labels to match with the R.
				newElements.Add(D.nodes.Last())
				# add the new node to the list of newElements that is returned by this function.
				self.TransformPositionOfNode(D.nodes.Last(), positionT, rNode)
				if TransformNodeShapes:
					self.TransfromShapeOfNode(D.nodes.Last(), positionT)
			else:
				# else, we may need to modify or update the node. In the pure graph
				# * grammar sense this is merely changing the local labels. In a way,
				# * this is a like a set grammar. We need to find the labels in L that
				# * are no longer in R and delete them, and we need to add the new labels
				# * that are in R but not already in L. The ones common to both are left
				# * alone.
				LNode = L.nodes.Find()
				# find index of the common node in L...
				KNode = Lmapping.findLMappedNode(LNode) # ...and then set Knode to the actual node in D.
				Rmapping.nodes[i] = KNode # also, make sure that the Rmapping is to this same node.
				self.updateLabels(LNode.localLabels, rNode.localLabels, KNode.localLabels)
				self.updateVariables(LNode.localVariables, rNode.localVariables, KNode.localVariables)
				if TransformNodePositions:
					self.TransformPositionOfNode(KNode, positionT, rNode)
				if TransformNodeShapes:
					KNode.DisplayShape = rNode.DisplayShape.Copy(KNode)
					self.TransfromShapeOfNode(KNode, positionT)
			i += 1
		# now moving onto the arcs (a little more challenging actually).
		i = 0
		while i != R.arcs.Count:
			rArc = R.arcs[i]
			if not L.arcs.Exists():
				if rArc.From == None:
					from = None
				elif L.nodes.Exists():
					# if the arc is coming from a node that is in K, then it must've been
					# * part of the location (or Lmapping) that was originally recognized.
					LNode = L.nodes.Find()
					# therefore we need to find the position/index of that node in L.
					from = Lmapping.findLMappedNode(LNode)
				else:
					# and that index1 will correspond to its image in Lmapping. Following,
					# * the Lmapping reference, we get to the proper node reference in D.
					# if not in K then the arc connects to one of the new nodes that were
					# * created at the beginning of this function (see step 1) and is now
					# * one of the references in Rmapping.
					RNode = R.nodes.Find()
					from = self.findRMappedNode(Rmapping, RNode)
				# this code is the same of "setting up where arc comes from - except here
				# * we do the same for the to connection of the arc.
				if rArc.To == None:
					to = None
				elif L.nodes.Exists():
					LNode = L.nodes.Find()
					to = Lmapping.findLMappedNode(LNode)
				else:
					RNode = R.nodes.Find()
					to = self.findRMappedNode(Rmapping, RNode)
				D.addArc(from, to, rArc.name, Type.GetType(rArc.TargetType, False))
				Rmapping.arcs[i] = D.arcs.Last()
				rArc.copy(D.arcs.Last())
				newElements.Add(D.arcs.Last())
			else:
				# add the new arc to the list of newElements that is returned by this function.
				# first find the position of the same arc in L.
				currentLArc = L.arcs.Find()
				mappedArc = Lmapping.findLMappedArc(currentLArc)
				# then find the actual arc in D that is to be changed.
				# one very subtle thing just happend here! (07/06/06) if the direction is reversed, then
				# * you might mess-up this Karc. We need to establish a boolean so that references
				# * incorrectly altered.
				KArcIsReversed = ((Lmapping.nodes.IndexOf(mappedArc.From) != L.nodes.IndexOf(currentLArc.From)) and (Lmapping.nodes.IndexOf(mappedArc.To) != L.nodes.IndexOf(currentLArc.To)))
				Rmapping.arcs[i] = mappedArc
				# similar to Step 3., we first find how to update the from and to.
				if (currentLArc.From != None) and (rArc.From == None):
					# this is a rare case in which you actually want to break an arc from its attached
					# * node. If the corresponding L arc is not null only! if it is null then it may be
					# * actually connected to something in the host, and we are in no place to remove it.
					if KArcIsReversed:
						mappedArc.To = None
					else:
						mappedArc.From = None
				elif rArc.From != None:
					RNode = R.nodes.Find()
					# find the position of node that this arc is supposed to connect to in R
					if KArcIsReversed:
						mappedArc.To = self.findRMappedNode(Rmapping, RNode)
					else:
						mappedArc.From = self.findRMappedNode(Rmapping, RNode)
				# now do the same for the To connection.
				if (currentLArc.To != None) and (rArc.To == None):
					if KArcIsReversed:
						mappedArc.From = None
					else:
						mappedArc.To = None
				elif rArc.To != None:
					RNode = R.nodes.Find()
					if KArcIsReversed:
						mappedArc.From = self.findRMappedNode(Rmapping, RNode)
					else:
						mappedArc.To = self.findRMappedNode(Rmapping, RNode)
				# just like in Step 2, we may need to update the labels of the arc.
				self.updateLabels(currentLArc.localLabels, rArc.localLabels, mappedArc.localLabels)
				self.updateVariables(currentLArc.localVariables, rArc.localVariables, mappedArc.localVariables)
				if not mappedArc.directed or (mappedArc.directed and currentLArc.directionIsEqual):
					mappedArc.directed = rArc.directed
				# if the KArc is currently undirected or if it is and direction is equal
				# * then the directed should be inherited from R.
				if not mappedArc.doublyDirected or (mappedArc.doublyDirected and currentLArc.directionIsEqual):
					mappedArc.doublyDirected = rArc.doublyDirected
				mappedArc.DisplayShape = rArc.DisplayShape.Copy(mappedArc)
			i += 1
		# finally, the hyperarcs .
		i = 0
		while i != R.hyperarcs.Count:
			rHyperarc = R.hyperarcs[i]
			lHyperarc = L.hyperarcs.FirstOrDefault()
			if lHyperarc == None:
				mappedNodes = rHyperarc.nodes.Select().Cast().ToList()
				D.addHyperArc(mappedNodes, rHyperarc.name, Type.GetType(rHyperarc.TargetType, False))
				Rmapping.hyperarcs[i] = D.hyperarcs.Last()
				rHyperarc.copy(D.hyperarcs.Last())
				newElements.Add(D.hyperarcs.Last())
			else:
				# add the new hyperarc to the list of newElements that is returned by this function.
				mappedHyperarc = Lmapping.findLMappedHyperarc(lHyperarc)
				intersectNodeNames = lHyperarc.nodes.Select()
				intersectNodeNames = intersectNodeNames.Intersect(rHyperarc.nodes.Select())
				enumerator = lHyperarc.nodes.Where().GetEnumerator()
				while enumerator.MoveNext():
					n = enumerator.Current
					mappedHyperarc.DisconnectFrom(Lmapping.findLMappedNode(n))
				enumerator = rHyperarc.nodes.Where().GetEnumerator()
				while enumerator.MoveNext():
					n = enumerator.Current
					mappedHyperarc.ConnectTo(self.findRMappedNode(Rmapping, n))
				Rmapping.hyperarcs[i] = mappedHyperarc
				# just like in Step 2 and 4, we may need to update the labels of the hyperarc.
				self.updateLabels(lHyperarc.localLabels, rHyperarc.localLabels, mappedHyperarc.localLabels)
				self.updateVariables(lHyperarc.localVariables, rHyperarc.localVariables, mappedHyperarc.localVariables)
				mappedHyperarc.DisplayShape = rHyperarc.DisplayShape.Copy(mappedHyperarc)
			i += 1
		return newElements

	def freeArcEmbedding(self, Lmapping, host, Rmapping, danglingNeighbors):
		newElements = List[graphElement]()
		enumerator = danglingNeighbors.GetEnumerator()
		while enumerator.MoveNext():
			dangleHyperArc = enumerator.Current
			if embeddingRule.hyperArcIsFree(dangleHyperArc, host, ):
				enumerator = embeddingRules.GetEnumerator()
				while enumerator.MoveNext():
					eRule = enumerator.Current
					newNodeToConnect = None if str.IsNullOrWhiteSpace(eRule.RNodeName) else self.findRMappedElement(Rmapping, eRule.RNodeName)
					nodeRemovedinLdiffRDeletion = None if str.IsNullOrWhiteSpace(eRule.LNodeName) else Lmapping.findLMappedElement(eRule.LNodeName)
					if eRule.ruleIsRecognized(dangleHyperArc, neighborNodes, nodeRemovedinLdiffRDeletion):
						if eRule.allowArcDuplication:
							newNeighborNodes = List[node](neighborNodes)
							newNeighborNodes.Add(newNodeToConnect)
							host.addHyperArc(dangleHyperArc.copy(), newNeighborNodes)
							newElements.Add(host.hyperarcs.Last())
						else:
							# add the new hyperarc to the list of newElements that is returned by this function.
							dangleHyperArc.ConnectTo(newNodeToConnect)
							break
		enumerator = danglingNeighbors.GetEnumerator()
		while enumerator.MoveNext():
			dangleArc = enumerator.Current
			dangleArc.nodes.RemoveAll()
			if dangleArc.nodes.Count == 0:
				host.removeHyperArc(dangleArc)
		return newElements

	def freeArcEmbedding(self, Lmapping, host, Rmapping, danglingNeighbors):
		# There are nodes in host which may have been left dangling due to the fact that their
		# * connected nodes were part of the L-R deletion. These now need to be either 1) connected
		# * up to their new nodes, 2) their references to old nodes need to be changed to null if
		# * intentionally left dangling, or 3) the arcs are to be removed. In the function
		# * removeLdiffKfromHost we remove old nodes but leave their references intact on their
		# * connected arcs. This allows us to find the list of freeArcs that are candidates
		# * for the embedding rules. Essentially, we are capturing the neighborhood within the host
		# * for the rule application, that is the arcs that are affected by the deletion of the L-R
		# * subgraph. Should one check non-dangling non-neighborhood arcs? No, this would seem to
		# * cause a duplication of such an arc. Additionally, what node in host should the arc remain
		# * attached to?  There seems to be no rigor in applying these more global (non-neighborhood)
		# * changes within the literature as well for the general edNCE method.
		newElements = List[graphElement]()
		enumerator = danglingNeighbors.GetEnumerator()
		while enumerator.MoveNext():
			dangleArc = enumerator.Current
			if embeddingRule.arcIsFree(dangleArc, host, , ): # For each of the embedding rules, we see if it is applicable to the identified freeArc.
				# * The rule then modifies the arc by simply pointing it to the new node in R as indicated
				# * by the embedding Rule's RNodeName. NOTE: the order of the rules are important. If two
				# * rules are 'recognized' with the same freeArc only the first one will modify it, as it
				# * will then remove it from the freeArc list. This is useful in that rules may have precedence
				# * to one another. There is an exception if the rule has allowArcDuplication set to true,
				# * since this would simply create a copy of the arc.
				enumerator = embeddingRules.GetEnumerator()
				while enumerator.MoveNext():
					eRule = enumerator.Current
					newNodeToConnect = None if str.IsNullOrWhiteSpace(eRule.RNodeName) else self.findRMappedElement(Rmapping, eRule.RNodeName)
					nodeRemovedinLdiffRDeletion = None if str.IsNullOrWhiteSpace(eRule.LNodeName) else Lmapping.findLMappedElement(eRule.LNodeName)
					if eRule.ruleIsRecognized(freeEndIdentifier, dangleArc, neighborNode, nodeRemovedinLdiffRDeletion):
						if freeEndIdentifier >= 0:
							if eRule.newDirection >= 0:
								toNode = newNodeToConnect
								fromNode = dangleArc.From
							else:
								toNode = dangleArc.From
								fromNode = newNodeToConnect
						else:
							if eRule.newDirection <= 0:
								fromNode = newNodeToConnect
								toNode = dangleArc.To
							else:
								fromNode = dangleArc.To
								toNode = newNodeToConnect
						if eRule.allowArcDuplication:
							# under the allowArcDuplication section, we will be making a copy of the
							# * freeArc. This seems a little error-prone at first, since if there is only
							# * one rule that applies to freeArc then we will have good copy and the old
							# * bad copy. However, at the end of this function, we go through the arcs again
							# * and remove any arcs that still appear free. This also serves the purpose to
							# * delete any dangling nodes that were not recognized in any rules.
							host.addArc(dangleArc.copy(), fromNode, toNode)
							newElements.Add(host.arcs.Last())
						else:
							# add the new arc to the list of newElements that is returned by this function.
							dangleArc.From = fromNode
							dangleArc.To = toNode
							break # skip to the next arc
		# this is done so that no more embedding rules will be checked with this freeArc.
		enumerator = danglingNeighbors.Where().GetEnumerator()
		while enumerator.MoveNext():
			dangleArc = enumerator.Current
			host.removeArc(dangleArc)
		return newElements

	def updateAdditionalFunctions(self, Lmapping, host, Rmapping, parameters):
		""" <summary>
		   The final update step is to invoke additional functions for the rule. 
		   These are traditionally called the Parametric Application Functions, but
		   they can do any custom modifications to the host.
		 </summary>
		 <param name = "Lmapping">The lmapping.</param>
		 <param name = "host">The host.</param>
		 <param name = "Rmapping">The rmapping.</param>
		 <param name = "parameters">The parameters.</param>
		"""
		# If you get an error in this function, it is most likely due to
		# * an error in the compilted DLLofFunctions. Open your code for the
		# * rules and leave this untouched - it's simply the messenger.
		enumerator = applyFuncs.GetEnumerator()
		while enumerator.MoveNext():
			applyFunction = enumerator.Current
			try:
				if applyFunction.GetParameters().GetLength(0) == 2:
					applyArguments = Array[Object]((Lmapping, host))
				elif applyFunction.GetParameters().GetLength(0) == 3:
					applyArguments = Array[Object]((Lmapping, host, Rmapping))
				elif applyFunction.GetParameters().GetLength(0) == 4:
					applyArguments = Array[Object]((Lmapping, host, Rmapping, parameters))
				else:
					applyArguments = Array[Object]((Lmapping, host, Rmapping, parameters, self))
				applyFunction.Invoke(DLLofFunctions, applyArguments)
			except Exception, e:
				SearchIO.MessageBoxShow("Error in additional apply function: " + applyFunction.Name + ".\nSee output bar for details.", "Error in  " + applyFunction.Name, "Error")
				SearchIO.output("Error in function: " + applyFunction.Name)
				#+ "\n" +ErrorLogger.MakeErrorString(e, false));
				SearchIO.output("Exception in : " + e.InnerException.TargetSite.Name)
				SearchIO.output("Error              : " + e.InnerException.Message)
				SearchIO.output("Stack Trace     	: " + e.InnerException.StackTrace)
			finally: