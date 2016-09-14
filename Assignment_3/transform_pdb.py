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

#
# Open the input file and cleanly handle exceptions.
#
with open( "5dbq.pdb", "r" ) as pdb_file:

   #
   # Open the output file and cleanly handle exception.
   #
   with open( "5dbq_transformed.pdb", "w" ) as output_file:

      for line in pdb_file:

         if line.startswith( ("ATOM","HETATM") ):

          # Get the characters up to the beginning of the data to be transformed...
            prefix = line[0:30]

          # Read the variables...
            x = float( line[31:39] )
            y = float( line[39:47] )
            z = float( line[47:54] )

          # Get the characters after the end of the data to be transformed..
            postfix = line[54:80]

            print "prefix: ", "'", prefix, "'"
            print "postfix: ", "'", postfix, "'"
            print "x =", x
            print "y =", y
            print "z =", z
            
         # Duplicate the prefix data in the output...
            output_file.write( prefix )

         # Write the coordinates...
            output_file.write( str.format( "{:>8.3f}", x)  )
            output_file.write( str.format( "{:>8.3f}", y) )
            output_file.write( str.format( "{:>8.3f}", z) )

         # Duplicate the postfix data in the output...
            output_file.write( postfix )
            output_file.write( "\n" )

         #end if
         else:
            output_file.write( line )

         #end else

      # end for line

   # end with outputfile

# end with pdb_file

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


"""