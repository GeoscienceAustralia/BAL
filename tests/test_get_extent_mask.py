"""
     Title: test_get_extent_mask.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-06-24
     Description: Unit testing module for get_extent_mask function in bal.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe


class TestGetExtentMask(unittest.TestCase):

    def test_get_extent_mask(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                                      os.path.split(getfile(
                                      currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')
        output_folder = os.path.join(testdata_folder, 'output')
        reference_folder = os.path.join(testdata_folder, 'reference')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True

        mask_expect = os.path.join(reference_folder, "expect_extent_mask.shp")

        from bal import get_extent_mask

        extent = '343000 5850000 347000 5852000 343000 5850000 347000 5852000'

        mask = os.path.join(output_folder, "mask.shp")
        get_extent_mask(extent, mask)

        compare_result_mask = os.path.join(output_folder,
                                            "compare_mask.txt")

        arcpy.FeatureCompare_management(mask, mask_expect, 'Id', '', '', '', '',
                                       '', '', '', '', compare_result_mask)
        if '"true"' not in open(compare_result_mask).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        if arcpy.Exists(mask):
            arcpy.Delete_management(mask)

        os.remove(compare_result_mask)
        os.remove(os.path.join(output_folder, "compare_mask.xml"))


if __name__ == "__main__":
    unittest.main()
