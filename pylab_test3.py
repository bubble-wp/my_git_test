#!/usr/bin/python2.7
__author__ = 'wp'

import math
import pylab
import numpy

# use numpy arange to get an array of float values
x_values = numpy.arange(0, math.pi * 4, 0.1)
y_values = [math.sin(x) for x in x_values]
pylab.plot(x_values, y_values)
pylab.xlabel('x values')
pylab.ylabel('sine of x')
pylab.title('Plot of sine fron 0 to 4*pi')
pylab.grid(True)
pylab.show()