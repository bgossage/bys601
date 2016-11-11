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


# Define a list to store the intensity values..
value_pairs = list()

lines = list()

unitCell = crystalmath.UnitCell()

#
# Open the input file and cleanly handle exceptions.
#
with open( filename, "r" ) as sca_file:

# Read all the lines in the file...
   lines = sca_file.readlines()

# end with sca_file

# Extract the unit cell parameters...
cell_params = lines[2].split()

print "Cell Params: ", cell_params

unitCell.a = float( cell_params[0] )
unitCell.b = float( cell_params[1] )
unitCell.c = float( cell_params[2] )
unitCell.alpha = float( cell_params[3] )
unitCell.beta = float( cell_params[4] )
unitCell.gamma = float( cell_params[5] )

Inorm = 0.0
d = 0.0


ranges = list()

d_low = 0.6
d_high = 3.0;


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

   if d > d_low and d < d_high:
      value_pairs.append( [d,Inorm] )

#end for i


# Sort the values on d-spacing...
value_pairs.sort( key = lambda pair : pair[0] ) 

num_values = len(value_pairs)

print "N = ", num_values
   
d_values = numpy.zeros(num_values)
i_values = numpy.zeros(num_values)

# Pull the data pairs into separate arrays...
i = 0
for datum in value_pairs:
   d_values[i] = datum[0]
   i_values[i] = datum[1]
   i += 1

# We need to create resolution bins at reasonable intervals,
# so use a histogram algorithm to get good looking results...

num_res = 40  # The number of resolution histogram bins
num_thr = 6   # The number of threshold histogram bins

# Compute histogram bins for the resolution d-values...
[hist,d_bin_edges] = numpy.histogram( d_values, bins=num_res )

num_res = len(d_bin_edges) - 1

# Compute the intensity histogram bins...
[hist,thr_bin_edges] = numpy.histogram( i_values, bins=num_thr )

resolutions = list()

# Store the bounds of each resolution bin as pairs in a list...
for k in range(0,num_res):
   resolutions.append( [d_bin_edges[k] , d_bin_edges[k+1]] )

# Define the thresholds as the upper bound of each bin...
thresholds = list()

for k in range(1,num_thr):
   threshold = thr_bin_edges[k]
   thresholds.append( threshold )

# Compute for Intensity threshold...
for threshold in thresholds:

   i = 0

   x_values = numpy.zeros(num_res)
   y_values = numpy.zeros(num_res)

   # Filter the data based on resolution bin and intensity threshold...
   for res in resolutions:

      res_low = res[0]
      res_high = res[1]

      res_center = (res_low + res_high) / 2.0 # The center of this bin

      Ndatums = 0

      for datum in value_pairs:
         d = datum[0]
         Inorm = datum[1]

         # Screen based on resolution bin...
         if d >= res_low and d<=res_high:

            # Screen based on noise-weighted intensity range...
            if Inorm > threshold:
               Ndatums += 1

         #end if d

      #end for datum

      # Compute the percent of samples that pass filtering...
      percent = 100.0 * float(Ndatums) / float(num_values)

      # The bin center value is the x value.
      # The percent passing is the y value.
      x_values[i] = res_center
      y_values[i] = percent

      i += 1

   #end for resolution


# Plot the current density curve ...
   plot_label = "I/sigma > " + "{:3.1f}".format( threshold )

   matplotlib.pyplot.plot( x_values, y_values, label=plot_label )

#end for threshold


## Show the density vs resolution functions...
matplotlib.pyplot.legend( loc='upper right' )
matplotlib.pyplot.xlabel( 'd spacing' )
matplotlib.pyplot.ylabel( 'percent' )
matplotlib.pyplot.title( 'Information Densities' )
matplotlib.pyplot.show()





 # EOF
 
 