"""
:mod:`sa_tools` - some support functions replacing spatial analyst

===============================================================

This module includes algorithms that are used to replace spatial analyst
functions such as ExtractByMask, Reclassify, Slope and Aspect used within this
package.

:moduleauthor: Tina Yang <tina.yang@ga.gov.au>

"""

from __future__ import absolute_import

import numpy as np
from scipy import ndimage
import numexpr
import arcpy
import os

RADIANS_PER_DEGREE = 0.01745329251994329576923690768489


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

    x_start = int(np.around((extent[0] - x_left)/pixelwidth))
    y_start = int(np.around((y_upper - extent[3])/pixelheight))

    cols = int(np.around((extent[2] - extent[0])/pixelwidth))
    rows = int(np.around((extent[3] - extent[1])/pixelheight))

    x_end = x_start + cols
    y_end = y_start + rows

    data_clip = data[y_start:y_end, x_start:x_end]

    return data_clip


def extract_by_mask(image_fname, extent_file, out_fname):
    """
    Extract a raster using a feature (shape) file

    :param image_fname: `file` the input raster
    :param extent_file: `file` the input extent feature file

    :return: `file` the output raster
    """

    output_folder = os.path.dirname(image_fname)
    arcpy.env.overwriteOutput = True

    # set directory
    work_folder = output_folder
    os.chdir(work_folder)
    arcpy.env.workspace = work_folder

    # set nodata value
    nodata_value = -99

    # get the information of the original image
    desc = arcpy.Describe(image_fname)
    x_min = desc.extent.XMin
    y_min = desc.extent.YMin
    x_max = desc.extent.XMax
    y_max = desc.extent.YMax
    pixel_w = desc.meanCellWidth
    pixel_h = desc.meanCellHeight
    sref = desc.spatialReference
    data = arcpy.RasterToNumPyArray(image_fname, nodata_to_value=nodata_value)

    # rasterise the shapefile and then extract into numpy array
    ext_raster = "ext_raster"
    arcpy.FeatureToRaster_conversion(extent_file, "FID", ext_raster, pixel_w)
    extent_data = arcpy.RasterToNumPyArray(ext_raster,
                                           nodata_to_value=nodata_value)

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

    # operate extent_data_effect and data_in_extent, if nodata in either,
    # output is nodata
    nodata_area = np.where(extent_data_effect == nodata_value)
    data_in_extent[nodata_area] = nodata_value

    # save the output array into a raster
    arcpy.NumPyArrayToRaster(data_in_extent, lowleft_corner, pixel_w, pixel_h,
                             value_to_nodata=nodata_value).save(out_fname)
    arcpy.DefineProjection_management(out_fname, sref)

    del data_in_extent
    del extent_data_effect
    del data

    if arcpy.Exists(ext_raster):
        arcpy.Delete_management(ext_raster)


def reclassify(image_fname, remap, out_fname):
    """
    Reclassify the raster as per the input remap

    :param image_fname: `file` the input raster
    :param remap: `str` the info of remap

    :return: `file` the output raster
    """

    output_folder = os.path.dirname(image_fname)
    arcpy.env.overwriteOutput = True

    # set directory
    work_folder = output_folder
    os.chdir(work_folder)
    arcpy.env.workspace = work_folder

    # set nodata value
    nodata_value = -99

    # get the information of the original image
    desc = arcpy.Describe(image_fname)
    x_min = desc.extent.XMin
    y_min = desc.extent.YMin
    pixel_w = desc.meanCellWidth
    pixel_h = desc.meanCellHeight
    sref = desc.spatialReference
    # get the lowleft corner for positioning the output raster
    lowleft_corner = arcpy.Point(x_min, y_min)

    data = arcpy.RasterToNumPyArray(image_fname, nodata_to_value=nodata_value)

    remap_list = remap.split(";")

    for a_map in remap_list:
        values = a_map.lstrip().split(" ")
        if len(values) == 2:
            start_value = float(values[0])
            end_value = float(values[0])
            new_value = values[1]
        else:
            start_value = float(values[0])
            end_value = float(values[1])
            new_value = values[2]

        # to include the orignal end value , expand the end value a bit
        end_value += 0.0001

        if new_value == 'NODATA':
            new_value = nodata_value
        else:
            new_value = int(new_value)

        range_loc = np.where((data >= start_value) & (data < end_value))
        data[range_loc] = new_value

    data = data.astype(int)
    # save the output array into a raster
    arcpy.NumPyArrayToRaster(data, lowleft_corner, pixel_w, pixel_h,
                             value_to_nodata=nodata_value).save(out_fname)
    arcpy.DefineProjection_management(out_fname, sref)

    del data


def cal_slope_aspect(dem, slope_fname, aspect_fname):
    """
    Calculate the slope from the input dem

    :param dem: `file` the input dem
    :param slope_fname: `file` the output slope
    :param aspect_fname: `file` the output aspect
    """

    output_folder = os.path.dirname(dem)
    arcpy.env.overwriteOutput = True

    # set directory
    work_folder = output_folder
    os.chdir(work_folder)
    arcpy.env.workspace = work_folder

    # set nodata value
    nodata_value = -99

    # get the information of the original image
    desc = arcpy.Describe(dem)
    x_min = desc.extent.XMin
    y_min = desc.extent.YMin
    pixel_w = desc.meanCellWidth
    pixel_h = desc.meanCellHeight
    sref = desc.spatialReference
    # get the lowleft corner for positioning the output raster
    lowleft_corner = arcpy.Point(x_min, y_min)

    elevation_array = arcpy.RasterToNumPyArray(dem,
                                               nodata_to_value=nodata_value)

    mask = np.where(elevation_array == nodata_value)

    dzdx_array = ndimage.sobel(elevation_array, axis=1) / (8. * pixel_w)
    dzdy_array = ndimage.sobel(elevation_array, axis=0) / (8. * pixel_h)

    # Slope
    hypotenuse_array = np.hypot(dzdx_array, dzdy_array)
    slope_array = numexpr.evaluate(
        "arctan(hypotenuse_array) / RADIANS_PER_DEGREE")
    slope_array[mask] = nodata_value
    del hypotenuse_array

    # Aspect
    # Convert angles from conventional radians to compass heading 0-360
    aspect_array = numexpr.evaluate(
        "(450 - arctan2(dzdy_array, -dzdx_array) / RADIANS_PER_DEGREE) % 360")
    aspect_array[mask] = nodata_value
    del dzdx_array, dzdy_array

    # save the output array into a raster
    arcpy.NumPyArrayToRaster(slope_array, lowleft_corner, pixel_w, pixel_h,
                             value_to_nodata=nodata_value).save(slope_fname)
    arcpy.DefineProjection_management(slope_fname, sref)

    arcpy.NumPyArrayToRaster(aspect_array, lowleft_corner, pixel_w, pixel_h,
                             value_to_nodata=nodata_value).save(aspect_fname)
    arcpy.DefineProjection_management(aspect_fname, sref)

    del elevation_array, slope_array, aspect_array
