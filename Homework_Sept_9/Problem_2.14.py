#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 9, 2016
#

# Problem 2.14

import sys

#
# Setup path to crystalmath module...
#
sys.path.append( "../modules" )

from crystalmath import *

# Create a unit cell...
unitCell = UnitCell()

# Unit cell parameters
unitCell.a = 5.3434
unitCell.b = 6.3347
unitCell.c = 8.1513

unitCell.alpha = 104.0589 * deg2rad
unitCell.beta = 99.3386 * deg2rad
unitCell.gamma = 99.3398 * deg2rad

# Get the Pinv transform into array form...
# (Note: Pinv is the transfrom from basis 2 to basis 1)
Pinv = numpy.array( [ [ 1.0, 1.0, -1.0], [0, 1, 0], [-1, 0, 0] ] )

# Calculate the transform matrix...
P = numpy.linalg.inv( Pinv )

# Calculate the G2 matrix...
G2 = unitCell.gmatrix()

print "G2 : ", G2, "\n"

# Calculate V2...
V2 = unitCell.volume()

print "V2: ", V2, "\n"

# Calculate the G1 matrix by applying the transform to G2...

Pinvt = numpy.transpose(Pinv)

PinvtG2 = numpy.dot( Pinvt, G2 )

G1 = numpy.dot( PinvtG2, P)

print "G1: ", G1, "\n"

detP = abs( numpy.linalg.det(P) )

# Calculate the volume

V1 = V2 / detP 

print "V1 = ", V1, "\n"

# Calculate the lattice parameters...

# The square of a1, b1, c1 are on the diagonal of G1...
a1 = math.sqrt( G1[0,0] )
b1 = math.sqrt( G1[1,1] )
c1 = math.sqrt( G1[2,2] )

print "a1 = ", a1
print "b1 = ", b1
print "c1 = ", c1
print "\n"

# The off-diagonal terms contain the angle cosines...
b1_c1_cosAlpha = G1[1,2]
a1_c1_cosBeta = G1[0,2]
a1_b1_cosGamma = G1[0,1]

# Divide out the vector magnitudes to get the angle cosines...
cosAlpha1 =  b1_c1_cosAlpha / (b1 * c1)
cosBeta1 = a1_c1_cosBeta / (a1 * c1)
cosGamma1 =  a1_b1_cosGamma / (a1 * b1)

print "cos(Alpha) = ", cosAlpha1
print "cos(Beta) = ", cosBeta1
print "cos(Gamma) = ", cosGamma1

alpha1 = math.acos( cosAlpha1 )
beta1 = math.acos( cosBeta1 )
gamma1 = math.acos( cosGamma1 )

print "alpha1 = ", alpha1
print "beta1 = ", beta1
print "gamm1 = " , gamma1

# G2 :  [[ 28.55192356  -5.49330364  -7.06771653]
#        [ -5.49330364  40.12842409 -12.54338713]
#        [ -7.06771653 -12.54338713  66.44369169]] 

#V2:  258.169774484 

#  G1:  [[ 73.51140822 -66.46132473  37.89176813]
#        [ 19.61110366  15.02401678  -3.44751625]
#        [ -7.06771653  12.56102018  21.48420703]] 

# V1 =  258.169774484 

# a1 =  8.57387941487
# b1 =  3.87608265932
# c1 =  4.63510593506



# EOF
