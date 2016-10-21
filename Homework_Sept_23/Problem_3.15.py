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


# Define the initial point group...
PG6 = [ groupy.g2, groupy.g3_plus ]

# Print the multiplication table...
groupy.print_table( PG6 )

# Result:
# X |  2      3+     
# ----------------
# 2 |  1      6-     
# 3+|  6-     3- 

# Add the new elments...
PG6.append( groupy.g1 );
PG6.append( groupy.g3_minus );
PG6.append( groupy.g6_minus );

# Print the multiplication table...
groupy.print_table( PG6 )

# Result:
# X |  2      3+     1      3-     6-     
# -------------------------------------
# 2 |  1      6-     2      6+     3+     
# 3+|  6-     3-     3+     1      6+     
# 1 |  2      3+     1      3-     6-     
# 3-|  6+     1      3-     3+     2      
# 6-|  3+     6+     6-     2      3-

# Add the new elments...
PG6.append( groupy.g6_plus );

# Print the multiplication table...
groupy.print_table( PG6 )

# X |  2      3+     1      3-     6-     6+     
# ------------------------------------------------------
# 2 |  1      6-     2      6+     3+     3-     
# 3+|  6-     3-     3+     1      6+     2      
# 1 |  2      3+     1      3-     6-     6+     
# 3-|  6+     1      3-     3+     2      6-     
# 6-|  3+     6+     6-     2      3-     1      
# 6+|  3-     2      6+     6-     1      3+ 

# No new elements, so we are done.

## EOF
