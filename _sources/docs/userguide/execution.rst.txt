.. |beta|   unicode:: U+003B2 .. GREEK SMALL LETTER BETA

.. _execution:

================
Running the tool
================

To calculate the BAL,  we use the **BAL calculation** tool within the **BAL** toolbox installed in ArcGIS 10.2.

Select the **BAL calculation** tool within the **BAL** toolbox, see Figure 5.1.

.. figure:: /docs/images/select_bal.jpg
     :align: center
     :alt: Select the tool **BAL calculation**.
     :figclass: align-center

     Figure 5.1 Select the tool **BAL calculation**.

Then the **BAL calculation** window is open, see Figure 5.2.

.. figure:: /docs/images/BAL_calculation_window.jpg
     :align: center 
     :alt: The **BAL calculation** window.
     :figclass: align-center

     Figure 5.2 The **BAL calculation** window.

Parameters within the tool
==========================

**Input DEM raster:**
           
	Open your input DEM file from a specific location. The DEM is
	required to be in a projected coordinate system with linear
	unit metre. For example GDA94 / MGA zone 50 is a projected
	spatial reference system and is suitable for use in the
	western part of Western Australia. More information about
	GDA94 / MGA zone 50 can be found `here
	<http://spatialreference.org/ref/epsg/gda94-mga-zone-50/>`_.

**Input vegetation raster:**
    
	Open your input vegetation dataset from a specific location. 
    The vegetation dataset can be in either a
	geographical or a projected coordinate system. It will be
	reprojected to the same projection and same resolution as DEM
	by the BAL tool.

**Vegetation reclassification:** 
          
	Reclassify the input vegetation classes into those defined in
	the Australian Standard AS 3959 (2009). There are seven
	classes defined in the Standard. In this tool, we give each
	class a unique number, i.e.:

	* 1: Forest, 
	* 2: Woodland, 
	* 3: Shrubland, 
	* 4: Scrub, 
	* 5: Mallee/Mulga, 
	* 6: Rainforest, 
	* 7: Grassland/Tussock moorland. 

	The reclassification process needs to be considered by the user, 
    and will vary according to the input vegetation dataset. 
    
    A sample reclassification map is entered for the example data. 
    The reclassification map needs to be changed by the users according 
    to their own input vegetation data.

**Output path:** 
          
	Define the output location. Note that this is asking for a folder to
    write the output to, not a file name.

**FDI value:**
     
	The input Fire Danger Index (FDI) value has four choices (100,
	80, 50, 40) based on the locations, which are specified in the
	Australian Standard AS 3959 (2009).

	* **100**: Australian Capital Territory (ACT), part of New South
          Wales (NSW) (Greater Hunter, Greater Sydney,
          Illawarra/Shoalhaven, Far South Coast and Southern Ranges
          fire weather districts), and Victoria general (excluding
          alpine areas).
	* **80**: NSW general (excluding alpine areas, and the areas with
          FDI 100), South Australia (SA), and Western Australia (WA).
	* **50**: NSW alpine areas, Tasmania, and Victoria alpine areas.
	* **40**: Northern Territory (NT), and Queensland (Qld).
      
	Select the FDI value from a suite of values (100, 80, 50,
	40). It is optional. The default value of 80 is
	applicable in Western Australia.

**Extent:**
          
	The extent is used to select the area of interest for which the
	BAL will be calculated. The default output data extent will be where
	you have consistent coverage of DEM and vegetation data within
	the area of interest.

.. note:: * There is a limitation in raster file name length and file path
          length in ArcGIS. For a raster name in ESRI Grid format, the maximum
          number of characters is 13 and for full path name, the maximum
          number of character is 128. For more information, `click here
          <http://resources.arcgis.com/EN/HELP/MAIN/10.2/index.html#//018700000009000000>`_. In
          addition, as tested, each folder name's length should be restricted
          to at most eight characters.
          * The script requires that the input DEM and vegetation dataset are in
          the same location. The tool will fail to run when the input DEM and
          vegetation datasets are not in the same folder.


Output
======

A suite of rasters are produced and stored in the output folder. They
represent the BAL for the area computed in each of eight cardinal
directions (E, S, W, N, NE, NW, SE and SW) and the maximum BAL of all
directions. Figure 5.3 is an example output.

.. figure:: /docs/images/BAL_output.jpg
     :align: center
     :alt: An example BAL output window.
     :figclass: align-center

     Figure 5.3 An example BAL output window.


