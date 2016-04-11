"""
    Title: test_point_r.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing module for POINT_R dictionary in value_lookup.py
"""

import sys
import os.path
import unittest
from inspect import getfile, currentframe


class TestPointR(unittest.TestCase):

    def test_point_r(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.value_lookup import ALL_NEIGHB, POINT_R

        rows = 10
        cols = 10

        i_list = [1, 3, 5, 7, 9]
        jj_list = [2, 4, 6, 8]

        dire = ['w', 'e', 'n', 's', 'nw', 'ne', 'se', 'sw']

        result_expect = [1, 1, 1, 1, 1, 1, 0, 2, 3, 4, 5, 0, 0, 2, 3, 4, 5, 2,
                         3, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 3, 4, 5, 0, 0, 2, 3,
                         4, 5, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1, 0, 2, 3, 4, 5,
                         0, 0, 2, 3, 4, 2, 3, 4, 5, 1, 1, 1, 1, 1, 0, 2, 3, 4,
                         5, 0, 0, 2, 2, 3, 4, 5, 3, 3, 3, 3, 3, 3, 2, 1, 0, 4,
                         5, 6, 7, 2, 1, 2, 1, 0, 4, 5, 6, 7, 4, 5, 3, 3, 3, 3,
                         3, 3, 3, 3, 2, 1, 0, 4, 5, 6, 7, 2, 1, 0, 2, 1, 0, 4,
                         5, 6, 7, 4, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 4,
                         5, 6, 7, 2, 1, 0, 2, 1, 0, 4, 5, 6, 4, 5, 6, 7, 3, 3,
                         3, 3, 3, 2, 1, 0, 4, 5, 6, 7, 2, 1, 0, 2, 4, 4, 5, 6,
                         7, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9, 4, 3, 4,
                         3, 2, 1, 6, 7, 8, 9, 6, 7, 5, 5, 5, 5, 5, 5, 5, 5, 4,
                         3, 2, 1, 6, 7, 8, 9, 4, 3, 2, 1, 4, 3, 2, 1, 6, 7, 8,
                         9, 6, 7, 8, 9, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1, 6, 7,
                         8, 9, 4, 3, 2, 1, 4, 3, 2, 6, 7, 8, 6, 7, 8, 9, 5, 5,
                         5, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9, 4, 3, 2, 1, 4, 6, 6,
                         7, 8, 9, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 8, 9, 6, 5, 6,
                         5, 4, 3, 8, 9, 8, 9, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4,
                         3, 8, 9, 6, 5, 4, 3, 6, 5, 4, 3, 8, 9, 8, 9, 7, 7, 7,
                         7, 7, 7, 7, 6, 5, 4, 3, 8, 9, 6, 5, 4, 3, 6, 5, 4, 8,
                         9, 8, 9, 7, 7, 7, 7, 7, 6, 5, 4, 3, 8, 9, 6, 5, 4, 3,
                         6, 8, 8, 9, 9, 9, 9, 9, 9, 9, 8, 7, 6, 5, 8, 7, 8, 7,
                         6, 5, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 6, 5, 8, 7, 6, 5,
                         8, 7, 6, 5, 9, 9, 9, 9, 9, 9, 9, 8, 7, 6, 5, 8, 7, 6,
                         5, 8, 7, 6, 9, 9, 9, 9, 9, 8, 7, 6, 5, 8, 7, 6, 5, 8]

        result = []

        for i in i_list:
            for a_j in jj_list:
                for a_dire in dire:
                    all_neighb_dir = ALL_NEIGHB[a_dire](i, a_j, rows, cols)

                    if all_neighb_dir < 4:
                        max_neighb_dir = all_neighb_dir
                    else:
                        max_neighb_dir = 4

                    for a_m in range(1, max_neighb_dir+1):
                        point_row = POINT_R[a_dire](i, a_m)
                        result.append(point_row)

        self.assertEqual(result, result_expect)


if __name__ == "__main__":
    unittest.main()
