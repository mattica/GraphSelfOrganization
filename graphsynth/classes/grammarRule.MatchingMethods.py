import clr

				import clr

				import clr

				import clr

				import clr

				import clr

# ************************************************************************
# *     This grammarRule.Basic.cs file partially defines the grammarRule
# *     class (also partially defined in grammarRule.ShapeMethods.cs,
# *     grammarRule.RecognizeApply.cs and grammarRule.NegativeRecognize.cs)
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
from System.Collections.Generic import *
from System.Globalization import *
from System.Linq import *

class grammarRule(object):
	""" <summary>
	 All of these functions are static Booleans functions that match the graph or graph elements between host and rule.
	 </summary>
	"""
	def IntendedTypesMatch(TargetType, hostElt):
		if str.IsNullOrWhiteSpace(TargetType) or Type.GetType(TargetType) == None:
			return True
		t = Type.GetType(TargetType)
		return (hostElt.GetType().IsInstanceOfType(t))

	IntendedTypesMatch = staticmethod(IntendedTypesMatch)

	def LabelsMatch(hostLabels, positiveLabels, negateLabels, containsAllLocalLabels):
		# first an easy check to see if any negating labels exist
		# * in the hostLabels. If so, immediately return false.
		if negateLabels.Any() and negateLabels.Intersect(hostLabels).Any():
			return False
		# next, set up a tempLabels so that we don't change the
		# * host's actual labels. We delete an instance of the label.
		# * this is new in version 1.8. It's important since one may
		# * have multiple identical labels.
		tempLabels = List[str](hostLabels)
		enumerator = positiveLabels.GetEnumerator()
		while enumerator.MoveNext():
			label = enumerator.Current
			if tempLabels.Contains(label):
				tempLabels.Remove(label)
			else:
				return False
		# this new approach actually simplifies and speeds up the containAllLabels
		# * check. If there are no more tempLabels than the two match completely - else
		# * return false.
		if containsAllLocalLabels and tempLabels.Any():
			return False
		return True

	LabelsMatch = staticmethod(LabelsMatch)

	def nodeMatches(self, LNode, hostNode, location):
		return (not LNode.strictDegreeMatch or LNode.degree == hostNode.degree) and LNode.degree <= hostNode.degree and self.LabelsMatch(hostNode.localLabels, LNode.localLabels, LNode.negateLabels, LNode.containsAllLocalLabels) and self.IntendedTypesMatch(LNode.TargetType, hostNode) and self.HyperArcPreclusionCheckForSingleNode(LNode, hostNode, location.hyperarcs)

	def nodeMatchRelaxed(self, LNode, hostNode, location):
		if location.Relaxations.NumberAllowable == 0:
			return False
		localNumAllowable = location.Relaxations.NumberAllowable
		usedRelaxItems = List[RelaxItem]()
		usedFulfilledRelaxItems = List[RelaxItem]()
		if LNode.strictDegreeMatch and LNode.degree != hostNode.degree:
			rStrictDegree = location.Relaxations.FirstOrDefault()
			if rStrictDegree == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rStrictDegree)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Strict_Degree_Match_Revoked, 1, LNode, hostNode.degree.ToString(CultureInfo.InvariantCulture)))
		if not self.IntendedTypesMatch(LNode.TargetType, hostNode):
			rType = location.Relaxations.FirstOrDefault()
			if rType == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rType)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Target_Type_Revoked, 1, LNode, hostNode.GetType().ToString()))
		if not self.HyperArcPreclusionCheckForSingleNode(LNode, hostNode, location.hyperarcs):
			rHyperArcPreclusion = location.Relaxations.FirstOrDefault()
			if rHyperArcPreclusion == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rHyperArcPreclusion)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.HyperArc_Preclusion_Revoked, 1, LNode))
		enumerator = LNode.negateLabels.GetEnumerator()
		while enumerator.MoveNext():
			nl = enumerator.Current
			if hostNode.localLabels.Contains(nl):
				rNegLabel = location.Relaxations.FirstOrDefault()
				if rNegLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rNegLabel)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Negate_Label_Revoked, 1, LNode, nl))
		tempLabels = List[str](hostNode.localLabels)
		enumerator = LNode.localLabels.GetEnumerator()
		while enumerator.MoveNext():
			label = enumerator.Current
			if tempLabels.Contains(label):
				tempLabels.Remove(label)
			else:
				rLabel = location.Relaxations.FirstOrDefault()
				if rLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rLabel)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Label_Revoked, 1, LNode, label))
				tempLabels.Remove(label)
		if LNode.containsAllLocalLabels and tempLabels.Any():
			rContainsAll = location.Relaxations.FirstOrDefault()
			if rContainsAll == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rContainsAll)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Contains_All_Local_Labels_Revoked, 1, LNode, hostNode.localLabels.Count.ToString(CultureInfo.InvariantCulture)))
		if localNumAllowable < 0:
			return False # don't make any reductions to the relaxations list - there are not
		# * enough to make this work.
		location.Relaxations.NumberAllowable = localNumAllowable
		enumerator = usedRelaxItems.GetEnumerator()
		while enumerator.MoveNext():
			r = enumerator.Current
			r.NumberAllowed -= 1
		location.Relaxations.FulfilledItems.AddRange(usedFulfilledRelaxItems)
		return True

	#private node nodeRelaxExistence(option location, ruleNode LNode)
	#{
	#    if (location.Relaxations.NumberAllowable == 0) return null;
	#    var rEltRemove = location.Relaxations.FirstOrDefault(r =>
	#        r.Matches(Relaxations.Element_Made_Negative, LNode) && r.NumberAllowed > 0);
	#    if (rEltRemove == null) return null;
	#    location.Relaxations.NumberAllowable--;
	#    location.Relaxations.FulfilledItems.Add(new RelaxItem(Relaxations.Element_Made_Negative, 1, LNode));
	#    node standinNode;
	#    Type nodeType = Type.GetType(LNode.TargetType, false);
	#    if (nodeType == null || nodeType == typeof(node))
	#        standinNode = new node();
	#    else
	#    {
	#        var nodeConstructor = nodeType.GetConstructor(new Type[0]);
	#        if (nodeConstructor == null)
	#            standinNode = new node();
	#        else standinNode = (node)nodeConstructor.Invoke(new object[0]);
	#    }
	#    LNode.copy(standinNode);
	#    return standinNode;
	#}
	def hyperArcMatches(Lha, Hha):
		if Lha.strictNodeCountMatch and (Lha.degree != Hha.degree):
			return False
		if Lha.degree > Hha.degree:
			return False
		return (grammarRule.LabelsMatch(Hha.localLabels, Lha.localLabels, Lha.negateLabels, Lha.containsAllLocalLabels) and grammarRule.IntendedTypesMatch(Lha.TargetType, Hha))

	hyperArcMatches = staticmethod(hyperArcMatches)

	def hyperArcMatchRelaxed(Lha, Hha, location):
		if location.Relaxations.NumberAllowable == 0:
			return False
		localNumAllowable = location.Relaxations.NumberAllowable
		usedRelaxItems = List[RelaxItem]()
		usedFulfilledRelaxItems = List[RelaxItem]()
		if Lha.strictNodeCountMatch and Lha.degree != Hha.degree:
			rStrictNodeCount = location.Relaxations.FirstOrDefault()
			if rStrictNodeCount == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rStrictNodeCount)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Strict_Node_Count_Revoked, 1, Lha, Hha.degree.ToString(CultureInfo.InvariantCulture)))
		if not grammarRule.IntendedTypesMatch(Lha.TargetType, Hha):
			rType = location.Relaxations.FirstOrDefault()
			if rType == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rType)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Target_Type_Revoked, 1, Lha, Hha.GetType().ToString()))
		enumerator = Lha.negateLabels.GetEnumerator()
		while enumerator.MoveNext():
			nl = enumerator.Current
			if Hha.localLabels.Contains(nl):
				rNegLabel = location.Relaxations.FirstOrDefault()
				if rNegLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rNegLabel)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Negate_Label_Revoked, 1, Lha, nl))
		tempLabels = List[str](Hha.localLabels)
		enumerator = Lha.localLabels.GetEnumerator()
		while enumerator.MoveNext():
			label = enumerator.Current
			if tempLabels.Contains(label):
				tempLabels.Remove(label)
			else:
				rLabel = location.Relaxations.FirstOrDefault()
				if rLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rLabel)
				tempLabels.Remove(label)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Label_Revoked, 1, Lha, label))
		if Lha.containsAllLocalLabels and tempLabels.Any():
			rContainsAll = location.Relaxations.FirstOrDefault()
			if rContainsAll == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rContainsAll)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Contains_All_Local_Labels_Revoked, 1, Lha, Hha.localLabels.Count.ToString(CultureInfo.InvariantCulture)))
		if localNumAllowable < 0:
			return False # don't make any reductions to the relaxations list - there are not
		# * enough to make this work.
		location.Relaxations.NumberAllowable = localNumAllowable
		enumerator = usedRelaxItems.GetEnumerator()
		while enumerator.MoveNext():
			r = enumerator.Current
			r.NumberAllowed -= 1
		location.Relaxations.FulfilledItems.AddRange(usedFulfilledRelaxItems)
		return True

	hyperArcMatchRelaxed = staticmethod(hyperArcMatchRelaxed)

	#private hyperarc hyperarcRelaxExistence(option location, ruleHyperarc LHyper)
	#{
	#    if (location.Relaxations.NumberAllowable == 0) return null;
	#    var rEltRemove = location.Relaxations.FirstOrDefault(r =>
	#        r.Matches(Relaxations.Element_Made_Negative, LHyper) && r.NumberAllowed > 0);
	#    if (rEltRemove == null) return null;
	#    location.Relaxations.NumberAllowable--;
	#    location.Relaxations.FulfilledItems.Add(new RelaxItem(Relaxations.Element_Made_Negative, 1, LHyper));
	#    hyperarc standinNode;
	#    Type hyperarcType = Type.GetType(LHyper.TargetType, false);
	#    if (hyperarcType == null || hyperarcType == typeof(hyperarc))
	#        standinNode = new hyperarc();
	#    else
	#    {
	#        var nodeConstructor = hyperarcType.GetConstructor(new Type[0]);
	#        if (nodeConstructor == null)
	#            standinNode = new hyperarc();
	#        else standinNode = (hyperarc)nodeConstructor.Invoke(new object[0]);
	#    }
	#    LHyper.copy(standinNode);
	#    return standinNode;
	#}
	def arcMatches(LArc, hostArc, fromHostNode, nextHostNode, LTraversesForward):
		""" <summary>
		 Returns a true/false based on if the host arc matches with this ruleArc.
		 </summary>
		 <param name="LArc">The L arc.</param>
		 <param name="hostArc">The host arc.</param>
		 <param name="fromHostNode">From host node.</param>
		 <param name="nextHostNode">The next host node.</param>
		 <param name="LTraversesForward">if set to <c>true</c> [traverse forward].</param>
		 <returns></returns>
		"""
		if (nextHostNode != None or LArc.nullMeansNull) and hostArc.otherNode(fromHostNode) != nextHostNode:
			return False
		hostTraversesForward = (hostArc.From != None) and (hostArc.From == fromHostNode)
		if LArc.directionIsEqual and (LArc.doublyDirected != hostArc.doublyDirected):
			return False
		if LArc.directionIsEqual and (LArc.directed != hostArc.directed):
			return False
		if LArc.directed and not hostArc.directed:
			return False
		if LArc.doublyDirected and not hostArc.doublyDirected:
			return False # if this rule arc is directed
		if LArc.directed and (hostTraversesForward != LTraversesForward):
			return False
		return (grammarRule.LabelsMatch(hostArc.localLabels, LArc.localLabels, LArc.negateLabels, LArc.containsAllLocalLabels) and grammarRule.IntendedTypesMatch(LArc.TargetType, hostArc))

	arcMatches = staticmethod(arcMatches)

	def arcMatchRelaxed(LArc, hostArc, location, fromHostNode, nextHostNode, LTraversesForward):
		if location.Relaxations.NumberAllowable == 0:
			return False
		localNumAllowable = location.Relaxations.NumberAllowable
		usedRelaxItems = List[RelaxItem]()
		usedFulfilledRelaxItems = List[RelaxItem]()
		if (nextHostNode != None) and hostArc.otherNode(fromHostNode) != nextHostNode:
			return False
		#relaxelt although we could look to make nextHostNode NOTEXIST(?)
		if LArc.nullMeansNull and hostArc.otherNode(fromHostNode) != None:
			rNullMeansNull = location.Relaxations.FirstOrDefault()
			if rNullMeansNull == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rNullMeansNull)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Null_Means_Null_Revoked, 1, LArc, nextHostNode.name if (nextHostNode != None) else ""))
		hostTraversesForward = (hostArc.From != None) and (hostArc.From == fromHostNode)
		if (LArc.directionIsEqual and (LArc.doublyDirected != hostArc.doublyDirected)) or (LArc.directionIsEqual and (LArc.directed != hostArc.directed)) or (LArc.directed and not hostArc.directed) or (LArc.doublyDirected and not hostArc.doublyDirected) or (LArc.directed and (hostTraversesForward != LTraversesForward)):
			rDir = location.Relaxations.FirstOrDefault()
			if rDir == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rDir)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Direction_Is_Equal_Revoked, 1, LArc, hostArc.name))
		if not grammarRule.IntendedTypesMatch(LArc.TargetType, hostArc):
			rType = location.Relaxations.FirstOrDefault()
			if rType == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rType)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Target_Type_Revoked, 1, LArc, hostArc.GetType().ToString()))
		enumerator = LArc.negateLabels.GetEnumerator()
		while enumerator.MoveNext():
			nl = enumerator.Current
			if hostArc.localLabels.Contains(nl):
				rNegLabel = location.Relaxations.FirstOrDefault()
				if rNegLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rNegLabel)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Negate_Label_Revoked, 1, LArc, nl))
		tempLabels = List[str](hostArc.localLabels)
		enumerator = LArc.localLabels.GetEnumerator()
		while enumerator.MoveNext():
			label = enumerator.Current
			if tempLabels.Contains(label):
				tempLabels.Remove(label)
			else:
				rLabel = location.Relaxations.FirstOrDefault()
				if rLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rLabel)
				tempLabels.Remove(label)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Label_Revoked, 1, LArc, label))
		if LArc.containsAllLocalLabels and tempLabels.Any():
			rContainsAll = location.Relaxations.FirstOrDefault()
			if rContainsAll == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rContainsAll)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Contains_All_Local_Labels_Revoked, 1, LArc, hostArc.localLabels.Count.ToString(CultureInfo.InvariantCulture)))
		if localNumAllowable < 0:
			return False # don't make any reductions to the relaxations list - there are not
		# * enough to make this work.
		location.Relaxations.NumberAllowable = localNumAllowable
		enumerator = usedRelaxItems.GetEnumerator()
		while enumerator.MoveNext():
			r = enumerator.Current
			r.NumberAllowed -= 1
		location.Relaxations.FulfilledItems.AddRange(usedFulfilledRelaxItems)
		return True

	arcMatchRelaxed = staticmethod(arcMatchRelaxed)

	def InitialRuleCheck(self):
		return (not spanning or (L.nodes.Count == _host.nodes.Count)) and ((OrderedGlobalLabels and self.OrderLabelsMatch(_host.globalLabels)) or (not OrderedGlobalLabels and self.LabelsMatch(_host.globalLabels, L.globalLabels, negateLabels, containsAllGlobalLabels))) and self.hasLargerOrEqualDegreeSeqence(_host.DegreeSequence, LDegreeSequence) and self.hasLargerOrEqualDegreeSeqence(_host.HyperArcDegreeSequence, LHyperArcDegreeSequence) and (_host.arcs.Count >= L.arcs.Count)

	def InitialRuleCheckRelaxed(self, location):
		if location.Relaxations.NumberAllowable == 0:
			return False
		localNumAllowable = location.Relaxations.NumberAllowable
		usedRelaxItems = List[RelaxItem]()
		usedFulfilledRelaxItems = List[RelaxItem]()
		if spanning and (L.nodes.Count != _host.nodes.Count):
			rSpanning = location.Relaxations.FirstOrDefault()
			if rSpanning == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rSpanning)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Spanning_Revoked, 1, None, _host.nodes.Count.ToString(CultureInfo.InvariantCulture)))
		enumerator = negateLabels.GetEnumerator()
		while enumerator.MoveNext():
			nl = enumerator.Current
			if _host.globalLabels.Contains(nl):
				rNegLabel = location.Relaxations.FirstOrDefault()
				if rNegLabel == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rNegLabel)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Negate_Global_Label_Revoked, 1, None, nl))
		if not OrderedGlobalLabels or not self.OrderLabelsMatch(_host.globalLabels):
			tempLabels = List[str](_host.globalLabels)
			enumerator = L.globalLabels.GetEnumerator()
			while enumerator.MoveNext():
				label = enumerator.Current
				if tempLabels.Contains(label):
					tempLabels.Remove(label)
				else:
					rLabel = location.Relaxations.FirstOrDefault()
					if rLabel == None:
						return False
					localNumAllowable -= 1
					usedRelaxItems.Add(rLabel)
					usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Global_Label_Revoked, 1, None, label))
					tempLabels.Remove(label)
			if OrderedGlobalLabels:
				rOrdered = location.Relaxations.FirstOrDefault()
				if rOrdered == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rOrdered)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Ordered_Global_Labels_Revoked, 1))
			if containsAllGlobalLabels and tempLabels.Any():
				rContainsAll = location.Relaxations.FirstOrDefault()
				if rContainsAll == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rContainsAll)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Contains_All_Local_Labels_Revoked, 1, None, _host.globalLabels.Count.ToString(CultureInfo.InvariantCulture)))
		if localNumAllowable < 0:
			return False
		# don't make any reductions to the relaxations list - there are not
		# * enough to make this work.
		location.Relaxations.NumberAllowable = localNumAllowable
		enumerator = usedRelaxItems.GetEnumerator()
		while enumerator.MoveNext():
			r = enumerator.Current
			r.NumberAllowed -= 1
		location.Relaxations.FulfilledItems.AddRange(usedFulfilledRelaxItems)
		return True

	def OrderLabelsMatch(self, hostLabels):
		# first an easy check to see if any negating labels exist
		# * in the hostLabels. If so, immediately return false.
		if negateLabels.Any() and negateLabels.Intersect(hostLabels).Any():
			return False
		if containsAllGlobalLabels:
			if hostLabels.SequenceEqual(L.globalLabels):
				globalLabelStartLocs.Add(0)
				return True
			return False
		AnyFound = False
		i = 0
		while i < hostLabels.Count - L.globalLabels.Count + 1:
			subList = Array.CreateInstance(str, L.globalLabels.Count)
			Array.Copy(hostLabels.ToArray(), i, subList, 0, L.globalLabels.Count)
			if L.globalLabels.SequenceEqual(subList):
				globalLabelStartLocs.Add(i)
				AnyFound = True
			i += 1
		return AnyFound

	def hasLargerOrEqualDegreeSeqence(ASequence, BSequence):
		""" <summary>
		 Determines whether A has larger or equal degree seqence to B.
		 </summary>
		 <param name="ASequence">The A sequence.</param>
		 <param name="BSequence">The B sequence.</param>
		 <returns>
		   <c>true</c> if  A [has larger or equal degree seqence] [the specified B sequence]; otherwise, <c>false</c>.
		 </returns>
		"""
		if BSequence.Count > ASequence.Count:
			return False
		return not BSequence.Where().Any()

	hasLargerOrEqualDegreeSeqence = staticmethod(hasLargerOrEqualDegreeSeqence)

	def FinalRuleChecks(self, location):
		if L.nodes.Where().Any():
			return False # not a valid option
		# a complete subgraph has been found. However, there is three more conditions to check:
		# * induced, shape transform, and additional recognize functions written as C# code
		if induced and self.otherArcsInHost(_host, location):
			return False # not a valid option
		# The induced boolean indicates that if there are any arcs in the host between the
		# * nodes of the subgraph that are not in L then this is not a valid location.
		firstNotExistIndex = L.nodes.FindIndex()
		if firstNotExistIndex < 0:
			T = self.findTransform(location.nodes)
		else:
			positiveNodes = List[node](location.nodes)
			positiveNodes.RemoveRange(firstNotExistIndex, (positiveNodes.Count - firstNotExistIndex))
			T = self.findTransform(positiveNodes)
		if UseShapeRestrictions and (not self.validTransform(T) or not self.otherNodesComply(T, location.nodes)):
			return False # not a valid option
		# the transform does not have a correct transformation
		enumerator = recognizeFuncs.GetEnumerator()
		while enumerator.MoveNext():
			recognizeFunction = enumerator.Current
			try:
				# newest approach #6
				if recognizeFunction.GetParameters().GetLength(0) == 2:
					recognizeArguments = Array[Object]((location, _host))
				elif 				# oldest approach #1
recognizeFunction.GetParameters()[0].ParameterType == clr.GetClrType(designGraph):
					recognizeArguments = Array[Object]((L, _host, location.nodes, location.arcs))
				elif 				# newer approach #5
(recognizeFunction.GetParameters().GetLength(0) == 3) and (recognizeFunction.GetParameters()[2].ParameterType == clr.GetClrType(option)):
					recognizeArguments = Array[Object]((self, _host, location))
				elif 				# new approach #4
(recognizeFunction.GetParameters().GetLength(0) == 4) and (recognizeFunction.GetParameters()[2].ParameterType == clr.GetClrType(designGraph)):
					recognizeArguments = Array[Object]((self, _host, designGraph(location.nodes, location.arcs, location.hyperarcs), T))
				elif 				# older approach #2
recognizeFunction.GetParameters().GetLength(0) == 4:
					recognizeArguments = Array[Object]((self, _host, location.nodes, location.arcs))
				else:
					#  approach #3
					recognizeArguments = Array[Object]((self, _host, location.nodes, location.arcs, T))
				if recognizeFunction.Invoke(DLLofFunctions, recognizeArguments) > 0:
					return False
			except Exception, e:
				SearchIO.MessageBoxShow("Error in additional recognize function: " + recognizeFunction.Name + ".\nSee output bar for details.", "Error in  " + recognizeFunction.Name, "Error")
				SearchIO.output("Error in function: " + recognizeFunction.Name)
				SearchIO.output("Exception in : " + e.InnerException.TargetSite.Name)
				SearchIO.output("Error              : " + e.InnerException.Message)
				SearchIO.output("Stack Trace     	: " + e.InnerException.StackTrace)
				return False
			finally:
		location.positionTransform = T
		return True

	def FinalRuleCheckRelaxed(self, location):
		if location.Relaxations.NumberAllowable == 0:
			return False
		localNumAllowable = location.Relaxations.NumberAllowable
		usedRelaxItems = List[RelaxItem]()
		usedFulfilledRelaxItems = List[RelaxItem]()
		if induced and self.otherArcsInHost(_host, location):
			rInduced = location.Relaxations.FirstOrDefault()
			if rInduced == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rInduced)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Induced_Revoked, 1))
		numNodes = L.nodes.Count
		i = 0
		while i < numNodes:
			if location.nodes[i] != None and not self.HyperArcPreclusionCheckForSingleNode(L.nodes[i], location.nodes[i], location.hyperarcs):
				rHyperArcPreclusion = location.Relaxations.FirstOrDefault()
				if rHyperArcPreclusion == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rHyperArcPreclusion)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.HyperArc_Preclusion_Revoked, 1, location.nodes[i]))
			i += 1
		firstNotExistIndex = L.nodes.FindIndex()
		if firstNotExistIndex < 0:
			T = self.findTransform(location.nodes)
		else:
			positiveNodes = List[node](location.nodes)
			positiveNodes.RemoveRange(firstNotExistIndex, (positiveNodes.Count - firstNotExistIndex))
			T = self.findTransform(positiveNodes)
		if UseShapeRestrictions and (not self.validTransform(T) or not self.otherNodesComply(T, location.nodes)):
			rShape = location.Relaxations.FirstOrDefault()
			if rShape == None:
				return False
			localNumAllowable -= 1
			usedRelaxItems.Add(rShape)
			usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Shape_Restriction_Revoked, 1))
		enumerator = recognizeFuncs.GetEnumerator()
		while enumerator.MoveNext():
			recognizeFunction = enumerator.Current
			try:
				# oldest approach: 1
				if recognizeFunction.GetParameters()[0].ParameterType == clr.GetClrType(designGraph):
					recognizeArguments = Array[Object]((L, _host, location.nodes, location.arcs))
				elif 				# newest approach: 5
(recognizeFunction.GetParameters().GetLength(0) == 3) and (recognizeFunction.GetParameters()[2].ParameterType == clr.GetClrType(option)):
					recognizeArguments = Array[Object]((self, _host, location))
				elif 				# newer approach: 4
(recognizeFunction.GetParameters().GetLength(0) == 4) and (recognizeFunction.GetParameters()[2].ParameterType == clr.GetClrType(designGraph)):
					recognizeArguments = Array[Object]((self, _host, designGraph(location.nodes, location.arcs, location.hyperarcs), T))
				elif 				# older approach: 2
recognizeFunction.GetParameters().GetLength(0) == 4:
					recognizeArguments = Array[Object]((self, _host, location.nodes, location.arcs))
				else:
					# new approach:3
					recognizeArguments = Array[Object]((self, _host, location.nodes, location.arcs, T))
				gValue = recognizeFunction.Invoke(DLLofFunctions, recognizeArguments)
				if gValue > 0:
					rAddnlFunction = location.Relaxations.FirstOrDefault()
					if rAddnlFunction == None:
						return False
					localNumAllowable -= 1
					usedRelaxItems.Add(rAddnlFunction)
					usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Additional_Functions_Revoked, 1, None, recognizeFunction.Name + " = " + gValue))
			except Exception, e:
				SearchIO.MessageBoxShow("Error in additional recognize function: " + recognizeFunction.Name + ".\nSee output bar for details.", "Error in  " + recognizeFunction.Name, "Error")
				SearchIO.output("Error in function: " + recognizeFunction.Name)
				SearchIO.output("Exception in : " + e.InnerException.TargetSite.Name)
				SearchIO.output("Error              : " + e.InnerException.Message)
				SearchIO.output("Stack Trace     	: " + e.InnerException.StackTrace)
				rAddnlFunction = location.Relaxations.FirstOrDefault()
				if rAddnlFunction == None:
					return False
				localNumAllowable -= 1
				usedRelaxItems.Add(rAddnlFunction)
				usedFulfilledRelaxItems.Add(RelaxItem(Relaxations.Additional_Functions_Revoked, 1, None, recognizeFunction.Name + " = Error: " + e.InnerException.Message))
			finally:
		if localNumAllowable < 0:
			return False # don't make any reductions to the relaxations list - there are not
		# * enough to make this work.
		location.Relaxations.NumberAllowable = localNumAllowable
		enumerator = usedRelaxItems.GetEnumerator()
		while enumerator.MoveNext():
			r = enumerator.Current
			r.NumberAllowed -= 1
		location.Relaxations.FulfilledItems.AddRange(usedFulfilledRelaxItems)
		location.positionTransform = T
		return True

	def otherArcsInHost(host, location):
		""" <summary>
		 This function is used when checking for an induced subgraph (near line 300 of this file under
		 the function case1LocationFound). I have placed it here near the induced property because that's
		 a logical place as any in such a big file.
		 </summary>
		 <param name="host">The host graph.</param>
		 <param name="location">The location.</param>
		 <returns>
		 true - if no other arcs exist between the locatedNodes.
		 </returns>
		"""
		# Check each arc of the host. If an arc is NOT in located Nodes but connects two located
		# * nodes then return false.
		if host.arcs.Any():
			return True
		return host.hyperarcs.Any()

	otherArcsInHost = staticmethod(otherArcsInHost)

	def HyperArcPreclusionCheckForSingleNode(self, LNode, hostNode, hostHyperarcs):
		""" <summary>
		 Hyperarc preclusion check for single node. Actually also "inclusion" check. Checks that host has
		 nodes connected in the same way to the hyperarcs as they are in the rule's LHS.
		 </summary>
		 <param name="LNode">The L node.</param>
		 <param name="hostNode">The host node.</param>
		 <param name="hostHyperarcs">The host hyperarcs.</param>
		 <returns>
		 true if preclusions are correct for this node (it is not included
		 in hyperarcs it was intentionally precluded from.
		 </returns>
		"""
		# after two other versions - which were correct but hard to follow - I settled on this one, which is both
		# * the easiest to understand and the fastest (for loop finds both hyperarcs without extra lookup function.
		i = 0
		while i < L.hyperarcs.Count:
			ruleHyperarc = L.hyperarcs[i]
			hostHyperarc = hostHyperarcs[i]
			if hostHyperarc != None and _host.hyperarcs.Contains(hostHyperarc) and 			# since this function is called before the end (as an early check on nodes
			# * in nodeMatches) it's possible that there are yet-to-be-found hyperarcs,
			# * which we need to skip at this point, or the hostHyperarc was a "stand-in" if
			# * the problem was relaxed s.t. the hyperarc doesn't really exist in the host.
(LNode.NotExist or not ruleHyperarc.NotExist) and 			# this one is tricky. Basically, we don't want to check preclusion/inclusion between LNodes that
			# * are supposed to exist and hyperarcs that are not (supposed to exist). The converse of this is
			# * check if it is a NotExist L-node (regardless of the hyperarc) or if the hyperarc is to exist.
LNode.arcs.Contains(ruleHyperarc) != hostNode.arcs.Contains(hostHyperarc):
				# finally, if the hyperarc is connected to the LNode (i.e. contains is true) then it should
				# * also connect in the host between the same matched elements. OR if the ruleHyperarc precludes
				# * the L-node (i.e. contains is false), then it should be false in the host as well.
				return False
			i += 1
		# if they are not the same (true != false) then we return false.
		return True