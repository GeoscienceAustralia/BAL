"""
:mod:`bal` - Calculate the bushfire attack level (BAL)
===============================================================

This module is used to produce the bushfire attack level (BAL) for an area of
interest within Australia based on input vegetation and elevation datasets
as per Method 1 in the Australian Standard AS 3959 (2009) -- Construction of
buildings in bushfire-prone areas.

:moduleauthor: Tina Yang <tina.yang@ga.gov.au>

"""

import sys
import os
import inspect
import math
from os.path import join as pjoin
import arcpy
from calculate_bal import bal_cal
from utilities.sa_tools import extract_by_mask, reclassify, cal_slope_aspect

__version__ = '1.0'


def reclass_veg(veg, dem, output_folder, remap, mask):
    """
    Reclassify the original vegetation into the categories classified as Table
    2.3 in AS 3959 (2009).

    :param veg: `file` the input vegetation
    :param dem: `file` the input dem used as reference projection
    :param output_folder: `str` the output folder
    :param remap: `srt` the vegetation reclassification
    :param mask: `file` the mask for the effective AOI

    :return: `file` the reclassified vegetation
    """

    arcpy.env.overwriteOutput = True

    input_folder = os.path.dirname(veg)
    arcpy.env.workspace = input_folder

    veg_r_init = 'veg_r_init'
    veg_r_proj = pjoin(input_folder, 'veg_r_pj')
    veg_class_r = pjoin(output_folder, 'veg_r')

    arcpy.AddMessage('Remap the vegetation into classes of 1 ~ 7 ...')

    # Derive reclassifed veg...
    reclassify(veg, remap, veg_r_init)

    # project as dem and change cell size same as that of dem
    dem_c = arcpy.GetRasterProperties_management(dem, "CELLSIZEX").getOutput(0)

    arcpy.ProjectRaster_management(veg_r_init, veg_r_proj, dem, "#", dem_c)

    if arcpy.Exists(veg_r_init):
        arcpy.Delete_management(veg_r_init)

    # get the AOI
    extract_by_mask(veg_r_proj, mask, veg_class_r)

    g_list = arcpy.ListRasters('g_g*')
    if len(g_list) != 0:
        for g_file in g_list:
            arcpy.Delete_management(g_file)

    if arcpy.Exists(veg_r_proj):
        arcpy.Delete_management(veg_r_proj)

    return veg_class_r


def get_slope_aspect(input_dem, output_folder, mask):
    """
    Calculate the slope and aspect from the input DEM

    :param input_dem: `file` the input DEM
    :param output_folder: `str` the output folder
    :param mask: `file` the mask for the effective AOI

    :return: `file` the reclassified slope
    :return: `file` the reclassified aspect
    """
    arcpy.env.overwriteOutput = True

    input_folder = os.path.dirname(input_dem)
    arcpy.env.workspace = input_folder

    dem_slope = pjoin(input_folder, 'slope')
    dem_aspect = pjoin(input_folder, 'aspect')

    # Derive slope and aspect ...
    cal_slope_aspect(input_dem, dem_slope, dem_aspect)

    aspect_rec_init = pjoin(input_folder, 'aspect_r_i')
    slope_rec_init = pjoin(input_folder, 'slope_r_i')
    aspect_rec = pjoin(output_folder, 'aspect_r')
    slope_rec = pjoin(output_folder, 'slope_r')

    # Derive reclassifed aspect...
    arcpy.AddMessage('Remap the aspect into classes of 1 ~ 9 ...')

    reclassify(dem_aspect, "-1 0 9;0 22.5 1;22.5 67.5 2;67.5 112.5 3;\
               112.5 157.5 4;157.5 202.5 5;202.5 247.5 6;247.5 292.5 7;\
               292.5 337.5 8;337.5 360 1", aspect_rec_init)

    value_max = arcpy.GetRasterProperties_management(
                dem_slope, "MAXIMUM").getOutput(0)

    if float(value_max) < 20:
        value_max = 20.0001

    # remap is minimum inclusive but maxmum exclusive. using .0001 to comform
    # to the standard minimum is exclusive and maximum is inclusive
    remap = "0 0 1;0.0001 5 2;5.0001 10 3;10.0001 15 4;\
            15.0001 20 5;20.0001 " + \
            str(math.ceil(float(value_max))) + " 6"

    arcpy.AddMessage('Remap the slope into classes of 1 ~ 6 ...')

    # Derive reclassifed slope...
    reclassify(dem_slope, remap, slope_rec_init)

    extract_by_mask(aspect_rec_init, mask, aspect_rec)
    extract_by_mask(slope_rec_init, mask, slope_rec)

    g_list = arcpy.ListRasters('g_g*')
    if len(g_list) != 0:
        for g_file in g_list:
            arcpy.Delete_management(g_file)
    if arcpy.Exists(dem_slope):
        arcpy.Delete_management(dem_slope)
    if arcpy.Exists(dem_aspect):
        arcpy.Delete_management(dem_aspect)
    if arcpy.Exists(slope_rec_init):
        arcpy.Delete_management(slope_rec_init)
    if arcpy.Exists(aspect_rec_init):
        arcpy.Delete_management(aspect_rec_init)

    return slope_rec, aspect_rec


def find_common_area(veg_class, slope, aspect):
    """
    Find the common area of vegetation, slope and aspect to calculate BAL.

    :param veg_class: `file` the reclassified vegetation
    :param slope: `file` the slope derived from DEM
    :param aspect: `file` the aspect derived from DEM

    :return: `file` the vegetation in common area
    :return: `file` the slope in common area
    :return: `file` the aspect in common area
    """

    output_folder = os.path.dirname(veg_class)
    arcpy.env.overwriteOutput = True

    # set directory
    work_folder = output_folder
    os.chdir(work_folder)
    arcpy.env.workspace = work_folder

    # get the common area of veg and dem
    # get the extent of inputs
    slope_poly = "slope_poly.shp"
    veg_class_poly = "veg_class_poly.shp"
    get_footprint(slope, slope_poly)
    get_footprint(veg_class, veg_class_poly)

    mask_com = 'mask_com.shp'

    arcpy.Intersect_analysis([slope_poly, veg_class_poly], mask_com)

    veg_class_com = pjoin(output_folder, 'veg_c')
    slope_com = pjoin(output_folder, 'slope_c')
    aspect_com = pjoin(output_folder, 'aspect_c')

    extract_by_mask(veg_class, mask_com, veg_class_com)
    extract_by_mask(slope, mask_com, slope_com)
    extract_by_mask(aspect, mask_com, aspect_com)

    if arcpy.Exists(slope_poly):
        arcpy.Delete_management(slope_poly)
    if arcpy.Exists(veg_class_poly):
        arcpy.Delete_management(veg_class_poly)
    if arcpy.Exists(mask_com):
        arcpy.Delete_management(mask_com)
    if arcpy.Exists(veg_class):
        arcpy.Delete_management(veg_class)
    if arcpy.Exists(slope):
        arcpy.Delete_management(slope)
    if arcpy.Exists(aspect):
        arcpy.Delete_management(aspect)

    return veg_class_com, slope_com, aspect_com


def bal_calc(vegetation, dem, fdi, output_folder, remap, mask):
    """
    Calcuate BAL based on vegetation map and DEM.

    :param vegetation: `file` the original vegetation
    :param dem: `file` the input DEM
    :param fdi: `int` the input FDI value
    :param output_folder: `str` the output folder
    :param remap: `srt` the vegetation reclassification
    :param mask: `file` the mask for the effective area of interest (AOI)
    """
    arcpy.env.overwriteOutput = True

    arcpy.AddMessage('Reclassify the vegetation map ...   ')
    veg_class = reclass_veg(vegetation, dem, output_folder, remap, mask)

    arcpy.AddMessage('Reclassify slope and aspect ...   ')
    slope, aspect = get_slope_aspect(dem, output_folder, mask)

    if arcpy.Exists(mask):
        arcpy.Delete_management(mask)

    # extract the common area between vegtation, slope and aspect
    arcpy.AddMessage('Get common area of input data ...   ')
    veg_class_com, slope_com, aspect_com = find_common_area(veg_class,
                                                            slope, aspect)

    arcpy.AddMessage('Calculate the BAL ...   ')
    bal_cal(veg_class_com, slope_com, aspect_com, fdi)


def get_extent_mask(extent, mask):
    """
    Derive the mask for the customised input extent.

    :param extent: `str` the input extent
    :param mask: `file` the output mask
    """

    extent_list = str(extent).split()

    # Array to hold points
    array = arcpy.Array()

    # Create the bounding box
    array.add(arcpy.Point(float(extent_list[0]), float(extent_list[1])))
    array.add(arcpy.Point(float(extent_list[2]), float(extent_list[1])))
    array.add(arcpy.Point(float(extent_list[2]), float(extent_list[3])))
    array.add(arcpy.Point(float(extent_list[0]), float(extent_list[3])))
    array.add(arcpy.Point(float(extent_list[0]), float(extent_list[1])))

    # Create the polygon object
    polygon = arcpy.Polygon(array)
    array.removeAll()
    arcpy.CopyFeatures_management(polygon, mask)


def get_footprint(raster, footprint):
    """
    Find the footprint of a raster

    :param raster: `file` the input raster
    :param footprint: `file` the output footprint
    """

    # set the environment variable and workspace
    arcpy.env.overwriteOutput = True
    input_folder = os.path.dirname(raster)
    arcpy.env.workspace = input_folder

    raster_extent = arcpy.Describe(raster).extent

    get_extent_mask(raster_extent, footprint)

    # add the original spatial reference to the footprint
    desc = arcpy.Describe(raster)
    arcpy.DefineProjection_management(footprint, desc.spatialReference)


def find_aoi(extent, dem, veg):
    """
    Find the effective area of interest based on input vegetation map, DEM and
    extent.

    :param extent: `str` the input extent
    :param dem: `file` the input DEM
    :param veg: `file` the input vegetation

    :return: `file` the mask for effective AOI
    """

    # set the environment variable and workspace
    arcpy.env.overwriteOutput = True
    input_folder = os.path.dirname(dem)
    arcpy.env.workspace = input_folder

    # derive the effective mask based on the input data
    arcpy.AddMessage('Get the area of interest from the input extent ...')
    mask = 'mask.shp'

    if str(extent) in ['DEFAULT', 'MAXOF', 'MINOF']:
        # get the extent of inputs
        dem_poly = "dem_poly.shp"
        veg_poly = "veg_poly.shp"
        get_footprint(dem, dem_poly)
        get_footprint(veg, veg_poly)
        arcpy.Intersect_analysis([dem_poly, veg_poly], mask)

        # delete intermediate files
        if arcpy.Exists(dem_poly):
            arcpy.Delete_management(dem_poly)
        if arcpy.Exists(veg_poly):
            arcpy.Delete_management(veg_poly)
    else:
        get_extent_mask(extent, mask)

        # add dem's spatial reference to the mask
        desc = arcpy.Describe(dem)
        arcpy.DefineProjection_management(mask, desc.spatialReference)

    return mask


def run():
    """
    Run the BAL calculations.

    """
    # add subfolders into path
    cmd_folder = os.path.realpath(
        os.path.abspath(
            os.path.split(
                inspect.getfile(
                    inspect.currentframe()))[0]))
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)

    cmd_subfolder = pjoin(cmd_folder, "utilities")
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)

    # get input parameters from toolbox interface
    dem = arcpy.GetParameterAsText(0)
    veg = arcpy.GetParameterAsText(1)
    remap = arcpy.GetParameterAsText(2)
    output_folder = arcpy.GetParameterAsText(3)
    fdi = arcpy.GetParameter(4)
    extent = arcpy.GetParameter(5)

    dem_sr = arcpy.Describe(dem).spatialReference
    arcpy.AddMessage("DEM's spatial reference type is {0}".format(dem_sr.type))

    if dem_sr.type == "Projected":
        # find effective AOI based on the input parameters
        mask = find_aoi(extent, dem, veg)

        try:
            # calculate the BAL for the effective AOI
            bal_calc(veg, dem, fdi, output_folder, remap, mask)
            arcpy.AddMessage("Successfully completed BAL calculation!")
        except Exception as err:
            # Report any exceptions back
            arcpy.AddError(err)

    else:
        arcpy.AddError("To go ahead, the DEM needs to be projected first")

if __name__ == '__main__':
    run()
