#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.12

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

print "HMB unit cell volume = ", unitCell.volume(), " Angstrom**3"

# HMB unit cell volume =  258.41  Angstrom**3



# EOF
