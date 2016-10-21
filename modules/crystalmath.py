#!/usr/bin/python
#
#
# BYS 601, Fall 2016
#
# Brett Gossage (bgossgen@gmail.com)
#
# A python module for crystallography computations
#

import math
import numpy


#
# Define conversions between degrees and radians.
#
deg2rad = numpy.pi / 180.0
rad2deg = 180.0 / numpy.pi


#
# A python class for a Unit Cell.
#
class UnitCell:
   
#
# Constructor.
#
   def __init__( self, name="unknown" ):

      self.name = name

      self.a = 0.0 # Angstroms
      self.b = 0.0
      self.c = 0.0

      self.alpha = 0.0 # Radians
      self.beta = 0.0
      self.gamma = 0.0

   # end constructor ~~~~~~~~~~~~~~~~~~~~~~~~

#
# Calculate the G matrix.
#
   def gmatrix( self ):

   # Calculate the basis vectors for the G matrix...
      aa = self.a * self.a  # a dot a
      bb = self.b * self.b
      cc = self.c * self.c

      ab = self.a * self.b * math.cos(self.gamma)  # a dot b
      ac = self.a * self.c * math.cos(self.beta)
      bc = self.b * self.c * math.cos(self.alpha)

      G = numpy.array( [ [aa, ab, ac], [ab, bb, bc], [ac, bc, cc] ])

      return G

   # end method gmatrix ~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# Calculate the volume of this unit cell (Angstroms**3)
#
   def volume( self ):

      G = self.gmatrix()

      detG = numpy.linalg.det(G)

      vol = math.sqrt(detG)

      return vol

   # end method volume ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
#
# Compute the interatomic bond length given the fractional coordinates of two molecules (Angstroms).
#
   def bond_length( self, X1, X2 ):

      X = numpy.subtract( X1, X2 )

   # Note: we are using row vectors so the transpose comes last.

      XG = numpy.dot( X, self.gmatrix() )

      XGXt = numpy.dot( XG, numpy.transpose(X) );

      r12 = math.sqrt( XGXt )

      return r12

   # end method bond_length ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# Compute the interatomic bond angle given the fractional coordinates of three molecules (Degrees).
#
   def bond_angle( self, X1, X2, X3 ):

      X12 = numpy.subtract( X2, X1 )
      X13 = numpy.subtract( X3, X1 )

      r12 = self.bond_length( X1, X2 )
      r13 = self.bond_length( X1, X3 )

   # Note: we are using row vectors so the transpose comes last.

      X12_G = numpy.dot( X12, self.gmatrix() )

      X12_G_X13t = numpy.dot( X12_G, numpy.transpose(X13) );

      cos_theta = X12_G_X13t / (r12 * r13);

      theta = math.acos( cos_theta );

      return theta * rad2deg

   # end method bond_angle ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# Return the cartesian coordinate transform matrix.
#
   def transform( self ):

      cosBeta = math.cos( self.beta )
      cosAlpha = math.cos( self.alpha )
      cosGamma = math.cos( self.gamma )
      sinGamma = math.sin( self.gamma )

      c1 = self.c * cosBeta

      temp = (cosAlpha - cosGamma*cosBeta) / sinGamma

      c2 = self.c * temp

      c3 = self.c * math.sqrt( 1.0 - cosBeta*cosBeta - temp*temp )

      transform = numpy.array( [ [self.a, self.b*cosGamma, c1], [0.0, self.b*sinGamma, c2], [0.0, 0.0, c3] ])

      return transform

   # end method transform ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# end class UnitCell

# EOF

