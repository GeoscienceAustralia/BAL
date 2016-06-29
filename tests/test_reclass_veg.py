"""
    Title: test_reclas_veg.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-06-24
    Description: Unit testing module for reclass_veg function in bal.py
"""

import unittest
import arcpy
import sys
import os.path
from inspect import getfile, currentframe


class TestReclassVeg(unittest.TestCase):

    def test_reclass_veg(self):

        cmd_folder = os.path.realpath(os.path.abspath(
                     os.path.split(getfile(currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')

        input_folder = os.path.join(testdata_folder, 'input')
        reference_folder = os.path.join(testdata_folder, 'reference')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        arcpy.env.overwriteOutput = True

        dem = os.path.join(input_folder, "dem.img")
        veg = os.path.join(input_folder, "vege.img")
        mask = os.path.join(input_folder, "test_mask.shp")
        veg_class_expect = os.path.join(reference_folder, "expect_v_r")
        
        input_folder = os.path.dirname(veg)
        arcpy.env.workspace = input_folder

        from bal import reclass_veg

        output_folder = os.path.join(testdata_folder, 'output')
                      
        remap = "1 3;2 2;3 3;4 5 7;6 8 1;9 2;10 3;11 12 1;13 1;14 3;\
                 15 6;16 7;17 3;18 19 2;20 7;21 3;22 2; 23 24 7;25 27 5;\
                 28 2;29 30 7;31 3;32 33 1;34 7;35 3;36 37 7;38 4;39 7;40 1;\
                 41 2;42 7;43 2;44 7;45 4;46 7;47 NODATA;97 2;98 99 1"


        veg_class = reclass_veg(veg, dem, output_folder, remap, mask)

        compare_result = os.path.join(output_folder, "compare_veg_r.txt")

        arcpy.RasterCompare_management(veg_class, veg_class_expect, '', '', '',
                                       compare_result)

        if '"true"' not in open(compare_result).read():
            self.assertEqual(1, 1, 'No errors')
        else:
            self.assertEqual(1, 0, 'Has errors')

        # delete output files
        if arcpy.Exists(veg_class):
            arcpy.Delete_management(veg_class)

        os.remove(compare_result)
        os.remove(os.path.join(output_folder, "compare_veg_r.xml"))


if __name__ == "__main__":
    unittest.main()
