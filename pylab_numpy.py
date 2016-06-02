#!/usr/bin/python2.7
__author__ = 'wp'

import numpy
import pylab

vals = numpy.ones(10000)
vals *= 100
# standard distribution, 10,000 elements, mu = 0, std = 1


sigma = numpy.random.standard_normal(10000)
sigma *= 15
# generate a standard distribution, mu = 100, std = 15

vals += sigma
pylab.hist(vals, 100)
pylab.title('Standard Distribution, mu=100, std=15')
pylab.show()
