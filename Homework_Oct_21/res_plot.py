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

filename = "4H2L_C222.sca"


if( len(sys.argv) > 1 ):
   filename = sys.argv[1] 
   
#end if

print "filename: ", filename

#
# Open the input file and cleanly handle exceptions.
#
with open( filename, "r" ) as sca_file:

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
   
   value_pairs = list()
   
   Inorm = 0.0
   d = 0.0
   
   Ndatums = len(lines)-3
   
   print "Datums = ", Ndatums

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

   # Compute resolution: d = 1 / H.hkl
      d = unitCell.d_spacing( h, k, l )

   # Compute I/sigma...
      Inorm = I / sigma
      

      if Inorm > 3.0 :
         value_pairs.append( [d,Inorm] )

   #end for

   N = len(value_pairs);
   
   print "N = ", N
   
   percent = 100.0 * float(N)/float(Ndatums)
   

   
   print "Percent above threshold: ", percent
   
   x_values = numpy.zeros(N)
   y_values = numpy.zeros(N)
   
   for i in range(0,N):
       x_values[i] = value_pairs[i][0]
       y_values[i] = value_pairs[i][1]
       
   print "Resolution range: [ ", min(x_values), " , ", max(x_values), " ] "
	   
   index_array = numpy.argsort( x_values )

   px_values = x_values[index_array]
   py_values = y_values[index_array]
   
   matplotlib.pyplot.plot( px_values, py_values )
   matplotlib.pyplot.show()
   
   
  
# end with sca_file

# Plot the I/sigma vs resolution d...



 # EOF
 
 