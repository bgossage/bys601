#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# Assignment 3, Sept 14, 2016
#

import sys

sys.path.append( "../modules" )

import math
import numpy
import crystalmath

with open( "5dbq.pdb", "r" ) as pdb_file:

   with open( "5dbq_transformed.pdb", "w" ) as output_file:

      for line in pdb_file:

         if line.startswith( ("ATOM","HETATM") ):

            print "Line:", line

            prefix = line[0:30]
            
            x = float( line[31:39] )
            y = float( line[39:47] )
            z = float( line[47:54] )
            
            postfix = line[54:80]

            print "prefix: ", "'", prefix, "'"
            print "postfix: ", "'", postfix, "'"
            print "x =", x
            print "y =", y
            print "z =", z
            output_file.write( prefix )
            
            output_file.write( str.format( "{:>8.3f}", x)  )
            output_file.write( str.format( "{:>8.3f}", y) )
            output_file.write( str.format( "{:>8.3f}", z) )
            
            output_file.write( postfix )
            output_file.write( "\n" )

         #end if
         else:
            output_file.write( line )

         #end else

      # end for line

   # end with outputfile

# end with pdb_file


#
#Cols.
 #1 - 4
 #ATOM
#or
 #1 - 6
 #HETATM
#7 - 11
 #Atom serial number(i)
#13 - 16
 #Atom name(ii)
#17
 #Alternate location indicator(iii)
#18 - 20
 #Residue name(iv,v)
#22
 #Chain identifier, e.g., A for hemoglobin alpha chain
#23 - 26
 #Residue seq. no.
#27
 #Code for insertions of residues, e.g., 66A, 66B, etc.
#31 - 38 X
 #
#
#39 - 46 Y
 #
 #Orthogonal coordinates  (Angstroms)
#
#47 - 54 Z
 #
#55 - 60
 #Occupancy
#61 - 66
 #Temperature factor(vi)
#68 - 70
 #Footnote number
