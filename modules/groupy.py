#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# 
#

#
# Module for Point Groups in Python
#

import numpy

#
# Define the group matrices.
#

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

g4_plus = numpy.array( [ [0, -1],
                         [1, -1]
                       ]
                     )

g4_minus = numpy.dot( g4_plus, g4_plus )


g4 = numpy.array( [ [0, -1],
                    [1, -1]
                  ]
                )

g6_plus = numpy.array( [ [1, -1],
                         [1, 0]
                       ]
                     )

g6_minus = numpy.array( [ [0, 1],
                          [-1, 1]
                       ]
                     )

#
# Return the name of a element.
#
def name_of( g ):

   if numpy.array_equal( g, g1 ):
      return "1"

   if numpy.array_equal( g, g2 ):
      return "2"

   if numpy.array_equal( g, g3_plus ):
      return "3+"

   if numpy.array_equal( g, g3_minus ):
      return "3-"

   if numpy.array_equal( g, g4_plus ):
      return "4+"

   if numpy.array_equal( g, g4_minus ):
      return "4-"

   if numpy.array_equal( g, g6_plus ):
      return "6+"

   if numpy.array_equal( g, g6_minus ):
      return "6-"

   return "?"

# end name_of() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# Find the identity of a group.
#
def identity_of( group ):

   for g in group:
      for h in group:

         a = numpy.dot(g,h)
         b = numpy.dot(h,g)

         if( numpy.array_equal(a, b) and  numpy.array_equal(h, a) ):
            return g

# endif identity_of() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# Print the multiplication table for a group.
#
def print_table( group ):

   print
   print "X | ",
   for g in group:
      print "{:6s}".format( name_of( g ) ),

   print "\n------------------------------------------------------"

   for g in group:
      print "{:2s}| ".format( name_of( g ) ),
      for h in group:

         m = numpy.dot( g, h )
         print "{:6s}".format( name_of( m ) ),

      print ""

      # end for h

   # end for g
   print
# end print_table() ~~~~~~~~~~~~~~~~~~~~~~~~~~~



## EOF
