#!/usr/bin/python

import simulation

#Instantiate and run a simulation. 
sim = simulation.Simulation(num_agents=20, max_iterations=40, connectivity=.3)
sim.run()

