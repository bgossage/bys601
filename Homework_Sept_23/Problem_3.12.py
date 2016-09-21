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

import numpy


g1 = numpy.array( [ [1, 0],
                    [0, 1]
                  ]
                )

g2 = numpy.array( [ [-1, 0],
                    [0, -1]
                  ]
                )

gmy = numpy.array( [ [-1, 0],
                     [0, 1]
                   ]
                 )

gmx = numpy.array( [ [1, 0],
                     [0, -1]
                   ]
                 )

g3_plus = numpy.array( [ [0, -1],
                         [1, -1]
                       ]
                     )

g3_minus = numpy.dot( g3_plus, g3_plus )


def name_of( g ):
   if numpy.array_equal( g, g1 ):
      return "1"

   if numpy.array_equal( g, g3_plus ):
      return "3+"

   if numpy.array_equal( g, g3_minus ):
      return "3-"
   
   return "?"
# end name_of() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_table( group ):

   print
   print "X | ",
   for g in group:
      print "{:6s}".format( name_of( g ) ),
      
   print "\n------------------------------"

   for g in group:
      print "{:2s}| ".format( name_of( g ) ),
      for h in PG3:

         m = numpy.dot( g, h )
         print "{:6s}".format( name_of( m ) ),

      print ""

      # end for h

   # end for g
   print
# end print_table() ~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Define the group...
PG3 = [ g1, g3_plus, g3_minus ]

# Print it...
print_table( PG3 )


# Result:
#
# X |  1      3+     3-     
# ------------------------------
# 1 |  1      3+     3-     
# 3+|  3+     3-     1      
# 3-|  3-     1      3+     
#


## EOF
