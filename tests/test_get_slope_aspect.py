"""
     Title: test_get_slope_aspect.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-06-24
     Description: Unit testing module for get_slope_aspect function in bal.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe


class TestGetSlopeAspect(unittest.TestCase):

    def test_get_slope_aspect(self):

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
        slope_expect = os.path.join(reference_folder, "expect_s_r")
        aspect_expect = os.path.join(reference_folder, "expect_a_r")

        from bal import get_slope_aspect

        output_folder = os.path.join(testdata_folder, 'output')
        mask = dem

        slope, aspect = get_slope_aspect(dem, output_folder, mask)

        compare_result_slope = os.path.join(output_folder,
                                            "compare_slope_r.txt")
        compare_result_aspect = os.path.join(output_folder,
                                             "compare_aspect_r.txt")

        arcpy.RasterCompare_management(slope, slope_expect, '', '', '',
                                       compare_result_slope)
        if '"true"' not in open(compare_result_slope).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        arcpy.RasterCompare_management(aspect, aspect_expect, '', '', '',
                                       compare_result_aspect)
        if '"true"' not in open(compare_result_aspect).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        if arcpy.Exists(slope):
            arcpy.Delete_management(slope)

        if arcpy.Exists(aspect):
            arcpy.Delete_management(aspect)

        os.remove(compare_result_slope)
        os.remove(os.path.join(output_folder, "compare_slope_r.xml"))
        os.remove(compare_result_aspect)
        os.remove(os.path.join(output_folder, "compare_aspect_r.xml"))


if __name__ == "__main__":
    unittest.main()
