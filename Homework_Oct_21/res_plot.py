#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Homework, Oct 21, 2016
#

import sys

#
# Setup path to crystalmath module...
#
sys.path.append( "../modules" )

import math
import numpy
import matplotlib.pyplot
import crystalmath


#
# Open the input file and cleanly handle exceptions.
#
with open( "4H2L_C222.sca", "r" ) as sca_file:

   lines = sca_file.readlines()
   
   cell_params = lines[2].split()
   
   print "Cell Params: ", cell_params
   
   unitCell = crystalmath.UnitCell()
   
   unitCell.a = float( cell_params[0] )
   unitCell.b = float( cell_params[1] )
   unitCell.c = float( cell_params[2] )
   unitCell.alpha = float( cell_params[3] )
   unitCell.beta = float( cell_params[4] )
   unitCell.gamma = float( cell_params[5] )
   
   N = len(lines) - 3;
   
   x_values = numpy.zeros(N)
   y_values = numpy.zeros(N)
   
   count = 0

   for i in range( 3, len(lines) ):
      
   # Read h  k  l  I  sigma...

  #    print lines[i]
      
      tokens = lines[i].split();
      
      if len(tokens) == 0 : break
   
      h = float( tokens[0] )
      k = float( tokens[1] )
      l = float( tokens[2] )
      
      I = float( tokens[3] )
      sigma = float( tokens[4] )

   
   # Compute resolution: d = 1 / H.hkl...
      d = unitCell.d_spacing( h, k, l )
      
      x_values[count] = d
   
   # Compute I/sigma...
      Inorm = I / sigma
      
      y_values[count] = Inorm
      
      print d, " ", Inorm
   
   # Store in array for plotting...

      count += 1

   #end for
   
   index_array = numpy.argsort( x_values )

   px_values = x_values[index_array]
   py_values = y_values[index_array]

   
   matplotlib.pyplot.plot( px_values, py_values )
   matplotlib.pyplot.show()
   
   
  
# end with sca_file

# Plot the I/sigma vs resolution d...



 # EOF
 
 