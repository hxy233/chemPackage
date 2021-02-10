import unittest
from chemPackage import collect
import numpy as np
from numpy.testing import assert_array_almost_equal

class TestADFMethods(unittest.TestCase):
    def setUp(self):
        self.test = collect('unitTests/h2o_pol.out')

    def test_Orbital(self):
        orbE = np.array([-25.34, -13.259, -9.557, -7.398, -0.228, 2.232])
        np.testing.assert_array_almost_equal(self.test.orbital_energies, orbE)
        occ = np.array([2., 2., 2., 2., 0., 0.])
        np.testing.assert_array_almost_equal(self.test.orbital_occ, occ)
        spin = np.array([0, 0, 0, 0, 0, 0])
        np.testing.assert_array_almost_equal(self.test.orbital_spin, spin)