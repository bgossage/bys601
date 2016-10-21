#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.9

import sys

#
# Setup path to crystalmath module...
#
sys.path.append( "../modules" )

from crystalmath import *

# Create a unit cell...
unitCell = UnitCell( "AA" )

# Unit cell paramters for CuSO4 5H2O              
unitCell.a = 6.091
unitCell.b = 10.63
unitCell.c = 5.064

unitCell.alpha = 82.410 * deg2rad
unitCell.beta = 107.50 * deg2rad
unitCell.gamma = 102.70 * deg2rad

# Define the fractional coordinates...
X_S = numpy.array( [0.333, 0.337, 0.222], ndmin=2 )  # Note: ndmin allows transpose to work
X_O = numpy.array( [0.667, 0.656, 0.317], ndmin=2 )

 
bond_length = unitCell.bond_length( X_S, X_O )

print "Interatomic bond length: ", bond_length, " Angstroms"

# Interatomic bond length:  3.5606127765  Angstroms

