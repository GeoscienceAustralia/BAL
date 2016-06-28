"""
    Title: test_bal_class.py
    Author: Tina Yang, tina.yang@ga.gov.au
    CreationDate: 2015-07-02
    Description: Unit testing module for BAL_CLASS dictionary in
    bal_database.py
"""

import sys
import os.path
import unittest
import numpy as np
import arcpy
from inspect import getfile, currentframe


class TestEXTRACTBYMASK(unittest.TestCase):

    def test_extract_by_mask(self):

        cmd_folder = os.path.realpath(
                     os.path.abspath(os.path.split(
                     getfile(currentframe()))[0]))

        testdata_folder = os.path.join(cmd_folder, 'test_data')
        input_folder = os.path.join(testdata_folder, 'input')
        output_folder = os.path.join(testdata_folder, 'output')
        refer_folder = os.path.join(testdata_folder, 'reference')

        parent = os.path.abspath(os.path.join(cmd_folder, os.pardir))

        if parent not in sys.path:
            sys.path.insert(0, parent)

        from utilities.sa_tools import extract_by_mask
        
        arcpy.env.overwriteOutput = True     

        raster = os.path.join(input_folder, "vege_mga.img")        
        result = os.path.join(output_folder, "extracted_raster.img")
        
        extent_list = [os.path.join(input_folder, "mask_extent_small.shp"),
                       os.path.join(input_folder, "mask_extent_large.shp")]
                       
        expec_list = [os.path.join(refer_folder, "expect_extracted_small.img"),
                      os.path.join(refer_folder, "expect_extracted_large.img")]                       
        
        index = 0
        for extent in extent_list:
            
            extract_by_mask(raster, extent, result)
    
            compare_result = os.path.join(output_folder, "compare_result.txt")
    
            arcpy.RasterCompare_management(result, expec_list[index], '', 
                                           'Pixel Type', '', compare_result, 
                                           '', '', '')
                                           
            if '"true"' not in open(compare_result).read():
                self.assertEqual(1, 1, 'No errors')
            else:
                self.assertEqual(1, 0, 'Has errors')
    
            if arcpy.Exists(result):
                arcpy.Delete_management(result)
    
            os.remove(compare_result)
            os.remove(os.path.join(output_folder, "compare_result.xml"))

            index += 1

if __name__ == "__main__":
    unittest.main()
