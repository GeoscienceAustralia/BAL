"""
     Title: test_bal_cal.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-07-09
     Description: Unit testing module for bal_cal function in calculate_bal.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe
from numpy.testing import assert_array_equal


class TestBalCal(unittest.TestCase):

    def test_bal_cal(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                                      os.path.split(
                                      getfile(currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')

        input_folder = os.path.join(testdata_folder, 'input')
        output_folder = os.path.join(testdata_folder, 'output')
        reference_folder = os.path.join(testdata_folder, 'reference')

        veg_class = os.path.join(output_folder, "veg_c")
        slope = os.path.join(output_folder, "slope_c")
        aspect = os.path.join(output_folder, "aspect_c")
        fdi = 80

        if not arcpy.Exists(slope):
            arcpy.CopyRaster_management(os.path.join(input_folder, "slope_c"),
                              slope)

        if not arcpy.Exists(aspect):
            arcpy.CopyRaster_management(os.path.join(input_folder, "aspect_c"),
                              aspect)

        if not arcpy.Exists(veg_class):
            arcpy.CopyRaster_management(os.path.join(input_folder, "veg_c"),
                              veg_class)

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True

        bal_max_expect = os.path.join(reference_folder, "expect_bal_max.img")

        from calculate_bal import bal_cal

        bal_cal(veg_class, slope, aspect, fdi)

        compare_result = os.path.join(output_folder, "compare_bal.txt")

        arcpy.RasterCompare_management('bal_max.img', bal_max_expect, '',
                                       'Pixel Value', '', compare_result)
        if '"true"' not in open(compare_result).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        ds1 = os.path.join(output_folder, "bal_max.img")
        if ds1 is None:
            print 'Could not open bal_max.img'
            sys.exit(1)
        bal_data = arcpy.RasterToNumPyArray(ds1, nodata_to_value=-99)

        ds2 = bal_max_expect
        if ds2 is None:
            print 'Could not open expect_bal_max.img'
            sys.exit(1)
        bal_expect = arcpy.RasterToNumPyArray(ds2, nodata_to_value=-99)

        assert_array_equal(bal_data, bal_expect)

        os.remove(compare_result)
        os.remove(os.path.join(output_folder, "compare_bal.xml"))

        for a_dir in ['w', 'e', 'n', 's', 'nw', 'ne', 'se', 'sw', 'max']:
            output_bal = os.path.join(output_folder, 'bal_' + a_dir + '.img')
            if arcpy.Exists(output_bal):
                arcpy.Delete_management(output_bal)


if __name__ == "__main__":
    unittest.main()
