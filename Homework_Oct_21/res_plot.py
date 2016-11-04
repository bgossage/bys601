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

# Read all the lines in the file...
   lines = sca_file.readlines()

# Extract the unit cell parameters...
   cell_params = lines[2].split()
   
   print "Cell Params: ", cell_params
   
   unitCell = crystalmath.UnitCell()
   
   unitCell.a = float( cell_params[0] )
   unitCell.b = float( cell_params[1] )
   unitCell.c = float( cell_params[2] )
   unitCell.alpha = float( cell_params[3] )
   unitCell.beta = float( cell_params[4] )
   unitCell.gamma = float( cell_params[5] )

# Defne a list to store the values that pass screening...
   value_pairs = list()
   
   Inorm = 0.0
   d = 0.0
   
   Ndatums = 0
   

   threshold = 5.0
   
   thresholds = [ 1.0, 2.0, 3.0, 5.0, 10.0, 15.0 ]
   
   ranges = [ [29.44,10.6196],
              [4.38, 3.48],
              [3.48, 3.03]
            ]


# Process each scatter data line...
   for i in range( 3, len(lines) ):
      
   # Read h  k  l  I  sigma...
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

   # Screen based on desired resolution range...
      res_low = ranges[0][1]; res_high = ranges[0][0]

      #if d >= res_low and d <= res_high :
      Ndatums += 1

   # Screen based on noise-weighted intensity threshold.
      if Inorm > threshold :
         #print h, " ", k, " ", l, " | ", d, "   ", I, " ", sigma, " : ", Inorm
         value_pairs.append( [d,Inorm] )

   #end for
   
# Sort the values on d-spacing...
   value_pairs.sort( key = lambda pair : pair[0] ) 

   N = len(value_pairs)

   print "N = ", N

   print "Datums = ", Ndatums

   percent = 100.0 * float(N)/float(Ndatums)

   print "Percent within Res. range: ", percent

   x_values = numpy.zeros(N)
   y_values = numpy.zeros(N)

   for i in range(0,N):
      x_values[i] = value_pairs[i][0]
      y_values[i] = value_pairs[i][1]

   print "Resolution range: [ ", min(x_values), " , ", max(x_values), " ] "

   matplotlib.pyplot.plot( x_values, y_values )
   matplotlib.pyplot.show()


# end with sca_file

# Plot the I/sigma vs resolution d...



 # EOF
 
 