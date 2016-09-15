#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Assignment 3, Sept 14, 2016
#

import sys

sys.path.append( "../modules" )

import math
import numpy
import crystalmath

deg2rad = numpy.pi / 180.0

unitCell = crystalmath.UnitCell()

# Unit cell paramters for oxidoreductase RCSB 5DBQ              
# Crystal structure of insect thioredoxin at 1.95 angstroms
unitCell.a = 107.710
unitCell.b = 28.980
unitCell.c = 79.860

unitCell.alpha = 90.00 * crystalmath.deg2rad
unitCell.beta = 128.32 * crystalmath.deg2rad
unitCell.gamma = 90.00 * crystalmath.deg2rad

Vol = unitCell.volume()


print "The volume of the unit cell is equal to %0.2f cubic angstroms."  %Vol


