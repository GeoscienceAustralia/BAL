"""
    Title: test_find_dist_class.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing for find_dist_class function in calculate_bal.py
"""

import sys
import os.path
import unittest
from inspect import getfile, currentframe


class TestFindDistClass(unittest.TestCase):

    def test_find_dist_class(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))


        if parent not in sys.path:
            sys.path.insert(0, parent)

        from calculate_bal import find_dist_class

        dist_list = [12.5, 37.5, 62.5, 87.5]
        dist_limit_list = [[16, 21, 31, 42],
                           [11, 15, 22, 31],
                           [42, 52, 68, 87]]

        result_expect = [1, 4, 5, 5, 2, 5, 5, 5, 1, 1, 3, 5]

        result = []

        for dist_limit in dist_limit_list:
            for dist in dist_list:
                dist_class = find_dist_class(dist, dist_limit)
                result.append(dist_class)

        self.assertEqual(result, result_expect)


if __name__ == "__main__":
    unittest.main()
