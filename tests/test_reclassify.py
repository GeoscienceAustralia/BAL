"""
    Title: test_reclassify.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2016-06-28
    Description: Unit testing module for reclassify function in sa_tools.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe


class TestReclassify(unittest.TestCase):

    def test_reclassify(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                     os.path.split(getfile(currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')

        input_folder = os.path.join(testdata_folder, 'input')
        reference_folder = os.path.join(testdata_folder, 'reference')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = input_folder

        output_folder = os.path.join(testdata_folder, 'output')
        reclassify_result = os.path.join(output_folder, 'reclassi')

        from utilities.sa_tools import reclassify

        # test 1st case with vegetation
        veg = os.path.join(input_folder, "vege.img")
        reclassify_expect = os.path.join(reference_folder, "expect_r_1")

        remap = "1 3;2 2;3 3;4 5 7;6 8 1;9 2;10 3;11 12 1;13 1;14 3;\
                 15 6;16 7;17 3;18 19 2;20 7;21 3;22 2; 23 24 7;25 27 5;\
                 28 2;29 30 7;31 3;32 33 1;34 7;35 3;36 37 7;38 4;39 7;40 1;\
                 41 2;42 7;43 2;44 7;45 4;46 7;47 NODATA;97 2;98 99 1"

        reclassify(veg, remap, reclassify_result)

        compare_result = os.path.join(output_folder, "compare_reclassify.txt")

        arcpy.RasterCompare_management(reclassify_result, reclassify_expect,
                                       '', '', '', compare_result)

        if '"true"' not in open(compare_result).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        # delete output files
        if arcpy.Exists(reclassify_result):
            arcpy.Delete_management(reclassify_result)

        os.remove(compare_result)
        os.remove(os.path.join(output_folder, "compare_reclassify.xml"))

        # test 2nd case with slope
        slope = os.path.join(input_folder, "slope_in")
        reclassify_expect = os.path.join(reference_folder, "expect_r_2")

        remap = "0 0 1;0.0001 5 2;5.0001 10 3;10.0001 15 4;\
                15.0001 20 5;20.0001 20 6"

        reclassify(slope, remap, reclassify_result)

        compare_result = os.path.join(output_folder, "compare_reclassify.txt")

        arcpy.RasterCompare_management(reclassify_result, reclassify_expect,
                                       '', '', '', compare_result)

        if '"true"' not in open(compare_result).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        # delete output files
        if arcpy.Exists(reclassify_result):
            arcpy.Delete_management(reclassify_result)

        os.remove(compare_result)
        os.remove(os.path.join(output_folder, "compare_reclassify.xml"))


        # test 3rd case with aspect
        aspect = os.path.join(input_folder, "aspect_in")
        reclassify_expect = os.path.join(reference_folder, "expect_r_3")

        remap = "-1 0 9;0 22.5 1;22.5 67.5 2;67.5 112.5 3;\
               112.5 157.5 4;157.5 202.5 5;202.5 247.5 6;247.5 292.5 7;\
               292.5 337.5 8;337.5 360 1"

        reclassify(aspect, remap, reclassify_result)

        compare_result = os.path.join(output_folder, "compare_reclassify.txt")

        arcpy.RasterCompare_management(reclassify_result, reclassify_expect,
                                       '', '', '', compare_result)

        if '"true"' not in open(compare_result).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        # delete output files
        if arcpy.Exists(reclassify_result):
            arcpy.Delete_management(reclassify_result)

        os.remove(compare_result)
        os.remove(os.path.join(output_folder, "compare_reclassify.xml"))


if __name__ == "__main__":
    unittest.main()
