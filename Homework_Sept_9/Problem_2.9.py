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

from crystalmath import *

# Create a unit cell...
unitCell = UnitCell( "AA" )

# Unit cell parameters for Anhydrous Alum from Chapter 1
unitCell.a = 4.709
unitCell.b = 4.709
unitCell.c = 7.984

unitCell.alpha = 90.0 * deg2rad
unitCell.beta = 90.0 * deg2rad
unitCell.gamma = 120.0 * deg2rad

# Define the fractional coordinates...
X_S = numpy.array( [0.333, 0.337, 0.222], ndmin=2 )  # Note: ndmin allows transpose to work
X_O = numpy.array( [0.667, 0.656, 0.317], ndmin=2 )

 
bond_length = unitCell.bond_length( X_S, X_O )

print "Interatomic bond length: ", bond_length, " Angstroms"

# Interatomic bond length:  1.71548966055  Angstroms
