"""
    Title: test_dist_limit.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing module for DIST_LIMIT_UPSLOPE and
    DIST_LIMIT_DOWNSLOPE dictionary in bal_database.py
"""

import sys
import os.path
import unittest
from inspect import getfile, currentframe


class TestDISTLIMIT(unittest.TestCase):

    def test_dist_limit(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.bal_database import DIST_LIMIT_UPSLOPE
        from utilities.bal_database import DIST_LIMIT_DOWNSLOPE

        others_80 = DIST_LIMIT_UPSLOPE[80]
        downslope_80 = DIST_LIMIT_DOWNSLOPE[80]

        expect_others = {1: [16, 21, 31, 42], 2: [10, 14, 20, 29],
                         3: [7, 9, 13, 19], 4: [10, 13, 19, 27],
                         5: [6, 8, 12, 17], 6: [6, 9, 13, 19],
                         7: [6, 8, 12, 17]}

        expect_downslope = {(2, 1): [20, 27, 37, 50], (2, 2): [13, 17, 25, 35],
                            (2, 3): [7, 10, 15, 22], (2, 4): [11, 15, 22, 31],
                            (2, 5): [7, 9, 13, 20], (2, 6): [8, 11, 17, 24],
                            (2, 7): [7, 9, 14, 20],
                            (3, 1): [26, 33, 46, 61], (3, 2): [16, 22, 31, 43],
                            (3, 3): [8, 11, 17, 25], (3, 4): [12, 17, 24, 35],
                            (3, 5): [7, 10, 15, 23], (3, 6): [11, 15, 22, 31],
                            (3, 7): [8, 10, 16, 23],
                            (4, 1): [33, 42, 56, 73], (4, 2): [21, 28, 39, 53],
                            (4, 3): [9, 13, 19, 28], (4, 4): [14, 19, 28, 39],
                            (4, 5): [8, 11, 18, 26], (4, 6): [14, 19, 28, 39],
                            (4, 7): [9, 12, 18, 26],
                            (5, 1): [42, 52, 68, 87], (5, 2): [27, 35, 48, 64],
                            (5, 3): [10, 15, 22, 31], (5, 4): [15, 21, 31, 43],
                            (5, 5): [9, 13, 20, 29], (5, 6): [18, 25, 36, 48],
                            (5, 7): [10, 14, 21, 30]}

        self.assertEqual(others_80, expect_others)
        self.assertEqual(downslope_80, expect_downslope)


if __name__ == "__main__":
    unittest.main()
