"""
:mod:`calculate_bal` - essential part of calculating the
bushfire attack level (BAL)

===============================================================

This module includes algorithms that are used to calculate BAL as per
Method 1 in the Australian Standard AS 3959 (2009) -- Construction of
buildings in bushfire-prone areas.

:moduleauthor: Tina Yang <tina.yang@ga.gov.au>

"""

import arcpy
import os
import numpy as np
from utilities import value_lookup, bal_database


def bal_cal(veg_class, slope, aspect, fdi):
    """
    Calculate the BAL based on the classified vegetation and the combined
    slope and vegetation according to an appropriate table in AS 3959 (2009)
    to determine the bushfire attack level (BAL).

    :param veg_class: `file` the input classified vegetation
    :param slope: `file` the input slope
    :param aspect: `file` the input aspect
    :param fdi: `int` the input FDI value
    """

    output_folder = os.path.dirname(veg_class)
    arcpy.env.overwriteOutput = True

    # set directory
    work_folder = output_folder
    os.chdir(work_folder)
    arcpy.env.workspace = work_folder

    # get veg raster size, format, projection, etc
    desc = arcpy.Describe(veg_class)
    extent = desc.extent
    lowleft_corner = arcpy.Point(extent.XMin, extent.YMin)
    pixel_w = desc.meanCellWidth
    pixel_h = desc.meanCellHeight
    sref = desc.spatialReference

    # load the raster into numpy array
    veg_data = arcpy.RasterToNumPyArray(veg_class, nodata_to_value=-99)
    slope_data = arcpy.RasterToNumPyArray(slope, nodata_to_value=-99)
    aspect_data = arcpy.RasterToNumPyArray(aspect, nodata_to_value=-99)

    # calculate the BAL for each direction in numpy array and get maximum of
    # 2 direction each time, until get the maximum of all directions
    dire = ['w', 'e', 'n', 's', 'nw', 'ne', 'se', 'sw']

    for one_dir in dire:
        bal_list = []
        outdata = convo(one_dir, veg_data, slope_data, aspect_data,
                        pixel_w, fdi)

        output_dir = 'bal_' + one_dir + '.img'

        if arcpy.Exists(output_dir):
            arcpy.Delete_management(output_dir)

        arcpy.NumPyArrayToRaster(outdata, lowleft_corner, pixel_w,
                                 pixel_h, value_to_nodata=-99).save(output_dir)

        arcpy.DefineProjection_management(output_dir, sref)

        if one_dir == 'w':
            bigger = outdata
            del outdata
            continue

        bal_list.append(bigger)
        bal_list.append(outdata)
        bigger = get_max_bal(bal_list)
        del outdata

    # get maximum BAL from the list
    arcpy.NumPyArrayToRaster(bigger, lowleft_corner, pixel_w,
                             pixel_h, value_to_nodata=-99).save('bal_max.img')

    arcpy.DefineProjection_management('bal_max.img', sref)

    arcpy.BuildPyramidsandStatistics_management(output_folder, "#",
                                                "BUILD_PYRAMIDS",
                                                "CALCULATE_STATISTICS")

    # delete intermediate results
    if arcpy.Exists(veg_class):
        arcpy.Delete_management(veg_class)
    if arcpy.Exists(slope):
        arcpy.Delete_management(slope)
    if arcpy.Exists(aspect):
        arcpy.Delete_management(aspect)
    del veg_data, slope_data, aspect_data
    del bal_list, bigger


def get_max_bal(bal_list):
    """
    get the maximum bal value of all 8 directions.

    :param bal_list: `list of arrays` the bal value for each of 8 directions

    :return: :class:`numpy.ndarray` the maximum bal value of 8 directions
    """

    stacked_arrays = np.dstack(tuple(bal_list))
    max_of_stack = stacked_arrays.max(2)

    return max_of_stack


def get_slope_in_aspect(slope_data, aspect_data, rows, cols, aspect_value):
    """
    Get the slope data in a specific aspect.

    :param slope_data: :class:`numpy.ndarray` the slope values
    :param aspect_data: :class:`numpy.ndarray` the aspect values
    :param rows: `int` the row number of the slope_data
    :param cols: `int` the column number of the slope_data
    :param aspect_value: `int` the aspect value

    :return: :class:`numpy.ndarray` the slope data in an aspect
    """

    slope_in_aspect = np.zeros((rows, cols), np.float32)
    # -1 means upslope
    slope_in_aspect.fill(-1)
    # if the original slope is nodata, the slope_in_aspect should be nodata
    nodata_location = np.where(slope_data == -99)
    slope_in_aspect[nodata_location] = slope_data[nodata_location]

    same_aspect_location = np.where(aspect_data == aspect_value)
    slope_in_aspect[same_aspect_location] = slope_data[same_aspect_location]

    return slope_in_aspect


def convo(a_dir, veg_data, slope_data, aspect_data, pixel_width, fdi):
    """
    Find the maximum BAL for the point of interest in one direction by
    assessing all neighbours' BAL values in that direction (up to 100 metres).

    :param a_dir: `string` the specific direction
    :param veg_data: :class:`numpy.ndarray` the classified vegetation values
    :param slope_data: :class:`numpy.ndarray` the slope values
    :param aspect_data: :class:`numpy.ndarray` the aspect values
    :param pixel_width: `float` the pixel width of the classified vegetation
    :param fdi: `int` the input FDI value

    :return: :class:`numpy.ndarray` the output BAL values
    """

    dire_aspect = value_lookup.DIRE_ASPECT
    aspect_value = dire_aspect[a_dir]

    # dire_width is the cell span length at the specific direction
    if a_dir in ['w', 'e', 'n', 's']:
        dire_width = pixel_width
    else:
        dire_width = pixel_width * 1.414

    filter_width = int(np.ceil(100.0 / dire_width))

    rows = veg_data.shape[0]
    cols = veg_data.shape[1]

    slope_in_aspect = get_slope_in_aspect(slope_data, aspect_data, rows, cols,
                                          aspect_value)

    outdata = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for jj in range(cols):

            # for pixels whose neighbour amount is less than defined value.
            # e.g here for 25m resolution, it is 4 for hori and vert and 3
            # for diagnoal direction
            all_neighb_dir = value_lookup.ALL_NEIGHB[a_dir](i, jj, rows, cols)

            if all_neighb_dir < filter_width:
                max_neighb_dir = all_neighb_dir
            else:
                max_neighb_dir = filter_width

            slope = np.zeros(max_neighb_dir)
            veg = np.zeros(max_neighb_dir)
            bal = np.zeros(max_neighb_dir)
            dist = np.zeros(max_neighb_dir)

            # if max_neighb_dir is 0, it means no neighbours at this direction
            # so no loop is acted as follows. then the output is nodata
            for m in range(1, max_neighb_dir + 1):
                # get neighbour point location
                point_row = value_lookup.POINT_R[a_dir](i, m)
                point_col = value_lookup.POINT_C[a_dir](jj, m)

                # get neighbour point distance, slope, veg data
                dist[m - 1] = (m - 1) * dire_width + 0.5 * dire_width
                slope[m - 1] = slope_in_aspect[point_row, point_col]
                veg[m - 1] = veg_data[point_row, point_col]

                # calcualte bal for the neighbour point
                bal[m - 1] = bal_esti(veg[m - 1],
                                      dist[m - 1], slope[m - 1], fdi)

            # get the calculated pixel value
            if len(bal) > 0:
                outdata[i, jj] = max(bal)
            else:
                # the boundary data
                outdata[i, jj] = -99

    return outdata


def find_dist_class(dist, dist_limit):
    """
    Decide the BAL class based on the input distance and the distance
    upper-limit for each BAL class.

    :param dist: `float` the horizontal distance from POI
    :param dist_limit: `list` the upper-limit for each BAL class

    :return: `int` the distance class defined in bal_database.py
    """

    if dist < dist_limit[0]:
        dist_class = 1
    elif dist < dist_limit[1]:
        dist_class = 2
    elif dist < dist_limit[2]:
        dist_class = 3
    elif dist < dist_limit[3]:
        dist_class = 4
    else:
        dist_class = 5

    return dist_class


def bal_esti(veg, dist, slope, fdi):
    """
    Calculate the BAL based on the vegetation class, slope degree and
    horizontal distance from the point of interest (POI).

    :param veg: `float` the vegetation type
    :param dist: `float` the horizontal distance from POI
    :param slope: `float` the slope value
    :param fdi: `int` the input FDI value

    :return: `float` the output BAL value for this neighbour point regards to
             the POI
    """

    # nodata area
    if slope == -99:
        bal = -99

    # downslope > 20 degree
    elif slope == bal_database.SLOPE[5]:
        if veg == -99:
            bal = -99
        else:
            bal = 200

    # flat land (0 degree) or upslopes
    elif slope in [-1, bal_database.SLOPE[0]]:
        if veg == -99:
            bal = -99
        else:
            d_limit = bal_database.DIST_LIMIT_UPSLOPE[fdi][veg]
            dist_class = find_dist_class(dist, d_limit)
            bal = bal_database.BAL_CLASS[dist_class]

    # 0 < downslope <= 20 degree
    else:
        if veg == -99:
            bal = -99
        else:
            d_limit = bal_database.DIST_LIMIT_DOWNSLOPE[fdi][(slope, veg)]
            dist_class = find_dist_class(dist, d_limit)
            bal = bal_database.BAL_CLASS[dist_class]

    # if fdi is not 50, if it is grassland, distance is consdiered up to 50m,
    # update bal to nodata
    if fdi != 50 and veg == bal_database.VEG_CLASS[6]:
        if dist >= 50:
            bal = -99

    return bal
