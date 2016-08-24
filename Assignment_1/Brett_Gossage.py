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
import math

#
# Define a function to prompt for an input string with a default value.
# 
def input_string( prompt, default ) :
   try:
      
     msg = prompt + "(" + str(default) + "): "
      
     ans =  raw_input(msg)
     
     if( not ans ):
        return default
     
     return ans;
      
   except EOFError:
      return str(default)

#
# Define a function to prompt for an input float with a default value.
# 
def input_float( prompt, default ) :
   
    return float( input_string( prompt, str(default) ) )


#
# NOTE: Ka is the dissociation constant
# 
# pKa = -log( Ka )
#


#
# Define the list of available stock buffer solutions...
#          name                  pKa     molarity
stock = { "Tris" :             ("8.072", "0.1"), 
          "Succinic acid" :    ("4.207", "1.0"),
          "CABS" :             ("10.7",  "0.1"),
          "KH2PO4" :           ("7.2",   "0.1")
        }

try:
   print "Available buffers: ", stock
   
   buffer = "";
   
   while( buffer not in stock ):
   
   # Get the desired buffer solution...
      buffer = input_string( "Enter a valid buffer: ", default="KH2PO4" )

   else:
   # Find the buffer pKa...
      pKa = float( stock[buffer][0] )
      
   
   print
   print "Selected Solution: ", buffer
   print "Solution pKa: ", pKa


# Get desired pH from the user...
   pH = input_float("Enter the desired pH: ", default=7.4 )

   if( abs(pH-pKa) > 1.0 ): raise Exception( "pH is not within +-1.0 of the pKa" )

   print "Desired pH: ", pH
   
# Get the molarity of the conjugate base...
   base = input_float( "Enter the concentration of the base (mM): ", default=0.25 )
   
#
# NOTE: Assume that the Henderson-Hasselbach equation applies.
#           =>      pH = pKa + log10( [A] / [HA] )
#                   A .=. concentration of the conjugate base
#                   HA .=. concentration of the weak acid
#
   
# => [A] / [HA] = 10.0 ** ( pH - pKa)

   ratio = math.pow( 10.0, pH - pKa );
   
   print "Ratio of [A] to [HA]: ", ratio

# Get desired volume from the user...
   volume = input_float("Enter the desired volume (L): ",  default=.01 )
   
   print "Desired volume: ", volume, " (L)"
   
# Get desired molarity from the user...
   molarity = input_float("Enter the desired molarity (M): ",  default=0.01 )
   
   print "Desired molarity: ", molarity, " (M)"

# Calculate the fraction of each buffer component...
   A_fraction = ratio / ( 1.0 + ratio );
   
   print "A = ",  A_fraction
   
   HA_fraction = 1.0 / (1.0 + ratio);
   
   print "HA = ", HA_fraction

# Find the molarity of each component...
   M_A = molarity * A_fraction;
   M_HA = molarity * HA_fraction;
  
   print "Molarity of A = ", M_A, " M"
   print "Molarity of HA = ", M_HA, " M"

# Calculate the moles of each component...
   Moles_A = M_A * volume
   Moles_HA = M_HA * volume
   
   print "Moles of A = ", Moles_A, " moles"
   print "Moles of HA = ", Moles_HA, " moles"
   
# Calculate the volume of each stock solution...
   Liters_A = Moles_A / base
   Liters_HA = Moles_HA / float(stock[buffer][1])
   
   print "Liters A: ", Liters_A * 1e6, "uL"
   print "Liters_HA: ", Liters_HA * 1e6, "uL"
   

except Exception as err:
   print "An error occured: ", err
   sys.exit( -1 )
except:
   print "Unknown error "
   sys.exit( -1  )

#
# EOF
#