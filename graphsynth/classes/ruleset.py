"""Base class for RuleSet.

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


# As far as I can tell, this is the first time the idea of a rule set
# * has been developed to this degree. In many applications we find that
# * different sets of rules are needed. Many of these characteristics
# * are built into our current generation process.
class ruleSet(object):
	# A ruleSet can have one rule set to the triggerRule. If there is no
	# * triggerRule, then this should stay at negative one (or any negative
	# * number). When the trigger rule is applied, the generation process, will
	# * exit to the specified generationStep (as described below).
	# <summary>
	#   For a particular set of rules, we need to specify what generation should
	#   do if any of five conditions occur during the recognize->choose->apply
	#   cycle. The enumerator, nextGenerationSteps, listed in globalSettings.cs
	#   indicates what to do. The five correspond directly to the five elements
	#   of another enumerator called GenerationStatuses. These five possibilties are:
	#   Normal, Choice, CycleLimit, NoRules, TriggerRule. So, following normal operation 
	#   of RCA (normal), we perform the first operation stated below, nextGenerationStep[0]
	#   this will likely be to LOOP and contine apply rules. Defaults for these are
	#   specified in App.gsconfig.
	# </summary>
	# <summary>
	#   Represents a list of the rule file names.
	# </summary>
	# <summary>
	#   Represents a list of the rules included within the ruleset.
	#   The rules are clearly part of the set, but these are not stored
	#   in the rsxml file, only the ruleFileNames.
	# </summary>
	# <summary>
	#   Gets or sets the name for the ruleSet - usually set to the filename
	# </summary>
	# <value>The name.</value>
	def get_name(self):

	def set_name(self, value):

	name = property(fget=get_name, fset=set_name)

	# <summary>
	#   Gets or sets the trigger rule num. Note: the rule numbers start at 1
	#   not zero. Here we keep track by using a zero-based private field with
	#   this property (as a way to remember. I know it sounds strange, but it
	#   works).
	# </summary>
	# <value>The trigger rule num.</value>
	def get_TriggerRuleNum(self):
		return self.__triggerRuleNum + 1

	def set_TriggerRuleNum(self, value):
		self.__triggerRuleNum = value - 1

	TriggerRuleNum = property(fget=get_TriggerRuleNum, fset=set_TriggerRuleNum)

	# <summary>
	#   Gets or sets the choice method - either automatic or by design.
	# </summary>
	# <value>The choice method.</value>
	def get_choiceMethod(self):
		return self.__choiceMethod

	def set_choiceMethod(self, value):
		self.__choiceMethod = value

	choiceMethod = property(fget=get_choiceMethod, fset=set_choiceMethod)

	# Often when multiple ruleSets are used, some will produce feasible candidates,
	# * while others will only produce steps towards a feasible candidate. Here, we
	# * classify a particular ruleSet as one of these.
	# <summary>
	#   Gets or sets the feasibility state of the interim candidates.
	# </summary>
	# <value>The interim candidates.</value>
	def get_interimCandidates(self):
		return self.__interimCandidates

	def set_interimCandidates(self, value):
		self.__interimCandidates = value

	interimCandidates = property(fget=get_interimCandidates, fset=set_interimCandidates)

	# <summary>
	#   Gets or sets the feasibility state of the final candidates.
	# </summary>
	# <value>The final candidates.</value>
	def get_finalCandidates(self):
		return self.__finalCandidates

	def set_finalCandidates(self, value):
		self.__finalCandidates = value

	finalCandidates = property(fget=get_finalCandidates, fset=set_finalCandidates)

	def get_RuleSetIndex(self):

	def set_RuleSetIndex(self, value):

	RuleSetIndex = property(fget=get_RuleSetIndex, fset=set_RuleSetIndex)

	# For multiple ruleSets, a value to store its place within the set of ruleSets
	# * proves a useful indicator.
	# <summary>
	#   Gets or sets the index of the rule set.
	# </summary>
	# <value>The index of the rule set.</value>
	# a C# file can be custom created to correspond to special recognize or apply
	# * instructions that may exist. These '.cs' are stored here.
	# <summary>
	#   Gets or sets the recognize source file names (string paths).
	# </summary>
	# <value>The recognize source files.</value>
	def get_recognizeSourceFiles(self):
		return self.__recognizeSourceFiles

	def set_recognizeSourceFiles(self, value):
		self.__recognizeSourceFiles = value

	recognizeSourceFiles = property(fget=get_recognizeSourceFiles, fset=set_recognizeSourceFiles)

	# <summary>
	#   Gets or sets the apply source file names (string paths).
	# </summary>
	# <value>The apply source files.</value>
	def get_applySourceFiles(self):
		return self.__applySourceFiles

	def set_applySourceFiles(self, value):
		self.__applySourceFiles = value

	applySourceFiles = property(fget=get_applySourceFiles, fset=set_applySourceFiles)

	def nextRuleSet(self, status):
		""" <summary>
		   Retrieves the index of the next rule set.A helper function to RecognizeChooseApplyCycle.
		   This function returns what the new ruleSet will be. Here the enumerator nextGenerationSteps
		   and GenerationStatuses is used to great affect. Understand that if a negative number is
		   returned, the cycle will be stopped.
		 </summary>
		 <param name = "status">The status.</param>
		 <returns></returns>
		"""
		if self._nextGenerationStep[status] == nextGenerationSteps.Loop:
			return self.RuleSetIndex
		elif self._nextGenerationStep[status] == nextGenerationSteps.GoToNext:
			return self.RuleSetIndex + 1
		elif self._nextGenerationStep[status] == nextGenerationSteps.GoToPrevious:
			return self.RuleSetIndex - 1
		else:
			return self._nextGenerationStep[status]

	def __init__(self):
		""" <summary>
		   Initializes a new instance of the <see cref = "ruleSet" /> class.
		 </summary>
		 <param name = "defaultRulesDir">The default rules dir.</param>
		"""
		self.__choiceMethod = choiceMethods.Design
		self.__finalCandidates = feasibilityState.Unspecified
		self.__interimCandidates = feasibilityState.Unspecified
		self.__triggerRuleNum = -1
		self._ruleFileNames = List[str]()
		self._rules = List[grammarRule]()
		self.__recognizeSourceFiles = List[str]()
		self.__applySourceFiles = List[str]()

	def __init__(self):
		self.__choiceMethod = choiceMethods.Design
		self.__finalCandidates = feasibilityState.Unspecified
		self.__interimCandidates = feasibilityState.Unspecified
		self.__triggerRuleNum = -1
		self._ruleFileNames = List[str]()
		self._rules = List[grammarRule]()
		self.__recognizeSourceFiles = List[str]()
		self.__applySourceFiles = List[str]()

	def recognize(self, host, InParallel, RelaxationTemplate):
		""" <summary>
		 This is the recognize function called within the RCA generation. It is
		 fairly straightforward method that basically invokes the more complex
		 recognize function for each rule within it, and returns a list of
		 options.
		 </summary>
		 <param name="host">The host.</param>
		 <param name="InParallel">if set to <c>true</c> [in parallel].</param>
		 <param name="RelaxationTemplate">The relaxation template.</param>
		 <returns></returns>
		"""
		options = List[option]()
		if self._rules.Count == 0:
			return options
		if self.choiceMethod == choiceMethods.Automatic:
			i = 0
			while i != self._rules.Count:
				ruleOpts = self._rules[i].recognize(host, InParallel, RelaxationTemplate if (generationAfterNoRules == nextGenerationSteps.Stop) else None)
				if ruleOpts.Count > 0:
					r0 = ruleOpts[0]
					r0.assignRuleInfo(i + 1, self.RuleSetIndex)
					return List[option](r0)
				i += 1
		elif InParallel: # new parallel rule check
			options = self._rules.SelectMany().AsParallel().ToList()
		else: # do in series
			options = self._rules.SelectMany().ToList()
		i = 0
		while i < options.Count:
			options[i].optionNumber = i
			i += 1
		return options

	# simple functions to add and remove rules from the ruleSet
	def Add(self, newRule):
		""" <summary>
		   Adds the specified new rule.
		 </summary>
		 <param name = "newRule">The new rule.</param>
		"""
		self._rules.Add(newRule)

	def Remove(self, removeRule):
		""" <summary>
		   Removes the specified remove rule.
		 </summary>
		 <param name = "removeRule">The remove rule.</param>
		"""
		self._rules.Remove(removeRule)

		
	def copy(self):
		""" Copies this instance of ruleset. """
        return deepcopy(self)


	def get_filer(self):

	def set_filer(self, value):

	filer = property(fget=get_filer, fset=set_filer)

	def get_rulesDir(self):

	def set_rulesDir(self, value):

	rulesDir = property(fget=get_rulesDir, fset=set_rulesDir)

	# <summary>
	#   Gets or sets the filer.
	# </summary>
	# <value>The filer.</value>
	# <summary>
	#   Gets or sets the rules dir.
	# </summary>
	# <value>The rules dir.</value>
	# <summary>
	#   Gets or sets the generation method after normal.
	# </summary>
	# <value>The generation after normal.</value>
	def get_generationAfterNormal(self):
		return nextGenerationStep[0]

	def set_generationAfterNormal(self, value):
		nextGenerationStep[0] = value

	generationAfterNormal = property(fget=get_generationAfterNormal, fset=set_generationAfterNormal)

	# <summary>
	#   Gets or sets the generation method after choice.
	# </summary>
	# <value>The generation after choice.</value>
	def get_generationAfterChoice(self):
		return nextGenerationStep[1]

	def set_generationAfterChoice(self, value):
		nextGenerationStep[1] = value

	generationAfterChoice = property(fget=get_generationAfterChoice, fset=set_generationAfterChoice)

	# <summary>
	#   Gets or sets the generation method after cycle limit.
	# </summary>
	# <value>The generation after cycle limit.</value>
	def get_generationAfterCycleLimit(self):
		return nextGenerationStep[2]

	def set_generationAfterCycleLimit(self, value):
		nextGenerationStep[2] = value

	generationAfterCycleLimit = property(fget=get_generationAfterCycleLimit, fset=set_generationAfterCycleLimit)

	# <summary>
	#   Gets or sets the generation method after no rules.
	# </summary>
	# <value>The generation after no rules.</value>
	def get_generationAfterNoRules(self):
		return nextGenerationStep[3]

	def set_generationAfterNoRules(self, value):
		nextGenerationStep[3] = value

	generationAfterNoRules = property(fget=get_generationAfterNoRules, fset=set_generationAfterNoRules)

	# <summary>
	#   Gets or sets the generation method after trigger rule.
	# </summary>
	# <value>The generation after trigger rule.</value>
	def get_generationAfterTriggerRule(self):
		return nextGenerationStep[4]

	def set_generationAfterTriggerRule(self, value):
		nextGenerationStep[4] = value

	generationAfterTriggerRule = property(fget=get_generationAfterTriggerRule, fset=set_generationAfterTriggerRule)

	def loadAndCompileSourceFiles(rulesets, recompileRules, compiledparamRules, execDir):
		""" <summary>
		   Loads and compiles the source files.
		 </summary>
		 <param name = "rulesets">The rulesets.</param>
		 <param name = "recompileRules">if set to <c>true</c> [recompile rules].</param>
		 <param name = "compiledparamRules">The compiledparam rules.</param>
		 <param name = "execDir">The exec dir.</param>
		"""
		if rulesets.GetLength(0) == 0:
			return 
		assem = None
		allSourceFiles = List[str]()
		rulesDirectory = rulesets[0].rulesDir
		if not recompileRules and (ruleSet.compiledFunctionsAlreadyLoaded(rulesets)):
			return 
		if recompileRules and ruleSet.FindSourceFiles(rulesets, allSourceFiles, rulesDirectory):
			if allSourceFiles.Count == 0:
				SearchIO.output("No additional code files to compile.", 4)
			else:
				if ruleSet.CompileSourceFiles(rulesets, allSourceFiles, , rulesDirectory, execDir, compiledparamRules):
					assem = cr.CompiledAssembly
		filenames = Array.CreateInstance(str, 0)
		if assem == None:
			# load .dll since compilation crashed
			filenames = Directory.GetFiles(rulesDirectory, "*" + compiledparamRules + "*")
			if filenames.GetLength(0) > 1:
				SearchIO.MessageBoxShow("More than one compiled library (*.dll) similar to " + compiledparamRules + "in" + rulesDirectory)
			if filenames.GetLength(0) == 0:
				SearchIO.MessageBoxShow("Compiled library: " + compiledparamRules + " not found in\n" + rulesDirectory + ".\n Attempting to recompile.")
				if ruleSet.CompileSourceFiles(rulesets, allSourceFiles, , rulesDirectory, execDir, compiledparamRules):
					assem = cr.CompiledAssembly
			else:
				assem = Assembly.LoadFrom(filenames[0])
		try:
			if assem != None:
				compiledFunctions = assem.CreateInstance("GraphSynth.ParamRules.ParamRules")
				enumerator = rulesets.SelectMany().GetEnumerator()
				while enumerator.MoveNext():
					rule = enumerator.Current
					rule.DLLofFunctions = compiledFunctions
					rule.recognizeFuncs.Clear()
					enumerator = rule.recognizeFunctions.GetEnumerator()
					while enumerator.MoveNext():
						functionName = enumerator.Current
						func = compiledFunctions.GetType().GetMethod(functionName)
						if func != None:
							rule.recognizeFuncs.Add(func)
						else:
							SearchIO.MessageBoxShow("Unable to locate function, " + functionName + ", in assembly, " + filenames[0] + ".")
					rule.applyFuncs.Clear()
					enumerator = rule.applyFunctions.GetEnumerator()
					while enumerator.MoveNext():
						functionName = enumerator.Current
						func = compiledFunctions.GetType().GetMethod(functionName)
						if func != None:
							rule.applyFuncs.Add(func)
						else:
							SearchIO.MessageBoxShow("Unable to locate function, " + functionName + ", in assembly, " + filenames[0] + ".")
		except Exception, e:
			SearchIO.MessageBoxShow("Compilation Error :" + ErrorLogger.MakeErrorString(e, False), "Error Compiling Additional Rule Functions", "Error")
		finally:

	loadAndCompileSourceFiles = staticmethod(loadAndCompileSourceFiles)

	def FindSourceFiles(rulesets, allSourceFiles, rulesDirectory):
		""" <summary>
		   Finds the source files.
		 </summary>
		 <param name = "rulesets">The rulesets.</param>
		 <param name = "allSourceFiles">All source files.</param>
		 <param name = "rulesDirectory">The rules directory.</param>
		 <returns></returns>
		"""
		filesFound = True
		enumerator = rulesets.Where().GetEnumerator()
		while enumerator.MoveNext():
			a = enumerator.Current
			enumerator = a.recognizeSourceFiles.GetEnumerator()
			while enumerator.MoveNext():
				file = enumerator.Current
				fileLower = file.ToLower()
				if File.Exists(rulesDirectory + fileLower):
					if not allSourceFiles.Contains(rulesDirectory + fileLower):
						allSourceFiles.Add(rulesDirectory + fileLower)
				else:
					SearchIO.MessageBoxShow("Missing source file: " + fileLower + ". Cancelling compilation of C# recognize source file.", "Missing File", "Error")
					filesFound = False
					break
			enumerator = a.applySourceFiles.GetEnumerator()
			while enumerator.MoveNext():
				file = enumerator.Current
				fileLower = file.ToLower()
				if File.Exists(rulesDirectory + fileLower):
					if not allSourceFiles.Contains(rulesDirectory + fileLower):
						allSourceFiles.Add(rulesDirectory + fileLower)
				else:
					SearchIO.MessageBoxShow("Missing source file: " + fileLower + ". Cancelling compilation of C# apply source file.", "Missing File", "Error")
					filesFound = False
					break
		return filesFound

	FindSourceFiles = staticmethod(FindSourceFiles)

	def CompileSourceFiles(rulesets, allSourceFiles, cr, rulesDir, execDir, compiledparamRules):
		""" <summary>
		   Compiles the source files.
		 </summary>
		 <param name = "rulesets">The rulesets.</param>
		 <param name = "allSourceFiles">All source files.</param>
		 <param name = "cr">The cr.</param>
		 <param name = "rulesDir">The rules dir.</param>
		 <param name = "execDir">The exec dir.</param>
		 <param name = "compiledparamRules">The compiledparam rules.</param>
		 <returns></returns>
		"""
		cr = None
		try:
			c = CSharpCodeProvider()
			# c.CreateCompiler();
			#                ICodeCompiler icc = c.CreateCompiler();
			cp = CompilerParameters()
			cp.ReferencedAssemblies.Add("system.dll")
			cp.ReferencedAssemblies.Add("system.xml.dll")
			cp.ReferencedAssemblies.Add("system.data.dll")
			cp.ReferencedAssemblies.Add("system.windows.forms.dll")
			#cp.ReferencedAssemblies.Add(execDir + "GraphSynth.exe");
			cp.ReferencedAssemblies.Add(execDir + "GraphSynth.BaseClasses.dll")
			cp.CompilerOptions = "/t:library"
			cp.GenerateInMemory = True
			cp.OutputAssembly = rulesDir + compiledparamRules
			allSourceFilesArray = allSourceFiles.ToArray()
			cr = c.CompileAssemblyFromFile(cp, allSourceFilesArray)
			#cr = icc.CompileAssemblyFromFileBatch(cp, allSourceFilesArray);
			if cr.Errors.HasErrors:
				raise Exception()
			return True
		except , :
			SearchIO.MessageBoxShow("Error Compiling C# recognize and apply source files.", "Compilation Error", "Error")
			enumerator = cr.Errors.GetEnumerator()
			while enumerator.MoveNext():
				e = enumerator.Current
				SearchIO.output(e.ToString())
			return False
		finally:

	CompileSourceFiles = staticmethod(CompileSourceFiles)

	def compiledFunctionsAlreadyLoaded(rulesets):
		return rulesets.Where().All()

	compiledFunctionsAlreadyLoaded = staticmethod(compiledFunctionsAlreadyLoaded)

