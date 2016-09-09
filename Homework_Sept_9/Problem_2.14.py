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

P = numpy.array( [ [ 1.0, 1.0, -1.0], [0, 1, 0], [-1, 0, 0] ] )

B2 = numpy.array( [unitCell.a, unitCell.b, unitCell.c ] )

Pinv = numpy.linalg.inv( P )

G2 = unitCell.gmatrix()

print "G2 : ", G2

V2 = unitCell.volume()

print "V2: ", V2

B1 = numpy.matmul( B2, Pinv )

a1 = B1[0]
b1 = B1[1]
c1 = B1[2]

print "a1 = ", a1
print "b1 = ", b1
print "c1 = ", c1

Pinvt = numpy.transpose(Pinv)

PinvtG2 = numpy.matmul( Pinvt, G2 )

G1 = numpy.matmul( PinvtG2, Pinv)

print "G1: ", G1

detP = abs( numpy.linalg.det(P) )

V1 = V2 / detP 

print "V1 = ", V1

# Calculate the lattice parameters...

a1b1 = G1[0,1]
b1c1 = G1[1,2]
a1c1 = G1[0,2]

cosAlpha1 =  b1c1 / b1 * c1
cosBeta1 = a1c1 / a1 * c1
cosGamma1 =  a1b1 / a1 * b1

print "cos(Alpha) = ", cosAlpha1

alpha1 = math.acos( cosAlpha1 )
beta1 = math.acos( cosBeta1 )
gamma1 = math.acos( cosGamma1 )

print "alpha1 = ", alpha1
print "beta1 = ", beta1
print "gamm1 = " , gamma1



# EOF
