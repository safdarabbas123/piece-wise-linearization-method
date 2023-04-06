# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:38:20 2023

@author: sabbas
"""

import numpy as np
import unittest
from my_functions import nonlinear_function, piecewise_linearization

class TestNonlinearFunction(unittest.TestCase):

    def test_nonlinear_function(self):
        # Test case 1
        x1 = np.pi/2
        expected_output1 = np.sin(x1) + np.abs(x1)
        self.assertAlmostEqual(nonlinear_function(x1), expected_output1, places=6)

        # Test case 2
        x2 = 0
        expected_output2 = np.sin(x2) + np.abs(x2)
        self.assertAlmostEqual(nonlinear_function(x2), expected_output2, places=6)

        # Test case 3
        x3 = -np.pi/4
        expected_output3 = np.sin(x3) + np.abs(x3)
        self.assertAlmostEqual(nonlinear_function(x3), expected_output3, places=6)

class TestPiecewiseLinearization(unittest.TestCase):

    def test_piecewise_linearization(self):
        # Test case 1
        x1 = 3.5
        segments1 = [(2, 5), (0, 2), (-3, 0), (-5, -3)]
        expected_output1 = piecewise_linearization(x1, segments1)
        self.assertAlmostEqual(piecewise_linearization(x1, segments1), expected_output1, places=6)

        # Test case 2
        x2 = -2.5
        segments2 = [(2, 5), (0, 2), (-3, 0), (-5, -3)]
        expected_output2 = piecewise_linearization(x2, segments2)
        self.assertAlmostEqual(piecewise_linearization(x2, segments2), expected_output2, places=6)

        # Test case 3
        x3 = 1
        segments3 = [(-5, -3), (-3, 0), (0, 2), (2, 5)]
        expected_output3 = piecewise_linearization(x3, segments3)
        self.assertAlmostEqual(piecewise_linearization(x3, segments3), expected_output3, places=6)

if __name__ == '__main__':
    unittest.main()
