"""
    Title: test_point_c.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing module for POINT_C dictionary in value_lookup.py
"""

import sys
import os.path
import unittest
from inspect import getfile, currentframe


class TestPointC(unittest.TestCase):

    def test_point_c(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.value_lookup import ALL_NEIGHB, POINT_C

        rows = 10
        cols = 10

        i_list = [1, 3, 5, 7, 9]
        jj_list = [2, 4, 6, 8]

        dire = ['w', 'e', 'n', 's', 'nw', 'ne', 'se', 'sw']

        result_expect = [1, 0, 3, 4, 5, 6, 2, 2, 2, 2, 2, 1, 3, 3, 4, 5, 6, 1,
                         0, 3, 2, 1, 0, 5, 6, 7, 8, 4, 4, 4, 4, 4, 3, 5, 5, 6,
                         7, 8, 3, 2, 1, 0, 5, 4, 3, 2, 7, 8, 9, 6, 6, 6, 6, 6,
                         5, 7, 7, 8, 9, 5, 4, 3, 2, 7, 6, 5, 4, 9, 8, 8, 8, 8,
                         8, 7, 9, 9, 7, 6, 5, 4, 1, 0, 3, 4, 5, 6, 2, 2, 2, 2,
                         2, 2, 2, 1, 0, 3, 4, 5, 3, 4, 5, 6, 1, 0, 3, 2, 1, 0,
                         5, 6, 7, 8, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 5, 6, 7, 5,
                         6, 7, 8, 3, 2, 1, 0, 5, 4, 3, 2, 7, 8, 9, 6, 6, 6, 6,
                         6, 6, 6, 5, 4, 3, 7, 8, 9, 7, 8, 9, 5, 4, 3, 2, 7, 6,
                         5, 4, 9, 8, 8, 8, 8, 8, 8, 8, 7, 6, 5, 9, 9, 7, 6, 5,
                         4, 1, 0, 3, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 3,
                         4, 5, 6, 3, 4, 5, 6, 1, 0, 3, 2, 1, 0, 5, 6, 7, 8, 4,
                         4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0, 5, 6, 7, 8, 5, 6, 7,
                         8, 3, 2, 1, 0, 5, 4, 3, 2, 7, 8, 9, 6, 6, 6, 6, 6, 6,
                         6, 6, 5, 4, 3, 2, 7, 8, 9, 7, 8, 9, 5, 4, 3, 2, 7, 6,
                         5, 4, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 6, 5, 4, 9, 9, 7,
                         6, 5, 4, 1, 0, 3, 4, 5, 6, 2, 2, 2, 2, 2, 2, 1, 0, 3,
                         4, 5, 6, 3, 4, 1, 0, 3, 2, 1, 0, 5, 6, 7, 8, 4, 4, 4,
                         4, 4, 4, 3, 2, 1, 0, 5, 6, 7, 8, 5, 6, 3, 2, 5, 4, 3,
                         2, 7, 8, 9, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 7, 8, 9, 7,
                         8, 5, 4, 7, 6, 5, 4, 9, 8, 8, 8, 8, 8, 8, 7, 6, 5, 4,
                         9, 9, 7, 6, 1, 0, 3, 4, 5, 6, 2, 2, 2, 2, 1, 0, 3, 4,
                         5, 6, 3, 2, 1, 0, 5, 6, 7, 8, 4, 4, 4, 4, 3, 2, 1, 0,
                         5, 6, 7, 8, 5, 4, 3, 2, 7, 8, 9, 6, 6, 6, 6, 5, 4, 3,
                         2, 7, 8, 9, 7, 6, 5, 4, 9, 8, 8, 8, 8, 7, 6, 5, 4, 9]

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
                        point_col = POINT_C[a_dire](a_j, a_m)
                        result.append(point_col)

        self.assertEqual(result, result_expect)


if __name__ == "__main__":
    unittest.main()
