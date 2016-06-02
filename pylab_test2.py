#!/usr/bin/python2.7

__author__ = 'wp'

import math
import pylab

# initialize the two lists and the counting variable num. Note is a float
x_values = []
y_values = []
num = 0.0

# collect both num and the sine of num in a list
while num < math.pi * 4:
    y_values.append(math.sin(num))
    x_values.append(num)
    num += 0.01

# plot the x and y values as red circles
pylab.plot(x_values, y_values, 'ro')
pylab.show()