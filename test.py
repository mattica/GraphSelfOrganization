#!/usr/bin/python

import simulation
import sys

sim = simulation.Simulation(num_agents=20, iterations=50, connectivity=0) 
sim.run()

