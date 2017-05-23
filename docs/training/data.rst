.. _data_requirements:

Data requirements
=================

|project_name| requires only two datasets to determine BAL -- a
classified vegetation dataset and a digital elevation model. With
these two datasets, it is possible to determine the slope and aspect
of a site, and the classified vegetation types described in AS
3959--2009, to enable determination of BAL.

Digital elvation model
----------------------

A digital elevation model (DEM) is a digital model that represents a
geographic location's height above mean sea level. DEM's are developed
by a wide range of techniques, and widely varying horizontal grid
resolutions.

At the national scale, Geoscience Australia has published the
1-arcsecond Shuttle Radar Topography Mission (SRTM) Digital Elevation
Models Version 1.0 (see
http://www.ga.gov.au/metadata-gateway/metadata/record/gcat_72759),
which is freely accessible. This DEM has a grid resolution of
approximately 30 m by 30 m (at the equator). There are also other
DEM's available through the `Geoscience Australia Data and
Publications Search portal
<http://www.ga.gov.au/search/index.html#/>`_. Other organisations may
have higher-resolution and more up-to-date DEMs available for use in
the |project_name|.

For the |project_name|, it is recommended to use a DEM with a
horizontal grid resolution comparable to the SRTM DEM, or higher for
best results.

Format
......

Any `raster format supported by ESRI ArcGIS 10.2
<http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/supported-raster-dataset-file-formats.htm>`_
can be used in |project_name|. 32-bit floating point data in either
GeoTIFF or the native ESRI Grid format is recommended.

Vegetation data
---------------

A classified vegetation dataset is required for determination of
BAL. The availability of classified vegetation datasets is varied, and
the clssifications used are similarly diverse, depending on the
application for which they were intended and the methods used to
derive them.

For the examples used in this training workshop, we have used the
`National Vegetation Information System (NVIS)
<http://www.environment.gov.au/land/native-vegetation/national-vegetation-information-system>`_,
which provides information on the extent and distribution of
vegetation types in Australian landscapes. This data has a horizontal
resolution of 100 m by 100 m. Other organisations may have
higher-resolution and more up-to-date classified vegetation datasets
available for use in the |project_name|.

For optimal results, it is recommended to use a classified vegetation
dataset that is of a comparable resolution to the DEM used.

Format
......

Any `raster format supported by ESRI ArcGIS 10.2
<http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/supported-raster-dataset-file-formats.htm>`_
can be used in |project_name|. Generally, an unsigned integer data
type will be sufficient to describe the classified vegetation
type. Either GeoTIFF or the native ESRI Grid format is recommended.


Classification
..............

The vegetation data needs to represent different classification
types. Ideally, the data will match the vegetation classes set out in
AS 3959--2009. These are numbered 1--7 and are defined as follows:

.. table:: Classification of vegetation. After Table 2.3, AS 3959--2009.

+-------+------------------+----------------------------------------------+
| Value | Classification   | Description                                  |
+-------+------------------+----------------------------------------------+
|   1   | Forest           | Tall, open forest, tall woodland, open       |
|       |                  |                                              |
|       |                  | forest, low open forest, pine plantation     |
+-------+------------------+----------------------------------------------+
|   2   | Woodland         | Woodland, open woodland, low woodland, low   | 
|       |                  |                                              | 
|       |                  | open woodland, open shrubland                |
+-------+------------------+----------------------------------------------+
|   3   | Shrubland        | Closed heath, open heath, low shrubland      |
+-------+------------------+----------------------------------------------+
|   4   | Scrub            | Closed scrub, open scrub                     |
+-------+------------------+----------------------------------------------+
|   5   | Mallee/Mulga     | Tall shrubland                               |
+-------+------------------+----------------------------------------------+
|   6   | Rainforest       | Tall closed forest, closed forest, low       |
|       |                  |                                              | 
|       |                  | closed forest                                |
+-------+------------------+----------------------------------------------+
|   7   | Grassland        | Low open shrubland, hummock grassland,       |
|       |                  |                                              |
|       |                  | closed tussock grassland, tussock grassland, | 
|       |                  |                                              |
|       |                  | open tussock, sparse open tussock, dense     |
|       |                  |                                              |
|       |                  | sown pasture, sown pasture, open herbfield,  |
|       |                  |                                              |
|       |                  | sparse open herbfield                        |
+-------+------------------+----------------------------------------------+


The input data must be in this numerical format for the |project_name|
to execute correctly. Values other than those listed here will be
ignored and may produce incorrect BAL values.

The |project_name| provides users with the option to map their
classified vegetation to the required classes. By default, the mapping
matches the numerical values from NVIS to the required AS 3959--2009
values.

