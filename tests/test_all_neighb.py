"""
    Title: test_all_neighb.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing for ALL_NEIGHB dictionary in value_lookup.py
"""

import sys
import os.path
import unittest
from inspect import getfile, currentframe


class TestAllNEIGHB(unittest.TestCase):

    def test_all_neighb(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.value_lookup import ALL_NEIGHB

        rows = 10
        cols = 10

        i_list = [1, 3, 5, 7, 9]
        jj_list = [2, 4, 5, 6, 8]
        dire = ['w', 'e', 'n', 's', 'nw', 'ne', 'se', 'sw']

        result_expect = [2, 7, 1, 8, 1, 1, 7, 2, 4, 5, 1, 8, 1, 1, 5, 4, 5, 4,
                         1, 8, 1, 1, 4, 5, 6, 3, 1, 8, 1, 1, 3, 6, 8, 1, 1, 8,
                         1, 1, 1, 8, 2, 7, 3, 6, 2, 3, 6, 2, 4, 5, 3, 6, 3, 3,
                         5, 4, 5, 4, 3, 6, 3, 3, 4, 5, 6, 3, 3, 6, 3, 3, 3, 6,
                         8, 1, 3, 6, 3, 1, 1, 6, 2, 7, 5, 4, 2, 5, 4, 2, 4, 5,
                         5, 4, 4, 5, 4, 4, 5, 4, 5, 4, 5, 4, 4, 4, 6, 3, 5, 4,
                         5, 3, 3, 4, 8, 1, 5, 4, 5, 1, 1, 4, 2, 7, 7, 2, 2, 7,
                         2, 2, 4, 5, 7, 2, 4, 5, 2, 2, 5, 4, 7, 2, 5, 4, 2, 2,
                         6, 3, 7, 2, 6, 3, 2, 2, 8, 1, 7, 2, 7, 1, 1, 2, 2, 7,
                         9, 0, 2, 7, 0, 0, 4, 5, 9, 0, 4, 5, 0, 0, 5, 4, 9, 0,
                         5, 4, 0, 0, 6, 3, 9, 0, 6, 3, 0, 0, 8, 1, 9, 0, 8, 1,
                         0, 0]

        result = []

        for i in i_list:
            for a_j in jj_list:
                for one_dir in dire:
                    neig = ALL_NEIGHB[one_dir](i, a_j, rows, cols)
                    result.append(neig)

        self.assertEqual(result, result_expect)


if __name__ == "__main__":
    unittest.main()
