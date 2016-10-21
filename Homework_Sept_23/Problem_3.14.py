#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 23, 2016
#

# Problem 3.14

import sys

#
# Setup path to local modules...
#
sys.path.append( "../modules" )

import numpy
import groupy


# Define the point group...
PG6 = [ groupy.g1, groupy.g2, groupy.g3_plus, groupy.g3_minus, groupy.g6_minus, groupy.g6_plus ]

print "Matrix 6- : ", groupy.g6_minus

# Print the multiplication table...
groupy.print_table( PG6 )

I = groupy.identity_of( PG6 )

print "Identity = ", groupy.name_of( I )

# Find and print the inverse for each matrix...
for g in PG6:
   for h in PG6:
      elem = numpy.dot(g,h)
      if numpy.array_equal(elem,I):
         print "\n inverse of ", groupy.name_of(g), " = ", groupy.name_of( h )



# Results:

# Matrix 6- :  [ 0  1]
#              [-1  1]

# Identity =  1

#
# The multiplication table for point group 6...
#
# X |  1      2      3+     3-     6-     6+     
# --------------------------------------
# 1 |  1      2      3+     3-     6-     6+     
# 2 |  2      1      6-     6+     3+     3-     
# 3+|  3+     6-     3-     1      6+     2      
# 3-|  3-     6+     1      3+     2      6-     
# 6-|  6-     3+     6+     2      3-     1      
# 6+|  6+     3-     2      6-     1      3+

# inverse of  1  =  1

# inverse of  2  =  2

# inverse of  3+  =  3-

# inverse of  3-  =  3+

# inverse of  6-  =  6+

# inverse of  6+  =  6-




## EOF
