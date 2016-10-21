#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.10

import sys

#
# Setup path to crystalmath module...
#
sys.path.append( "../modules" )

from crystalmath import *

# Create a unit cell...
unitCell = UnitCell( "HMB" )

# Unit cell parameters for HMB
unitCell.a = 9.010
unitCell.b = 8.926
unitCell.c = 5.344

unitCell.alpha = (44.0 + 27.0/60.0) * deg2rad
unitCell.beta = (116 + 43.0/60.0) * deg2rad
unitCell.gamma = (119 + 34.0/60.0) * deg2rad

# Define the fractional coordinates...
A = numpy.array( [0.071, 0.182, 0.0], ndmin=2 )  # Note: ndmin allows transpose to work
B = numpy.array( [-0.109, 0.073, 0.0], ndmin=2 )
D = numpy.array( [0.145, 0.371, 0.0], ndmin=2 )
 
# Calculate the benzene carbon atom bond lengths...
AB_length = unitCell.bond_length( A, B )

print "AB bond length: ", AB_length, " Angstroms"
print "Estimated carbon atom radius: ", AB_length/2.0, " (Angstroms)"
#
# Benzene ring bond lengths:  1.42  Angstroms
# Estimated carbon atom radius:  0.71  (Angstroms)

#
# All the bond lengths in the ring are equal, so this covers all six.
#

# Benzene-Methyl carbon bond length..
AD_length = unitCell.bond_length( A, D )

print "AD bond length: ", AD_length, " Angstroms"

print "Estimated carbon atom radius: ", AD_length/2.0, " (Angstroms)"
#
# Benzene-Methyl bond lengths:  1.47  Angstroms
# Estimated carbon atom radius:  0.74  (Angstroms)
#

# The covalent radius for Carbon: sp3 0.76, sp2 0.73, sp 0.69  (Angstroms)
