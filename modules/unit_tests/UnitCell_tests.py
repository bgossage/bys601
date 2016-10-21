#!/usr/bin/python

"""
UnitCell class unit tests.

Each UnitCell method is tested against expected results from the given inputs.

(Uses the unit test module from the python libraries (similar to JUnit.)

"""

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
   HMB_UnitCell = crystalmath.UnitCell()

   def setUp(self):

      UnitCell_tests.SiO2UnitCell.a = 4.91
      UnitCell_tests.SiO2UnitCell.b = 4.91
      UnitCell_tests.SiO2UnitCell.c = 5.41

      UnitCell_tests.SiO2UnitCell.alpha = 90.0 * crystalmath.deg2rad
      UnitCell_tests.SiO2UnitCell.beta = 90.0 * crystalmath.deg2rad
      UnitCell_tests.SiO2UnitCell.gamma = 120.0 * crystalmath.deg2rad
      
      UnitCell_tests.HMB_UnitCell.a = 9.01
      UnitCell_tests.HMB_UnitCell.b = 8.926
      UnitCell_tests.HMB_UnitCell.c = 5.344

      UnitCell_tests.HMB_UnitCell.alpha = (44+27.0/60.0) * crystalmath.deg2rad
      UnitCell_tests.HMB_UnitCell.beta = (116+43.0/60.0) * crystalmath.deg2rad
      UnitCell_tests.HMB_UnitCell.gamma = (119+34.0/60) * crystalmath.deg2rad

   # end method setUp ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   """ 
      Test the computation of the G matrix from unit cell parameters
   """
   def test_gmatrix( self ):

      G = UnitCell_tests.SiO2UnitCell.gmatrix()

      print "The unit cell G Matrix: \n", G

      tol = 0.01

      self.assertAlmostEqual( G[0,0], 24.11, delta=tol )
      self.assertAlmostEqual( G[0,1], -12.05, delta=tol )

      self.assertAlmostEqual( G[0,2], 0.0, places=7 )
      self.assertAlmostEqual( G[1,2], 0.0, places=7 )
      self.assertAlmostEqual( G[2,0], 0.0, places=7 )
      self.assertAlmostEqual( G[2,1], 0.0, places=7 )

      self.assertAlmostEqual( G[1,1], 24.11, delta=tol )
      self.assertAlmostEqual( G[1,0], -12.05, delta=tol )
      self.assertAlmostEqual( G[2,2], 29.26, delta=tol )

   #end test_gmatrix ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   """ 
      Test the computation of the reciprocal space G-star matrix from unit cell parameters
   """
   def test_gstar_matrix( self ):

      Gstar = UnitCell_tests.HMB_UnitCell.gstar_matrix()

      print "The unit cell Gstar Matrix: \n", Gstar

      tol = 0.01

      self.assertAlmostEqual( Gstar[0,0], 0.0167, delta=tol )
      self.assertAlmostEqual( Gstar[0,1], 0.0059, delta=tol )
      self.assertAlmostEqual( Gstar[0,2], 0.0056, delta=tol )
      
      self.assertAlmostEqual( Gstar[1,0], 0.0059, delta=tol )
      self.assertAlmostEqual( Gstar[1,1], 0.0277, delta=tol )
      self.assertAlmostEqual( Gstar[1,2], -0.0285, delta=tol )

      self.assertAlmostEqual( Gstar[2,0], 0.0056, delta=tol )
      self.assertAlmostEqual( Gstar[2,1], -0.0285, delta=tol )
      self.assertAlmostEqual( Gstar[2,2], 0.0733, delta=tol )

   #end test_gstar_matrix ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   """ 
      Test the computation of the volume from unit cell parameters
   """
   def test_volume( self ):

      V = UnitCell_tests.SiO2UnitCell.volume()

      print "The unit cell volume = ", V

      self.assertAlmostEqual( V, 113.01, delta=0.1 )

   #end test_volume ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   """ 
      Test the computation of the d-spacing from unit cell parameters and a plane
   """
   def test_dspacing( self ):

      unitCell = crystalmath.UnitCell()
      
      unitCell.a = 5.0
      unitCell.b = 6.0
      unitCell.c = 1.0
      
      unitCell.alpha = 90.0 * crystalmath.deg2rad
      unitCell.beta = 90.0 * crystalmath.deg2rad
      unitCell.gamma = 115.0 * crystalmath.deg2rad

      
      h = 2
      k = 1
      l = 0
      
      d = unitCell.d_spacing( h, k, l )

      print "The unit cell d-spacing = ", d

      self.assertAlmostEqual( d, 1.83, delta=0.01 )

   #end test_dspacing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   """ 
      Test the computation of the bond length and angle from Foundations of Crystallography
   """
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
   
   """ 
      Test the computation of the cartesian transform matrix from unit cell parameters.
   """
   def test_transform( self ):
      
      
      
   # HMB Unit Cell Parameters
      hmb_unit_cell = crystalmath.UnitCell()
      
      hmb_unit_cell.a = 9.010;
      hmb_unit_cell.b = 8.926;
      hmb_unit_cell.c = 5.344;


      hmb_unit_cell.alpha = 44.0 + 27.0/60.0;
      hmb_unit_cell.beta = 116.0 + 43.0/60.0;
      hmb_unit_cell.gamma = 119.0 + 34.0/60.0;
      
      hmb_unit_cell.alpha *= crystalmath.deg2rad;
      hmb_unit_cell.beta *= crystalmath.deg2rad;
      hmb_unit_cell.gamma *= crystalmath.deg2rad;

      P = hmb_unit_cell.transform()
      
      print "The HMB cartesian transform matrix: \n", P
      
      tol = 0.01
      
      self.assertAlmostEqual( P[0,0], 9.01, delta=tol )
      self.assertAlmostEqual( P[0,1], -4.4044, delta=tol )
      self.assertAlmostEqual( P[0,2], -2.4025, delta=tol )
      
      self.assertAlmostEqual( P[1,0], 0.0, delta=tol )
      self.assertAlmostEqual( P[1,1], 7.7637, delta=tol )
      self.assertAlmostEqual( P[1,2], 3.0230, delta=tol )

      self.assertAlmostEqual( P[2,0], 0.0, delta=tol )
      self.assertAlmostEqual( P[2,1], 0.0, delta=tol )
      self.assertAlmostEqual( P[2,2], 3.6942, delta=tol )
   
   # end test_transform ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# end class UnitCell_tests

if __name__ == '__main__':
    unittest.main()

# EOF
