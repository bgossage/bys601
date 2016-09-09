#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.7

from crystalmath import *


unitCell = UnitCell()


# Unit cell paramters for CuSO4 5H2O              
unitCell.a = 6.091
unitCell.b = 10.63
unitCell.c = 5.064

unitCell.alpha = 82.410 * deg2rad
unitCell.beta = 107.50 * deg2rad
unitCell.gamma = 102.70 * deg2rad


print "The unit cell G Matrix: \n", unitCell.gmatrix()


# The unit cell G Matrix: 
# [[  37.100281    -14.23445474   -9.27521746]
#  [ -14.23445474  112.9969        7.11009107]
#  [  -9.27521746    7.11009107   25.644096  ]]
