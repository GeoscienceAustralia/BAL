"""
    Title: test_get_max_bal.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2016-05-27
    Description: Unit testing for get_max_bal function in calculate_bal.py
"""

import sys
import os.path
import unittest
from inspect import getfile, currentframe
import numpy as np


class TestGetMaxBal(unittest.TestCase):

    def test_get_max_bal(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from calculate_bal import get_max_bal

        a = np.array([[-99., 29., 100., 19.],
                      [-99., 19., 100., -99],
                      [-99., 40., 29., 100.],
                      [-99., 100., 40., -99]])

        b = np.array([[100., 200., 200., 200.],
                      [100., -99, 200., 200.],
                      [100., 100., 100., 29.],
                      [40., 29., 40., -99]])

        c = np.array([[-99., -99., -99., -99.],
                      [-99, 100., -99., 100.],
                      [19, 100., 100, -99],
                      [40., 29., 100., -99]])

        result_expect = np.array([[100., 200., 200., 200.],
                                  [100., 100., 200., 200.],
                                  [100, 100., 100, 100.],
                                  [40., 100., 100., -99]])
                                  
        array_list = [a, b, c]                                  

        result = get_max_bal(array_list)        
        
        np.testing.assert_array_equal(result, result_expect)


if __name__ == "__main__":
    unittest.main()
