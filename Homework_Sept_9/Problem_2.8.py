#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.8

from crystalmath import *


unitCell = UnitCell()


# Unit cell paramters for Anhydrous Alum from Chapter 1
unitCell.a = 4.709
unitCell.b = 4.709
unitCell.c = 7.984

unitCell.alpha = 90.0 * deg2rad
unitCell.beta = 90.0 * deg2rad
unitCell.gamma = 120.0 * deg2rad


print "The unit cell G Matrix: \n", unitCell.gmatrix()


# The unit cell G Matrix: 
#[[  2.21746810e+01  -1.10873405e+01   2.30213122e-15]
# [ -1.10873405e+01   2.21746810e+01   2.30213122e-15]
# [  2.30213122e-15   2.30213122e-15   6.37442560e+01]]

