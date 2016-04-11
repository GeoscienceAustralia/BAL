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


class TestFindAOI(unittest.TestCase):

    def test_find_aoi(self):

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

        arcpy.CheckOutExtension("spatial")

        dem = os.path.join(input_folder, "dem.img")
        veg = os.path.join(input_folder, "vege.img")

        from bal import find_aoi

        extent_list = ['DEFAULT', 'MAXOF', 'MINOF',
                       '343000 5850000 347000 5852000 343000 5850000 \
                       347000 5852000']

        mask_expect_list = [os.path.join(reference_folder,
                                         "expect_mask_others.shp"),
                            os.path.join(reference_folder,
                                         "expect_mask_others.shp"),
                            os.path.join(reference_folder,
                                         "expect_mask_others.shp"),
                            os.path.join(reference_folder, "expect_mask.shp")]

        index = 0
        for extent in extent_list:
            mask = find_aoi(extent, dem, veg)

            compare_result_mask = os.path.join(input_folder,
                                               "compare_mask_" +
                                               extent + ".txt")

            arcpy.FeatureCompare_management(mask, mask_expect_list[index],
                                            'Id', '', '', '', '', '', '', '',
                                            '', compare_result_mask)
            if '"true"' not in open(compare_result_mask).read():
                self.assertEqual(1, 1, 'No errors')
            else:
                self.assertEqual(1, 0, 'Has errors')

            os.remove(compare_result_mask)
            os.remove(os.path.join(input_folder, "compare_mask_" +
                                               extent + ".xml"))

            if arcpy.Exists(mask):
                arcpy.Delete_management(mask)

            index += 1


if __name__ == "__main__":
    unittest.main()
