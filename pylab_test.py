#!/usr/bin/python2.7

__author__ = 'wp'

import numpy
import pylab

listOfInts = []
for counter in range(10):
    listOfInts.append(counter * 2)

print listOfInts
print len(listOfInts)

# now plot the list
pylab.plot(listOfInts)
pylab.show()