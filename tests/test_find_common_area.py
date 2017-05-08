"""
     Title: test_find_common_area.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-06-24
     Description: Unit testing module for find_common_area function in bal.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe


class TestFindCommonArea(unittest.TestCase):

    def test_find_common_area(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                                      os.path.split(
                                      getfile(currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')

        input_folder = os.path.join(testdata_folder, 'input')
        output_folder = os.path.join(testdata_folder, 'output')
        reference_folder = os.path.join(testdata_folder, 'reference')

        veg_r = os.path.join(output_folder, "veg_r")
        slope_r = os.path.join(output_folder, "slope_r")
        aspect_r = os.path.join(output_folder, "aspect_r")

        if not arcpy.Exists(slope_r):
            arcpy.CopyRaster_management(os.path.join(input_folder, "slope_r"),
                              slope_r)

        if not arcpy.Exists(aspect_r):
            arcpy.CopyRaster_management(os.path.join(input_folder, "aspect_r"),
                              aspect_r)

        if not arcpy.Exists(veg_r):
            arcpy.CopyRaster_management(os.path.join(input_folder, "veg_r"),
                              veg_r)

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        veg_expect = os.path.join(reference_folder, "expect_v_c")
        slope_expect = os.path.join(reference_folder, "expect_s_c")
        aspect_expect = os.path.join(reference_folder, "expect_a_c")

        from bal import find_common_area

        veg_c, slope_c, aspect_c = find_common_area(veg_r, slope_r, aspect_r)

        compare_result_veg = os.path.join(output_folder, "compare_veg_c.txt")
        compare_result_slope = os.path.join(output_folder,
                                            "compare_slope_c.txt")
        compare_result_aspect = os.path.join(output_folder,
                                             "compare_aspect_c.txt")

        arcpy.RasterCompare_management(veg_c, veg_expect, '', 'Pyramids Exist', '',
                                       compare_result_veg)
        if '"true"' not in open(compare_result_veg).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        arcpy.RasterCompare_management(slope_c, slope_expect, '', '', '',
                                       compare_result_slope)
        if '"true"' not in open(compare_result_slope).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        arcpy.RasterCompare_management(aspect_c, aspect_expect, '', '', '',
                                       compare_result_aspect)
        if '"true"' not in open(compare_result_aspect).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        if arcpy.Exists(veg_c):
            arcpy.Delete_management(veg_c)
        if arcpy.Exists(slope_c):
            arcpy.Delete_management(slope_c)
        if arcpy.Exists(aspect_c):
            arcpy.Delete_management(aspect_c)

        os.remove(compare_result_veg)
        os.remove(compare_result_slope)
        os.remove(compare_result_aspect)
        os.remove(os.path.join(output_folder, "compare_veg_c.xml"))
        os.remove(os.path.join(output_folder, "compare_slope_c.xml"))
        os.remove(os.path.join(output_folder, "compare_aspect_c.xml"))


if __name__ == "__main__":
    unittest.main()
