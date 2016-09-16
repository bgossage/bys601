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

#
# Setup path to crystalmath module...
#
sys.path.append( "../modules" )

import math
import numpy
import crystalmath

atomic_wts = { "C" :  12.0,
               "N" :  14.0,
               "O" :  16.0,
               "S" :  32.0
             }


# Unit cell paramters for oxidoreductase RCSB 5DBQ
# Crystal structure of insect thioredoxin at 1.95 angstroms
unitCell = crystalmath.UnitCell()

unitCell.a = 107.710
unitCell.b = 28.980
unitCell.c = 79.860

unitCell.alpha = 90.00 * crystalmath.deg2rad
unitCell.beta = 128.32 * crystalmath.deg2rad
unitCell.gamma = 90.00 * crystalmath.deg2rad

#
# Convert crystallographic coordinates to fractional.
#
def to_fractional( x, y, z ):
   
   X = numpy.array( [ [x], [y], [z] ] )
#
# SCALEX matrix for oxidoreductase (RCSB: 5DBQ) (insect thioredoxin)
#
   M = numpy.array([ [0.009284, 0.000000, 0.007337],
                     [0.000000, 0.034507,  0.000000],
                     [0.000000, 0.000000,  0.015960] 
                   ])
   
   NewX = numpy.matmul(M,X)
   
   return NewX

# end method to_fractional ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#
# Convert fractional coordinates to cartesian
def to_cartesian( x, y, z ):

   X = numpy.array( [ [x], [y], [z] ] )

   M = unitCell.transform()

   NewX = numpy.matmul(M,X)

   return NewX

# end method to_cartesian ~~~~~~~~~~~~~~~~~~~~~~~~~

xavg = -49.1559084967
yavg = -34.3433611111
zavg = 78.4634820261
N = 0
MW = 0.0

#
# Open the input file and cleanly handle exceptions.
#
with open( "5dbq.pdb", "r" ) as pdb_file:

#
# Open the output file and cleanly handle exceptions.
#
   with open( "5dbq_transformed.pdb", "w" ) as output_file:

      for line in pdb_file:

         if line.startswith( ("ATOM","HETATM") ):

            element = line[77:78]

            atomic_wt = atomic_wts[element]

            MW += atomic_wt

         # Get the characters up to the beginning of the data to be transformed...
            prefix = line[0:30]

         # Read the variables...
            x = float( line[30:38] )
            y = float( line[38:46] )
            z = float( line[46:54] )

         # Shift the centroid to the origin...
            x -= xavg
            y -= yavg
            z -= zavg

 #           xavg += x
 #           yavg += y
 #           zavg += z
 #           N += 1

         # Convert to fractional coordinates...
            A =  to_fractional( x, y, z )

            xf = A[0,0]
            yf = A[1,0]
            zf = A[2,0]

         # Convert to cartesian coordinates...
            A =  to_cartesian( xf, yf, zf )

            xc = A[0,0]
            yc = A[1,0]
            zc = A[2,0]

         # Shift to the center of the  unit cell...
            x += unitCell.a * 0.5
            y += unitCell.b * 0.5
            z += unitCell.c * 0.5

         # Get the characters after the end of the data to be transformed..
            postfix = line[54:80]

         # Duplicate the prefix data in the output...
            output_file.write( prefix )

         # Write the coordinates...
            output_file.write( str.format( "{:8.3f}", x)  )
            output_file.write( str.format( "{:8.3f}", y) )
            output_file.write( str.format( "{:8.3f}", z) )

         # Duplicate the postfix data in the output...
            output_file.write( postfix )
            output_file.write( "\n" )

         #end if
         else:
         # Otherwise, duplicate all other lines in the output...
            output_file.write( line )

         #end else

      # end for line

   # end with outputfile

# end with pdb_file

print "Molecular Weight: ", MW

volume = 195573.43  # cubic angstroms

# Matthew's number from the PDB File: 2.02
Vm = 2.02

Mass = volume / Vm

num_molecules = Mass / MW;

print "num_molecules = ", num_molecules

print "Vm = ", Vm

# Molecular Weight:  24972.0
# Vm =  7.83170871376

# NOTE: uncomment to get the centroid

#xavg /= float(N)
#yavg /= float(N)
#zavg /= float(N)

#print "centroid: ", xavg, yavg, zavg

"""
ATOM Record Format

COLUMNS        DATA  TYPE    FIELD        DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name   "ATOM  "
 7 - 11        Integer       serial       Atom  serial number.
13 - 16        Atom          name         Atom name.
17             Character     altLoc       Alternate location indicator.
18 - 20        Residue name  resName      Residue name.
22             Character     chainID      Chain identifier.
23 - 26        Integer       resSeq       Residue sequence number.
27             AChar         iCode        Code for insertion of residues.
31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
55 - 60        Real(6.2)     occupancy    Occupancy.
61 - 66        Real(6.2)     tempFactor   Temperature  factor.
77 - 78        LString(2)    element      Element symbol, right-justified.
79 - 80        LString(2)    charge       Charge  on the atom.

ref:  http://www.wwpdb.org/documentation/file-format-content/format33/sect9.html#ATOM

"""
