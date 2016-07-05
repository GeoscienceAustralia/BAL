"""
     Title: test_findAOI.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-06-24
     Description: Unit testing module for find_aoi function in bal.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe


class TestGetFootPrint(unittest.TestCase):

    def test_get_footprint(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                                      os.path.split(getfile(
                                      currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')
        input_folder = os.path.join(testdata_folder, 'input')
        reference_folder = os.path.join(testdata_folder, 'reference')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True

        veg = os.path.join(input_folder, "vege.img")

        from bal import get_footprint

        footprint_expect = os.path.join(reference_folder,
                                        "expect_footprint.shp")


        footprint = 'footprint.shp'
        get_footprint(veg, footprint)

        compare_result_footprint = os.path.join(input_folder,
                                           "compare_footprint.txt")

        arcpy.FeatureCompare_management(footprint, footprint_expect,
                                        'Id', '', '', '', '', '', '', '',
                                        '', compare_result_footprint)

        if '"true"' not in open(compare_result_footprint).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        os.remove(compare_result_footprint)
        os.remove(os.path.join(input_folder, "compare_footprint.xml"))

        if arcpy.Exists(footprint):
            arcpy.Delete_management(footprint)


if __name__ == "__main__":
    unittest.main()
