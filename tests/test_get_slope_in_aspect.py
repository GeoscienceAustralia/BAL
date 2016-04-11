"""
    Title: test_get_slope_in_aspect.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-01
    Description: Unit testing module for get_slope_in_aspect function
    in calculate_bal.py
"""

import sys
import os.path
import unittest
import numpy as np
from inspect import getfile, currentframe
from numpy.testing import assert_array_equal


class TestGetSlopeInAspect(unittest.TestCase):

    def test_get_slope_in_aspect(self):

        slope_exp_w =  np.array([[1., 2., -99., 4., 5., 6., 5., -1.],
                                 [1., 2., 3., 4., 5., 6., 1., 2.],
                                 [3., 3., 5., 4., 4., 5., 4., 4.],
                                 [5., 5., -1., 2., -99., 2., 3., 1.],
                                 [-99., 2., 3., -1., 2., 3., 2., 3.],
                                 [2., 3., 3., 3., 3., 3., 3., 3.],
                                 [4., 3., 3., 4., 4., 4., 4., 5.],
                                 [4., 4., 1., 3., 4., 5., 6., -99.]])

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from calculate_bal import get_slope_in_aspect

        slope_data =  np.array([[ 1., 2.,  -99., 4., 5., 6., 5., 5.],
                                [ 1., 2.,  3.,  4., 5., 6., 1., 2.],
                                [ 3., 3., 5., 4., 4., 5., 4., 4.],
                                [ 5., 5., 6., 2., -99., 2., 3., 1.],
                                [-99., 2.,  3., 5., 2., 3., 2., 3.],
                                [  2., 3.,  3., 3., 3., 3., 3., 3.],
                                [ 4., 3., 3., 4., 4., 4., 4., 5.],
                                [ 4., 4., 1., 3., 4., 5., 6., -99.]])

        aspect_data = np.array([[7., 7., 7., 7., 7., 7., 7., 9.],
                                [7., 7., 7., 7., 7., 7., 7., 7.],
                                [7., 7., 7., 7., 7., 7., 7., 7.],
                                [7., 7., 1., 7., 2., 7., 7., 7.],
                                [3., 7., 7., 4., 7., 7., 7., 7.],
                                [7., 7., 7., 7., 7., 7., 7., 7.],
                                [7., 7., 7., 7., 7., 7., 7., 7.],
                                [7., 7., 7., 7., 7., 7., 7., 7.]])

        aspect_value = 7
        rows = 8
        cols = 8

        slope_in_w = get_slope_in_aspect(slope_data, aspect_data, rows, cols,
                                         aspect_value)

        assert_array_equal(slope_in_w, slope_exp_w)


if __name__ == "__main__":
    unittest.main()

