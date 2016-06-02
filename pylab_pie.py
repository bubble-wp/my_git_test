#!/usr/bin/python2.7
__author__ = 'wp'

import pylab

values = [10, 20, 50, 100, 200, 1000]
pieLabels = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

# these are the default colors. You get these if you do not provide any
colorLst = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')

pylab.pie(values, labels=pieLabels, colors=colorLst)
pylab.title('Pie chart of 6 values')
pylab.show()

