#!/usr/bin/python
#
#
# BYS 601
#
# Brett Gossage (bgossgen@gmail.com)
#
# Assignment 1
#

import sys

#
# Ka is the dissociation constant
# 
# pKa = -log( Ka )
#


#
# Define the list of available stock buffers...
#
solutions = { "Tris" : "8.072", 
              "Succinic acid" : "4.207",
              "CABS" : "10.7",
              "KH2PO4" : "7.2"
            }

try:
   print "Available buffers: ", solutions
   
   buffer = "";
   
   while( buffer not in solutions ):
   
   # Get the desired buffer solution...
      buffer = raw_input("Enter a valid buffer: " )

   else:
   # Find the buffer pKa...
      pKa = float( solutions[buffer] )
   
   print
   print "Selected Solution: ", buffer
   print "Solution pKa: ", pKa


# Get desired pH from the user...
   pH = float(raw_input("Enter the desired pH: " ))

   if( abs(pH-pKa) > 1.0 ): raise Exception( "pH is not within +-1.0 of the pKa" );

   print "Desired pH: ", pH

# Get desired volume from the user...
   volume = float(raw_input("Enter the desired volume (mL): " ))
   
   print "Desired volume: ", volume, " (mL)"

#
# NOTE: Assume that the Henderson-Hasselbach equation applies.
#           =>      pH = pKa + log( [A] / [HA] )
#                   A .=. concentration of the conjugate base
#                   HA .=. concentration of the weak acid
#



   

except Exception as err:
   print "An error occured: ", err
   sys.exit( -1 )
except:
   print "Unknown error "
   sys.exit( -1  )

#
# EOF
#