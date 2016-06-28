# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 11:41:15 2016

@author: u89076
"""

from __future__ import absolute_import 
  
import numpy as np
#from osgeo import gdal
#from osgeo.gdalconst import GA_ReadOnly
import arcpy
import os

def clip_array(data, x_left, y_upper, pixelwidth, pixelheight, extent):

    """
    Return the clipped area of the input array according to an sub-extent
    :param data: :class:`numpy.ndarray` the input array
    :param x_left: `float` the left-most x projected coordinate 
    :param y_upper: `float` the upper-most y projected coordinate
    :param pixelwidth: `float` the pixel width
    :param pixelheight: `float` the pixel height
    :param extent: `tuple` the clipping extent
    :return: :class:`numpy.ndarray` the clipped array
    """
    
#    import pdb
#    pdb.set_trace()
    
    x_start = int(np.around((extent[0] - x_left)/pixelwidth))
    y_start = int(np.around((y_upper - extent[3])/pixelheight))

    cols = int(np.around((extent[2] - extent[0])/pixelwidth))
    rows = int(np.around((extent[3] - extent[1])/pixelheight))

    x_end = x_start + cols
    y_end = y_start + rows

    data_clip = data[y_start:y_end, x_start:x_end]

    return data_clip
    
    

def extract_by_mask(image_fname, extent_file, out_fname): 
   
    
    output_folder = os.path.dirname(image_fname)
    arcpy.env.overwriteOutput = True

    # set directory
    work_folder = output_folder
    os.chdir(work_folder)
    arcpy.env.workspace = work_folder
    
    nodata_value = -99
    
#    import pdb
#    pdb.set_trace()   
    
    # get the informaiton of the original image     
    desc = arcpy.Describe(image_fname)
    x_min = desc.extent.XMin
    y_min = desc.extent.YMin
    x_max = desc.extent.XMax
    y_max = desc.extent.YMax    
    pixel_w = desc.children[0].meanCellWidth
    pixel_h = desc.children[0].meanCellHeight
    sref = desc.spatialReference
    data = arcpy.RasterToNumPyArray(image_fname, nodata_to_value=nodata_value)

    # rasterise the shapefile and then extract into numpy array    
    ext_raster = "ext_raster"    
    arcpy.FeatureToRaster_conversion(extent_file, "FID", ext_raster, pixel_w)    
    extent_data = arcpy.RasterToNumPyArray(ext_raster, nodata_to_value=nodata_value)
    
    # decide the effective extent to extract the raster
    extent = arcpy.Describe(extent_file).extent 
    if extent.XMin < x_min:
        effect_xmin = x_min
    else:
        effect_xmin = extent.XMin
        
    if extent.YMin < y_min:
        effect_ymin = y_min
    else:
        effect_ymin = extent.YMin 
        
    if extent.XMax > x_max:
        effect_xmax = x_max
    else:
        effect_xmax = extent.XMax

    if extent.YMax > y_max:
        effect_ymax = y_max
    else:
        effect_ymax = extent.YMax         
    
    
    effect_extent = (effect_xmin, effect_ymin, effect_xmax, effect_ymax)

    # get the lowleft corner for positioning the output raster
    lowleft_corner = arcpy.Point(effect_xmin, effect_ymin)          
    
    # extract the effective extent of interest from original image data
    data_in_extent = clip_array(data, x_min, y_max, pixel_w, pixel_h, 
                                effect_extent) 

    # extract the effective extent of interest from original extent data
    extent_data_effect = clip_array(extent_data, extent.XMin, extent.YMax, 
                                    pixel_w, pixel_h, effect_extent)                                
       
    # operate data and data_in_extent, if nodata in either, output is nodata 
    nodata_area = np.where(extent_data_effect == nodata_value)
    data_in_extent[nodata_area] = nodata_value    
    
    # save the output array into a raster
    arcpy.NumPyArrayToRaster(data_in_extent, lowleft_corner, pixel_w, pixel_h,
                             value_to_nodata=nodata_value).save(out_fname)
    arcpy.DefineProjection_management(out_fname, sref)
    
       
    del data_in_extent
    del data

    if arcpy.Exists(ext_raster):
        arcpy.Delete_management(ext_raster)   
 
    
     

if __name__ == '__main__':
    image_fname = r'C:\bal_removeSpatialAnalyst\input\vege_proj.img'
    out_fname = r'C:\bal_removeSpatialAnalyst\input\plygon_result'
    extent_file = r'C:\bal_removeSpatialAnalyst\input\expect_mask_others.shp'
    extract_by_mask(image_fname, extent_file, out_fname)