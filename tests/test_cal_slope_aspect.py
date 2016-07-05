"""
     Title: test_cal_slope_aspect.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-06-24
     Description: Unit testing module for cal_slope_aspect in sa_tools.py.
"""

import unittest
import arcpy
import sys
import os.path
import numpy
from inspect import getfile, currentframe


class TestCalSlopeAspect(unittest.TestCase):

    def test_cal_slope_aspect(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                                      os.path.split(getfile(
                                      currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')
        input_folder = os.path.join(testdata_folder, 'input')
        output_folder = os.path.join(testdata_folder, 'output')
        reference_folder = os.path.join(testdata_folder, 'reference')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True

        dem = os.path.join(input_folder, "dem.img")
        slope_result = os.path.join(output_folder, "result_s")
        aspect_result = os.path.join(output_folder, "result_a")
        slope_expect = os.path.join(reference_folder, "expect_s")
        aspect_expect = os.path.join(reference_folder, "expect_a")

        from utilities.sa_tools import cal_slope_aspect

        cal_slope_aspect(dem, slope_result, aspect_result)

        compare_result_slope = os.path.join(output_folder,
                                            "compare_slope.txt")
        compare_result_aspect = os.path.join(output_folder,
                                             "compare_aspect.txt")

        arcpy.RasterCompare_management(slope_result, slope_expect, '',
                             'Pixel Value; Statistics; Compression Type', '',
                             compare_result_slope)
        if '"true"' not in open(compare_result_slope).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        arcpy.RasterCompare_management(aspect_result, aspect_expect, '',
                            'Pixel Value; Statistics; Compression Type', '',
                            compare_result_aspect)
        if '"true"' not in open(compare_result_aspect).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        # compare pixel value
        nodata_value = -99
        slope_arr = arcpy.RasterToNumPyArray(slope_result,
                                             nodata_to_value=nodata_value)
        slope_arr_exp = arcpy.RasterToNumPyArray(slope_expect,
                                                 nodata_to_value=nodata_value)

        numpy.testing.assert_array_almost_equal(slope_arr, slope_arr_exp,
                                                decimal=4)

        aspec_arr = arcpy.RasterToNumPyArray(aspect_result,
                                              nodata_to_value=nodata_value)
        aspec_arr_exp = arcpy.RasterToNumPyArray(aspect_expect,
                                                  nodata_to_value=nodata_value)

        numpy.testing.assert_array_almost_equal(aspec_arr, aspec_arr_exp,
                                                decimal=4)

        if arcpy.Exists(slope_result):
            arcpy.Delete_management(slope_result)

        if arcpy.Exists(aspect_result):
            arcpy.Delete_management(aspect_result)

        try:
            os.remove(compare_result_slope)
            os.remove(os.path.join(output_folder, "compare_slope_r.xml"))
            os.remove(compare_result_aspect)
            os.remove(os.path.join(output_folder, "compare_aspect_r.xml"))
        except OSError:
            pass


if __name__ == "__main__":
    unittest.main()
