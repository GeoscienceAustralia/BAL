"""
    Title: test_bal_class.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing module for BAL_CLASS dictionary in
    bal_database.py
"""

import sys
import os.path
import unittest
import numpy as np
from inspect import getfile, currentframe


class TestCLIPARRAY(unittest.TestCase):

    def test_clip_array(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.sa_tools import clip_array
        
        pixelwidth = 30
        pixelheight = 30

        x_left = 395
        y_upper = 849

        extent_list = [[494.89, 748.21, 584.20, 838.35],
                       [484.25, 768.78, 565.88, 851.64],
                       [485.00, 759.00, 575.00, 849.00]]

        expected = np.array([[3,  4, 5],
                             [10, 11, 12],
                             [17, 18, 19]])

        data = np.arange(49).reshape(7, 7)

        for extent in extent_list:

            data_clip = clip_array(data, x_left, y_upper, pixelwidth,
                                   pixelheight, extent)
                                       
            np.testing.assert_array_equal(expected, data_clip)



if __name__ == "__main__":
    unittest.main()
