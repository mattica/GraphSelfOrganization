import clr

			import clr

			import clr

			import clr

			import clr

			import clr

			import clr

			import clr

# ************************************************************************
# *     This BasicFiler file & interface is part of the GraphSynth.BaseClasses
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
from System.Collections import *
from System.Collections.Generic import *
from System.Globalization import *
from System.IO import *
from System.Linq import *
from System.Text import *
from System.Xml import *
from System.Xml.Linq import *
from System.Xml.Serialization import *
from GraphSynth.Representation import *

class BasicFiler(object):
	""" <summary>
	   This method saves and opens basic graphs and rules (doesn't include WPF shapes)
	   as well as rulesets, which are the same as in earlier versions of GraphSynth.
	 </summary>
	"""
	def __init__(self, iDir, oDir, rDir):
		""" <summary>
		   Initializes a new instance of the <see cref = "BasicFiler" /> class.
		 </summary>
		 <param name = "iDir">The input directory.</param>
		 <param name = "oDir">The output directory.</param>
		 <param name = "rDir">The rules directory.</param>
		"""
		# <summary>
		#   This constant is used to tell other XML parsers (namely XAML displayers)
		#   to ignore elements that are prefaced with this.
		# </summary>
		self._IgnorablePrefix = "GraphSynth:"
		inputDirectory = iDir
		outputDirectory = oDir
		rulesDirectory = rDir

	# <summary>
	#   Gets or sets the input directory.
	# </summary>
	# <value>The input directory.</value>
	def get_inputDirectory(self):

	def set_inputDirectory(self, value):

	inputDirectory = property(fget=get_inputDirectory, fset=set_inputDirectory)

	# <summary>
	#   Gets or sets the output directory.
	# </summary>
	# <value>The output directory.</value>
	def get_outputDirectory(self):

	def set_outputDirectory(self, value):

	outputDirectory = property(fget=get_outputDirectory, fset=set_outputDirectory)

	# <summary>
	#   Gets or sets the rules directory.
	# </summary>
	# <value>The rules directory.</value>
	def get_rulesDirectory(self):

	def set_rulesDirectory(self, value):

	rulesDirectory = property(fget=get_rulesDirectory, fset=set_rulesDirectory)

	def Save(self, filename, o, SuppressWarnings):
		""" <summary>
		   Saves the object, o, to the specified filename.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <param name = "o">The object to save.</param>
		 <param name = "SuppressWarnings">if set to <c>true</c> [suppress warnings].</param>
		"""
		if :
			self.SaveGraph(filename, o)
		elif :
			self.SaveRule(filename, o)
		elif :
			self.SaveRuleSet(filename, o)
		elif :
			self.SaveCandidate(filename, o)
		elif :
			self.SaveCandidates(filename, o)
		elif not SuppressWarnings:
			raise Exception("Basic Filer (in GraphSynth.Representation) " + "received a different type than expected. Save was expecting " + "an object of type: designGraph, grammarRule, ruleSet, or candidate.")

	def Open(self, filename, SuppressWarnings):
		""" <summary>
		   Opens the list of objects at the specified filename.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <param name = "SuppressWarnings">if set to <c>true</c> [suppresses warnings].</param>
		 <returns>an array of opened objects</returns>
		"""
		# Load the file.
		doc = XmlDocument()
		doc.Load(filename)
		# create prefix<->namespace mappings (if any)
		nsMgr = XmlNamespaceManager(doc.NameTable)
		# Query the document
		if (doc.SelectNodes("/designGraph", nsMgr).Count > 0) or (doc.DocumentElement.Attributes["Tag"].Value == "Graph"):
			return Array[Object]((self.OpenGraph(filename)))
		if (doc.SelectNodes("/grammarRule", nsMgr).Count > 0) or (doc.DocumentElement.Attributes["Tag"].Value == "Rule"):
			return Array[Object]((self.OpenRule(filename)))
		if doc.SelectNodes("/ruleSet", nsMgr).Count > 0:
			return Array[Object]((self.OpenRuleSet(filename)))
		if doc.SelectNodes("/candidate", nsMgr).Count > 0:
			return Array[Object]((self.OpenCandidate(filename)))
		if not SuppressWarnings:
			raise Exception("Basic Filer (in GraphSynth.Representation) " + "opened a different type than expected. Open was expecting " + "an object of type: designGraph, grammarRule, ruleSet, or candidate.")
		return Array.CreateInstance(Object, 0)

	def SaveGraph(self, filename, graph1):
		""" <summary>
		   Saves the graph.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <param name = "graph1">The graph1.</param>
		"""
		graphWriter = None
		graph1.name = Path.GetFileNameWithoutExtension(filename)
		graph1.checkForRepeatNames()
		self.removeNullWhiteSpaceEmptyLabels(graph1)
		try:
			graphWriter = StreamWriter(filename)
			s = self.SerializeGraphToXml(graph1)
			if s != None:
				graphWriter.Write(s)
		except FileNotFoundException, fnfe:
			SearchIO.output("***Error Writing to File***")
			SearchIO.output(fnfe.ToString())
		finally:
			if graphWriter != None:
				graphWriter.Close()

	def SerializeGraphToXml(self, graph1):
		""" <summary>
		   Serializes the graph to XML.
		 </summary>
		 <param name = "graph1">The graph1.</param>
		 <returns></returns>
		"""
		try:
			settings = XmlWriterSettings(Indent = True, NewLineOnAttributes = True, CloseOutput = True, OmitXmlDeclaration = True)
			saveString = StringBuilder()
			saveXML = XmlWriter.Create(saveString, settings)
			graphSerializer = XmlSerializer(clr.GetClrType(designGraph))
			graphSerializer.Serialize(saveXML, graph1)
			return (saveString.ToString())
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
			return None
		finally:

	def OpenGraph(self, filename):
		""" <summary>
		   Opens the graph.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <returns></returns>
		"""
		newDesignGraph = None
		xmlGraph = None
		try:
			xmlGraph = XElement.Load(filename)
		except FileLoadException, fle:
			SearchIO.output("File was not found or accessible: " + fle)
			filename = ""
		finally:
		if not str.IsNullOrWhiteSpace(filename):
			if not xmlGraph.Name.LocalName.Contains("designGraph"):
				xmlGraph = ().FirstOrDefault()
			if xmlGraph != None:
				newDesignGraph = self.DeSerializeGraphFromXML(xmlGraph.ToString())
				if (str.IsNullOrWhiteSpace(newDesignGraph.name)) or (newDesignGraph.name == "Untitled"):
					newDesignGraph.name = Path.GetFileNameWithoutExtension(filename)
				SearchIO.output(Path.GetFileName(filename) + " successfully loaded.")
				self.RestoreDisplayShapes(newDesignGraph)
			else:
				SearchIO.output(Path.GetFileName(filename) + " does not contain design graph data.")
		return newDesignGraph

	def DeSerializeGraphFromXML(self, xmlString):
		""" <summary>
		   Deserialize graph from XML.
		 </summary>
		 <param name = "xmlString">The XML string.</param>
		 <returns></returns>
		"""
		try:
			stringReader = StringReader(xmlString)
			graphDeserializer = XmlSerializer(clr.GetClrType(designGraph))
			newDesignGraph = graphDeserializer.Deserialize(stringReader)
			newDesignGraph.internallyConnectGraph()
			self.removeNullWhiteSpaceEmptyLabels(newDesignGraph)
			return newDesignGraph
		except Exception, ioe:
			SearchIO.output("***Error Opening Graph:*** ")
			SearchIO.output(ioe.ToString())
			return None
		finally:

	def removeNullWhiteSpaceEmptyLabels(g):
		""" <summary>
		 Removes the null white space empty labels.
		 </summary>
		 <param name="g">The g.</param>
		"""
		g.globalLabels.RemoveAll(str.IsNullOrWhiteSpace)
		enumerator = g.arcs.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			a.localLabels.RemoveAll(str.IsNullOrWhiteSpace)
		enumerator = g.nodes.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			a.localLabels.RemoveAll(str.IsNullOrWhiteSpace)
		enumerator = g.hyperarcs.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			a.localLabels.RemoveAll(str.IsNullOrWhiteSpace)

	removeNullWhiteSpaceEmptyLabels = staticmethod(removeNullWhiteSpaceEmptyLabels)

	def RestoreDisplayShapes(graph):
		""" <summary>
		   Restores the display shapes.
		 </summary>
		 <param name = "graph">The graph.</param>
		"""
		oldX = 0.0
		oldY = 0.0
		oldZ = 0.0
		minY = Double.PositiveInfinity
		shapeKey = ""
		enumerator = graph.nodes.GetEnumerator()
		while enumerator.MoveNext():
			n = enumerator.Current
			if n.extraData != None:
				i = n.extraData.GetLength(0) - 1
				while i >= 0:
					unkXmlElt = n.extraData[i]
					if (unkXmlElt.Name == "screenX") and (unkXmlElt.InnerText.Length > 0):
						oldX = Double.Parse(unkXmlElt.InnerText)
					elif (unkXmlElt.Name == "screenY") and (unkXmlElt.InnerText.Length > 0):
						oldY = -Double.Parse(unkXmlElt.InnerText)
					if (unkXmlElt.Name == "x") and (unkXmlElt.InnerText.Length > 0):
						oldX = Double.Parse(unkXmlElt.InnerText)
					elif (unkXmlElt.Name == "y") and (unkXmlElt.InnerText.Length > 0):
						oldY = Double.Parse(unkXmlElt.InnerText)
					elif (unkXmlElt.Name == "z") and (unkXmlElt.InnerText.Length > 0):
						oldZ = Double.Parse(unkXmlElt.InnerText)
					elif (unkXmlElt.Name == "shapekey") and (unkXmlElt.InnerText.Length > 0):
						shapeKey = unkXmlElt.InnerText
					n.extraData[i] = None
					i -= 1
			if (n.X == 0.0f) and (n.Y == 0.0f) and (n.Z == 0.0f):
				n.X = oldX
				n.Y = oldY
				n.Z = oldZ
			if n.Y < minY:
				minY = n.Y
			n.DisplayShape = ShapeData(shapeKey, n)
		# the whole point of minY is to translate the figure up so that the coordinates are
		# * all non-negative. In the preceding parsing of xmlElements, you'll note that screenY
		# * is parsed to a negative number. But since we are now using a proper right hand
		# * coordinate frame we need to move all of these to new positions. Hence, we now move
		# * all the y-coords up by the greatest negative number found.
		if minY < 0:
			enumerator = graph.nodes.GetEnumerator()
			while enumerator.MoveNext():
				n = enumerator.Current
				n.Y -= self.minY
		shapeKey = ""
		enumerator = graph.arcs.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			if a.extraData != None:
				i = a.extraData.GetLength(0) - 1
				while i >= 0:
					unkXmlElt = a.extraData[i]
					if (unkXmlElt.Name == "styleKey") and (unkXmlElt.InnerText.Length > 0):
						shapeKey = unkXmlElt.InnerText
						a.extraData[i] = None
					i -= 1
			a.DisplayShape = ShapeData(shapeKey, a)
		enumerator = graph.hyperarcs.GetEnumerator()
		while enumerator.MoveNext():
			h = enumerator.Current
			if h.extraData != None:
				i = h.extraData.GetLength(0) - 1
				while i >= 0:
					unkXmlElt = h.extraData[i]
					if (unkXmlElt.Name == "styleKey") and (unkXmlElt.InnerText.Length > 0):
						shapeKey = unkXmlElt.InnerText
						h.extraData[i] = None
					i -= 1
			h.DisplayShape = ShapeData(shapeKey, h)

	RestoreDisplayShapes = staticmethod(RestoreDisplayShapes)

	def SaveRule(self, filename, ruleToSave):
		""" <summary>
		   Saves the rule.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <param name = "ruleToSave">The rule to save.</param>
		"""
		ruleWriter = None
		try:
			ruleToSave.name = Path.GetFileNameWithoutExtension(filename)
			ruleToSave.L.checkForRepeatNames()
			self.removeNullWhiteSpaceEmptyLabels(ruleToSave.L)
			ruleToSave.R.checkForRepeatNames()
			self.removeNullWhiteSpaceEmptyLabels(ruleToSave.R)
			ruleToSave.ReorderNodes()
			ruleWriter = StreamWriter(filename)
			s = self.SerializeRuleToXml(ruleToSave)
			if s != None:
				ruleWriter.Write(s)
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
		finally:
			if ruleWriter != None:
				ruleWriter.Close()

	def SerializeRuleToXml(self, ruleToSave):
		""" <summary>
		   Serializes the rule to XML.
		 </summary>
		 <param name = "ruleToSave">The rule to save.</param>
		 <returns></returns>
		"""
		try:
			settings = XmlWriterSettings(Indent = True, NewLineOnAttributes = True, CloseOutput = True, OmitXmlDeclaration = True)
			saveString = StringBuilder()
			saveXML = XmlWriter.Create(saveString, settings)
			ruleSerializer = XmlSerializer(clr.GetClrType(grammarRule))
			ruleSerializer.Serialize(saveXML, ruleToSave)
			return (saveString.ToString())
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
			return None
		finally:

	def OpenRule(self, filename):
		""" <summary>
		   Opens the rule.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <returns></returns>
		"""
		newGrammarRule = None
		xmlRule = None
		try:
			xmlRule = XElement.Load(filename)
		except FileLoadException, fle:
			SearchIO.output("File was not found or accessible: " + fle)
			filename = ""
		finally:
		if not str.IsNullOrWhiteSpace(filename):
			if not xmlRule.Name.LocalName.Contains("grammarRule"):
				xmlRule = ().FirstOrDefault()
			if xmlRule != None:
				try:
					newGrammarRule = self.DeSerializeRuleFromXML(xmlRule.ToString())
					self.RestoreDisplayShapes(newGrammarRule.L)
					self.RestoreDisplayShapes(newGrammarRule.R)
					self.removeNullWhiteSpaceEmptyLabels(newGrammarRule.L)
					self.removeNullWhiteSpaceEmptyLabels(newGrammarRule.R)
					if (str.IsNullOrWhiteSpace(newGrammarRule.name)) or (newGrammarRule.name == "Untitled"):
						newGrammarRule.name = Path.GetFileNameWithoutExtension(filename)
				except Exception, ioe:
					SearchIO.output("***XML Serialization Error***")
					SearchIO.output(ioe.ToString())
				finally:
		return newGrammarRule

	def DeSerializeRuleFromXML(self, xmlString):
		""" <summary>
		   Deserialize rule from XML.
		 </summary>
		 <param name = "xmlString">The XML string.</param>
		 <returns></returns>
		"""
		try:
			stringReader = StringReader(xmlString)
			ruleDeserializer = XmlSerializer(clr.GetClrType(grammarRule))
			newGrammarRule = ruleDeserializer.Deserialize(stringReader)
			if newGrammarRule.L == None:
				newGrammarRule.L = designGraph()
			else:
				newGrammarRule.L.internallyConnectGraph()
			if newGrammarRule.R == None:
				newGrammarRule.R = designGraph()
			else:
				newGrammarRule.R.internallyConnectGraph()
			enumerator = newGrammarRule.embeddingRules.Where().GetEnumerator()
			while enumerator.MoveNext():
				er = enumerator.Current
				enumerator = er.oldLabels.GetEnumerator()
				while enumerator.MoveNext():
					unkXmlElt = enumerator.Current
					# this doesn't seem like the best place for this, but the doub'e foreach
					# * loop is intended to help load old grammar rules that have the simpler
					# * version of embedding rules.
					if (unkXmlElt.Name == "freeArcLabel") and (unkXmlElt.InnerText.Length > 0):
						er.freeArcLabels.Add(unkXmlElt.InnerText)
					if (unkXmlElt.Name == "neighborNodeLabel") and (unkXmlElt.InnerText.Length > 0):
						er.neighborNodeLabels.Add(unkXmlElt.InnerText)
				er.oldLabels = None
			return newGrammarRule
		except Exception, ioe:
			SearchIO.output("***Error Opening Graph:*** ")
			SearchIO.output(ioe.ToString())
			return None
		finally:

	def checkRule(gR):
		""" <summary>
		 Checks the rule with some issues that may have been overlooked.
		 </summary>
		 <param name="gR">The grammar rule.</param>
		 <returns></returns>
		"""
		if (gR.L.checkForRepeatNames()) and not SearchIO.MessageBoxShow("You are not allowed to have repeat names in L. I have changed these " + "names to be unique, which may have disrupted your context graph, K. Do you want to continue?", "Repeat names in L", "Information", "YesNo", "Yes"):
			return False
		if (gR.R.checkForRepeatNames()) and not SearchIO.MessageBoxShow("You are not allowed to have repeat names in R. I have changed" + " these names to be unique, which may have disrupted your context graph, K. Do you" + " want to continue?", "Repeat names in R", "Information", "YesNo", "Yes"):
			return False
		if (BasicFiler.NotExistElementsinKR(gR)) and not SearchIO.MessageBoxShow("There appears to be common elements between " + "the left and right hand sides of the rule that are indicated as \"Must NOT Exist\"" + " within the left-hand side. This is not allowed. Continue Anyway?", "Improper use of negative elements", "Error", "YesNo", "No"):
			return False
		if (BasicFiler.NumKElements(gR) == 0) and not SearchIO.MessageBoxShow("There appears to be no common elements between " + "the left and right hand sides of the rule. Is this intentional? If so, click yes to continue.", "No Context Graph", "Information", "YesNo", "Yes"):
			return False
		if (BasicFiler.KarcsChangeDirection(gR) != "") and not SearchIO.MessageBoxShow("It appears that arc(s): " + BasicFiler.KarcsChangeDirection(gR) + " change direction (to = from or vice-versa). Even though the arc(s) might be undirected," + " this can still lead to problems in the rule application, it is recommended that this is" + " fixed before saving. Save anyway?", "Change in Arc Direction", "Information", "YesNo", "Yes"):
			return False
		if (not BasicFiler.ValidateFreeArcEmbeddingRules(gR)) and not SearchIO.MessageBoxShow("There appears to be invalid references in the free arc embedding rules." + " Node names used in free arc embedding rules do not exist. Continue Anyway?", "Invalid Free-Arc References", "Error", "YesNo", "No"):
			return False
		gR.ReorderNodes()
		return True

	checkRule = staticmethod(checkRule)

	def NotExistElementsinKR(gR):
		""" <summary>
		 Checks to see that the negative elements are not stored in K and R.
		 </summary>
		 <param name="gR">The grammar rule.</param>
		 <returns></returns>
		"""
		return (gR.L.nodes.Any() or gR.L.arcs.Any() or gR.L.hyperarcs.Any())

	NotExistElementsinKR = staticmethod(NotExistElementsinKR)

	def KarcsChangeDirection(gR):
		""" <summary>
		 Checks that the K arcs do not change direction.
		 </summary>
		 <param name="gR">The grammar rule.</param>
		 <returns></returns>
		"""
		badArcNames = ""
		enumerator = gR.L.arcs.GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			b = gR.R.arcs.Find()
			if b != None:
				if ((a.To != None) and (b.From != None) and (a.To.name == b.From.name)) or ((a.From != None) and (b.To != None) and (a.From.name == b.To.name)):
					badArcNames += a.name + ", "
		return badArcNames

	KarcsChangeDirection = staticmethod(KarcsChangeDirection)

	def NumKElements(gR):
		""" <summary>
		 Checks that the number of K elements is greater than 0.
		 </summary>
		 <param name="gR">The grammar rule.</param>
		 <returns></returns>
		"""
		return gR.L.nodes.Count() + gR.L.arcs.Count() + gR.L.hyperarcs.Count()

	NumKElements = staticmethod(NumKElements)

	def ValidateFreeArcEmbeddingRules(gR):
		""" <summary>
		 Validates the free arc embedding rules.
		 </summary>
		 <param name="gR">The grammar rule.</param>
		 <returns></returns>
		"""
		if gR.embeddingRules == None:
			return True
		result = True
		i = 0
		while i < gR.embeddingRules.Count:
			eR = gR.embeddingRules[i]
			if (str.IsNullOrWhiteSpace(eR.LNodeName)) or (eR.LNodeName.Equals("<any>")):
				eR.LNodeName = None
			elif not gR.L.nodes.Any():
				SearchIO.output("Error in the embedding rules #" + i + ": No L-node named " + eR.LNodeName)
				result = False
			if (str.IsNullOrWhiteSpace(eR.RNodeName)) or (eR.RNodeName.Equals("<any>")):
				eR.RNodeName = None
			elif not gR.R.nodes.Any():
				SearchIO.output("Error in the embedding rules #" + i + ": No R-node named " + eR.RNodeName)
				result = False
			if not result:
				break
			i += 1
		return result

	ValidateFreeArcEmbeddingRules = staticmethod(ValidateFreeArcEmbeddingRules)

	def SaveRuleSet(self, filename, ruleSetToSave):
		""" <summary>
		   Saves the rule set.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <param name = "ruleSetToSave">The rule set to save.</param>
		"""
		ruleWriter = None
		try:
			ruleSetToSave.name = Path.GetFileNameWithoutExtension(filename)
			ruleWriter = StreamWriter(filename)
			ruleSerializer = XmlSerializer(clr.GetClrType(ruleSet))
			ruleSerializer.Serialize(ruleWriter, ruleSetToSave)
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
		finally:
			if ruleWriter != None:
				ruleWriter.Close()

	def OpenRuleSet(self, filename):
		""" <summary>
		   Opens the rule set.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <returns></returns>
		"""
		newRuleSet = None
		ruleReader = None
		try:
			ruleReader = StreamReader(filename)
			ruleDeserializer = XmlSerializer(clr.GetClrType(ruleSet))
			newRuleSet = ruleDeserializer.Deserialize(ruleReader)
			newRuleSet.rulesDir = Path.GetDirectoryName(filename) + Path.DirectorySeparatorChar
			newRuleSet.filer = self
			numRules = newRuleSet.ruleFileNames.Count
			newRuleSet.rules = self.LoadRulesFromFileNames(newRuleSet.rulesDir, newRuleSet.ruleFileNames, )
			SearchIO.output(Path.GetFileName(filename) + " successfully loaded")
			if numRules == numLoaded:
				SearchIO.output(" and all (" + numLoaded + ") rules loaded successfully.")
			else:
				SearchIO.output("     but " + (numRules - numLoaded) + " rules did not load.")
			newRuleSet.initializeFileWatcher(newRuleSet.rulesDir)
			if (str.IsNullOrWhiteSpace(newRuleSet.name)) or (newRuleSet.name == "Untitled"):
				newRuleSet.name = Path.GetFileNameWithoutExtension(filename)
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
		finally:
			if ruleReader != None:
				ruleReader.Close()
		return newRuleSet

	def LoadRulesFromFileNames(self, ruleDir, ruleFileNames, numLoaded):
		""" <summary>
		   Loads the rules from file names.
		 </summary>
		 <param name = "ruleDir">The rule dir.</param>
		 <param name = "ruleFileNames">The rule file names.</param>
		 <param name = "numLoaded">The num loaded.</param>
		 <returns></returns>
		"""
		rules = List[grammarRule]()
		numLoaded = 0
		while numLoaded < ruleFileNames.Count:
			rulePath = ruleDir + ruleFileNames[numLoaded]
			if File.Exists(rulePath):
				SearchIO.output("Loading " + ruleFileNames[numLoaded])
				ruleObj = self.Open(rulePath)
				if :
					rules.Add(ruleObj)
				elif :
					rules.AddRange((ruleObj).Where().Cast())
				numLoaded += 1
			else:
				SearchIO.output("Rule Not Found: " + ruleFileNames[numLoaded])
				ruleFileNames.RemoveAt(numLoaded)
		return rules

	def ReloadSpecificRule(self, rs, i):
		""" <summary>
		   Reloads the specific rule.
		 </summary>
		 <param name = "rs">The rs.</param>
		 <param name = "i">The i.</param>
		"""
		rulePath = rs.rulesDir + rs.ruleFileNames[i]
		SearchIO.output("Loading " + rs.ruleFileNames[i])
		ruleObj = self.Open(rulePath)
		if :
			rs.rules[i] = ruleObj
		elif  and :
			rs.rules[i] = ((ruleObj)[0])

	def SaveCandidates(self, filename, candidates, SaveToOutputDir, timeStamp):
		""" <summary>
		 Saves the candidate.
		 </summary>
		 <param name="filename">The filename.</param>
		 <param name="candidates">The candidates.</param>
		 <param name="SaveToOutputDir">if set to <c>true</c> [save to output dir].</param>
		 <param name="timeStamp">if set to <c>true</c> [time stamp].</param>
		"""
		outputDir = self.outputDirectory
		if not SaveToOutputDir:
			outputDir = Path.GetFullPath(filename)
		filename = Path.GetFileNameWithoutExtension(filename)
		i = 0
		while i != candidates.Count:
			counter = i.ToString(CultureInfo.InvariantCulture)
			counter = counter.PadLeft(3, '0')
			tod = ""
			if timeStamp:
				tod = "." + DateTime.Now.Year + "." + DateTime.Now.Month + "." + DateTime.Now.Day + "." + DateTime.Now.Hour + "." + DateTime.Now.Minute + "." + DateTime.Now.Second + "."
			self.SaveCandidate(outputDir + filename + counter + tod + ".xml", candidates[i])
			i += 1

	def SaveCandidate(self, filename, c1):
		""" <summary>
		   Saves the candidate.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <param name = "c1">The c1.</param>
		"""
		# c1.graph.checkForRepeatNames();
		candidateWriter = None
		try:
			c1.graphFileName = Path.GetFileNameWithoutExtension(filename) + ".gxml"
			candidateWriter = StreamWriter(filename)
			candidateSerializer = XmlSerializer(clr.GetClrType(candidate))
			candidateSerializer.Serialize(candidateWriter, c1)
			self.Save(Path.GetDirectoryName(filename) + "/" + c1.graphFileName, c1.graph)
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
		finally:
			if candidateWriter != None:
				candidateWriter.Close()

	def OpenCandidate(self, filename):
		""" <summary>
		   Opens the candidate.
		 </summary>
		 <param name = "filename">The filename.</param>
		 <returns></returns>
		"""
		newCandidate = None
		candidateReader = None
		try:
			candidateReader = StreamReader(filename)
			candidateDeserializer = XmlSerializer(clr.GetClrType(candidate))
			newCandidate = candidateDeserializer.Deserialize(candidateReader)
			newCandidate.graph = self.Open(Path.GetDirectoryName(filename) + "/" + newCandidate.graphFileName)[0]
		except Exception, ioe:
			SearchIO.output("***XML Serialization Error***")
			SearchIO.output(ioe.ToString())
		finally:
			if candidateReader != None:
				candidateReader.Close()
		return newCandidate