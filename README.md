GraphSelfOrganization Research
==============================

This repository contains an a Python implementation of NSF-funded research to define optimal graphs for a complex engineering system.


**Requirements:**

* Python 2.7.5 (converting to Python 3.x would not be painful)
* numpy
* matplotlib
* networkx

To run an example, open your Python shell in the base directory and use:

    >>>import simulation
    >>>simulation.run()

The code here so far does not solve any engineering problem, but it does demonstrate many of the tools available for such a task. I recommend reading the proposal before going through this code. Below are definitions of several key concepts from the proposal, along with their location in this repository. 


**Agents**

An agent is an entity that represents some part of a design and acts to improve that design - the 'Cell' in Cellular Self-Organization. It makes decisions based on its environment and the surrounding agents. An example agent object may be found in agents/agent.py. 

Advice: keep each agent's influence and knowledge as local as possible. As each agent gains more influence, the aggregate behavior becomes more difficult to analyze, predict, or design. An explicit local utility function is not included in this example implementation, but that might be useful. Note: this example makes all decisions randomly, which is almost certainly not what you want. 


**Rules and Options**

A rule is a template for agent choices, and an option is a potential agent action and an instance of a rule. A rule may say, "If an agent sees X, then it may be beneficial to do Y." An option says, "It may be beneficial for agent A to do Y." While in traditional design optimization only one option is chosen at each step, in CSO giving each agent a choice at each step is more natural. 

A rule is responsible for recognizing where it can apply and generating an option for each potential application of itself. Example code for rules and options may be found in rulesets/rules.py. I have written rules coupled to a field and a graph, respectively. The environmental penalty function in simulation.py may also be considered a rule, even though the agent has no choice but to apply it. 

Advice: Options may conflict with other options or with themselves, so logic to prevent this may be necessary. If the same option is associated with more than one agent, it may be necessary to remove it from consideration after being applied once. Look up "confluence" for existing work on the interactions between rules. As a warning: most literature will use the word "rules" to speak about both rules and options. The distinction matters for you, although it may not matter for them. 


**Fields**

A field is a mathematical function whose domain is the space over which the agents move. Probably this is directly analogous to physical space, but it doesn't have to be. A field may map that space into scalar or vector quantities, as long as that quantity is unique for a given point in space. A field may arise from the environment (the penalty field in simulation.py), other agents (Field and VectorField in fields/field.py), some known goal information, or even a graph - maybe each link creates a local field. In the examples here, the field directly affects agent movement, but you may also treat a field as sensory information that aids agent decision-making. 

Advice: The main way you can tell if some effect counts as a field is to ask this question, "If this agent sees value X at this point in the domain, would another agent also see value X at this point?". If the answer is no - for instance if the value an agent sees depends on what other agents it's connected to - then you aren't dealing with a field. (That doesn't mean whatever you're dealing with isn't useful, though.) To reiterate some advice from the agent section: Try to keep field effects local if you can. 


**Graphs**

A graph is a network between agents. The nodes and links may have information associated with them; that information is also considered part of the graph. Graphs can be used to represent aspects of an engineering design or to transmit information between agents. Although the graph in the example here doesn't change over the course of the simulation, there is no reason it should not change due to agent choice or physical constraints. Read more about creating and manipulating graphs in the networkx documentation. 

Advice: Some of the most complicated logic in this research can arise from options that attempt to simultaneously mutate a graph. Keep your graph grammar rules simple. (Simple rules tend to be local.)


written by Jack Hall, University of Texas at Austin, August 2013

email: jackhall@utexas.edu

