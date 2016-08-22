#!/usr/bin/python
#
#
# BYS 601
#
# Brett Gossage (bgossgen@gmail.com)
#
# Assignment 1
#

#
# Define the list of available stock buffers...
#
solutions = { "Tris" : "8.072", 
              "Succinic acid" : "4.207",
              "CABS" : "10.7"
            }

try:
   print "Available buffers: ", solutions
   
# Get the desired buffer solution...
   buffer = raw_input("Enter the buffer: " )
   
   print "Selected buffer: ", buffer
   print "Selected pKa: ", solutions[buffer]
   
# Find the buffer pKa...
   pKa = float( solutions[buffer] )
   
   print "pKa = ", pKa

# Get desired pH from the user...
   pH = float(raw_input("Enter the desired pH: " ))
   
   if( pH < 0.0 ): raise Exception( "pH must be positive" )

   if( abs(pH-pKa) > 1.0 ): raise Exception( "pH is not within +-1.0 of the pKa" );

   print "Desired pH: ", pH




except Exception as err:
   print "An error occured: ", err
   sys.exit( -1 )
except:
   print "Unknown error "
   sys.exit( -1  )

#
# EOF
#