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
from inspect import getfile, currentframe


class TestBALCLASS(unittest.TestCase):

    def test_bal_class(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.bal_database import BAL_CLASS

        result_expect = {1: 100, 2: 40, 3: 29, 4: 19, 5: 12.5}

        self.assertEqual(BAL_CLASS, result_expect)


if __name__ == "__main__":
    unittest.main()
