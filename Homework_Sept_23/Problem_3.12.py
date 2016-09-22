#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Sept 23, 2016
#

# Problem 3.12

import sys

#
# Setup path to local modules...
#
sys.path.append( "../modules" )

import numpy
import groupy


# Define the group...
PG3 = [ groupy.g1, groupy.g3_plus, groupy.g3_minus ]

# Print it...
groupy.print_table( PG3 )


# Result:
#
# X |  1      3+     3-     
# ------------------------------
# 1 |  1      3+     3-     
# 3+|  3+     3-     1      
# 3-|  3-     1      3+     
#


## EOF
