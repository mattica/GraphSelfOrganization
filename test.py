#!/usr/bin/python
import sys
import time
import numpy
import matplotlib.pyplot as plt
import simulation
import field as fld

##test mexican hat and its gradient
#x, y = numpy.meshgrid(numpy.linspace(-6.0, 6.0, 20), 
#					  numpy.linspace(-6.0, 6.0, 20)) 
#pos = zip(numpy.reshape(x, -1).tolist(), numpy.reshape(y, -1).tolist())
##mexicanhat = fld.MexicanHat()
#gradient = fld.MexicanHatGradient(3.0)
#origin = numpy.zeros(2)
##hat = [mexicanhat(origin, point) for point in pos]
#grd = [gradient(origin, numpy.array(point)) for point in pos]
#dx, dy = [a[0] for a in grd], [a[1] for a in grd]
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.quiver(x, y, dx, dy)
##ax.plot(x, y, hat)
#plt.show()


sim = simulation.Simulation(num_agents=20, iterations=40, connectivity=.3)
sim.run()
#raw_input("Press Enter to end...")

