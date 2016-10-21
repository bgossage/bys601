#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.11

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
C = numpy.array( [-0.180, -0.109, 0.0], ndmin=2 )
D = numpy.array( [0.145, 0.371, 0.0], ndmin=2 )

ABC_angle = unitCell.bond_angle( A, B, C )
ADC_angle = unitCell.bond_angle( A, D, C )

ADB_angle = 360.0 - ABC_angle - ADC_angle


print "ABC bond angle: ", ABC_angle, " Degrees"
print "ADC bond angle: ", ADC_angle, " Degrees"
print "ADB bond angle: ", ADB_angle, " Degrees"


# ABC bond angle:  30.007857707  Degrees
# ADC bond angle:  150.111019677  Degrees
# ADB bond angle:  179.881122616  Degrees


# EOF
