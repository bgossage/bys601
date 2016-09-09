#!/usr/bin/python

import sys

sys.path.append( ".." )


import unittest
import crystalmath
import numpy


class UnitCell_tests( unittest.TestCase ):

# Class variable for SiO2 Unit cell parameters
# from Foundations of Crystallography, Example 2.4 
# 
   SiO2UnitCell = crystalmath.UnitCell()

   def setUp(self):

      UnitCell_tests.SiO2UnitCell.a = 4.91
      UnitCell_tests.SiO2UnitCell.b = 4.91
      UnitCell_tests.SiO2UnitCell.c = 5.41

      UnitCell_tests.SiO2UnitCell.alpha = 90.0 * crystalmath.deg2rad
      UnitCell_tests.SiO2UnitCell.beta = 90.0 * crystalmath.deg2rad
      UnitCell_tests.SiO2UnitCell.gamma = 120.0 * crystalmath.deg2rad

   # end method setUp ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   """ 
      Test the computation of the G matrix from unit cell parameters
   """
   def test_gmatrix( self ):

      G = UnitCell_tests.SiO2UnitCell.gmatrix()

      print "The unit cell G Matrix: \n", G

      self.assertAlmostEqual( G[0,0], 24.11, delta=0.01 )
      self.assertAlmostEqual( G[0,1], -12.05, delta=0.01 )

      self.assertAlmostEqual( G[0,2], 0.0, places=7 )
      self.assertAlmostEqual( G[1,2], 0.0, places=7 )
      self.assertAlmostEqual( G[2,0], 0.0, places=7 )
      self.assertAlmostEqual( G[2,1], 0.0, places=7 )

      self.assertAlmostEqual( G[1,1], 24.11, delta=0.01 )
      self.assertAlmostEqual( G[1,0], -12.05, delta=0.01 )

   #end test_gmatrix ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   """ 
      Test the computation of the volume from unit cell parameters
   """
   def test_volume( self ):

      V = UnitCell_tests.SiO2UnitCell.volume()

      print "The unit cell volume = ", V

      self.assertAlmostEqual( V, 113.01, delta=0.1 )

   #end test_volume ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   def test_bond_properties( self ):

      Xsi_1 = numpy.array( [0.4699, 0.0, 0.0], ndmin=2 )
      Xsi_2 = numpy.array( [0.5301, 0.5301, 0.3333], ndmin=2 )
      Xo    = numpy.array( [0.4141, 0.2681, 0.1188], ndmin=2 )

      L1 = UnitCell_tests.SiO2UnitCell.bond_length( Xsi_1, Xo )

      print "The Si1-O bond length = ", L1

      self.assertAlmostEqual( L1, 1.6067, delta=0.001 )

      L2 = UnitCell_tests.SiO2UnitCell.bond_length( Xsi_2, Xo )

      print "The Si2-O bond length = ", L2

      self.assertAlmostEqual( L2, 1.6102, delta=0.001 )
      
      A = UnitCell_tests.SiO2UnitCell.bond_angle( Xo, Xsi_1, Xsi_2 );
      
      print "The Si1-Si2-O bond angle = ", A
      
      self.assertAlmostEqual( A, 143.46, delta=1.0 )

   #end test_bond_properties ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# end class UnitCell_tests

if __name__ == '__main__':
    unittest.main()

# EOF
