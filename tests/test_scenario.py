"""
     Title: test_scenario.py
     Author: Tina Yang, tina.yang@ga.gov.au
     CreationDate: 2015-07-24
     Description: scenario test based on sample input data: classified veg,
     classified slope and classified aspect.
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe
import numpy as np
from numpy.testing import assert_array_equal


class TestScenario(unittest.TestCase):

    def test_scenario(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                                    os.path.split(getfile(currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')
        input_folder = os.path.join(testdata_folder, 'input')
        output_folder = os.path.join(testdata_folder, 'output')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True

        veg_class = os.path.join(output_folder, "veg_samp")
        slope = os.path.join(output_folder, "slope_samp")
        aspect = os.path.join(output_folder, "aspect_samp")

        bal_expect = np.ones([3, 140])
        bal_expect[:, 0] = -99
        bal_expect[:, 1:29] = 100
        bal_expect[:, 29:41] = 29
        bal_expect[:, 41:53] = 40
        bal_expect[:, 53:65] = 19
        bal_expect[:, 65:81] = 40
        bal_expect[:, 81:89] = 19
        bal_expect[:, 89:105] = 100
        bal_expect[:, 105:121] = 29
        bal_expect[:, 121:140] = 200

        if not arcpy.Exists(veg_class):
            arcpy.Copy_management(os.path.join(input_folder, "veg_samp"),
                              veg_class)

        if not arcpy.Exists(slope):
            arcpy.Copy_management(os.path.join(input_folder, "slope_samp"),
                              slope)

        if not arcpy.Exists(aspect):
            arcpy.Copy_management(os.path.join(input_folder, "aspect_samp"),
                              aspect)

        fdi = 80

        from calculate_bal import bal_cal
        bal_cal(veg_class, slope, aspect, fdi)

        ds1 = os.path.join(output_folder, "bal_w.img")

        if ds1 is None:
            print 'Could not open bal_w.img'
            sys.exit(1)

        bal_data = arcpy.RasterToNumPyArray(ds1, nodata_to_value=-99)

        assert_array_equal(bal_data, bal_expect)

        for a_dir in ['w', 'e', 'n', 's', 'nw', 'ne', 'se', 'sw', 'max']:
            output_bal = os.path.join(output_folder, 'bal_' + a_dir + '.img')
            if arcpy.Exists(output_bal):
                arcpy.Delete_management(output_bal)


if __name__ == "__main__":
    unittest.main()
