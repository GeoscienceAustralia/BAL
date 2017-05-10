Background
============

The algorithm used to calculate the BAL is based on Method 1 in the
Australian Standard AS 3959 (2009)--*Construction of buildings in
bushfire-prone areas*.

Method 1 is a simplified procedure that involves five steps to
determine BAL, and is subject to limitations on the circumstances in
which it can be used.

.. warning:: This method does not apply to the circumstances where the
             effective slope under the classified vegetation is more
             than 20 degrees downslope.

Procedure to determine BAL
--------------------------

According to the Standard AS 3959 (2009), five steps are involved to
calculate BAL.


Step 1
++++++

Select the relevant FDI based on the locations according to Table 2.1
in the Australian Standard AS 3959 (2009). For example, from Table
2.1, the FDI for Western Australia is 80.

.. table:: Jurisdictional and regional values for FDI (adapted from
           Table 2.1, AS 3959, 2009).
   :widths: 50, 10

   +----------------------------------------------------+---------+
   | **State/region**                                   |   FDI   |
   +----------------------------------------------------+---------+
   | **Australian Capital Territory**                   |   100   |
   +----------------------------------------------------+---------+
   | **New South Wales**                                |    -    |
   +----------------------------------------------------+---------+
   | (a) Greater Hunter, Greater Sydney,                |         |
   |     Illawarra/Shoalhaven, Far South Coast, and     |   100   |
   |     Southern Ranges fire weather districts         |         |
   +----------------------------------------------------+---------+
   | (b) NSW alpine areas                               |   50    |
   +----------------------------------------------------+---------+
   | (c) NSW general (excluding alpine areas, Greater   |         |
   |     Hunter, Greater Sydney, Illawarra/Shoalhaven,  |   80    |
   |     Far South Coast and Southern Ranges fire       |         |
   |     weather districts)                             |         |
   +----------------------------------------------------+---------+
   | **Northern Territory**                             |   40    |
   +----------------------------------------------------+---------+
   | **Queensland**                                     |   40    |
   +----------------------------------------------------+---------+
   | **South Australia**                                |   80    |
   +----------------------------------------------------+---------+
   | **Tasmania**                                       |   50    |
   +----------------------------------------------------+---------+
   | **Victoria**                                       |    -    |
   +----------------------------------------------------+---------+
   | (a) Victoria alpine areas                          |   50    |
   +----------------------------------------------------+---------+
   | (b) Victoria general (excluding alpine areas)      |   100   |
   +----------------------------------------------------+---------+
   | **Western Australia**                              |   80    |
   +----------------------------------------------------+---------+ 

.. note:: The FDI values may be able to be refined within a
          jurisdiction or region where sufficient climatological data
          is available and in consultation with the relevant
          regulatory authority.

.. note:: The FDI values were provided by the Australasian Fire and
          Emergency Service Authorities Council (AFAC).

.. note:: Alpine and sub-alpine areas are defined as per the National
          Construction Code, Volume 2 [NCCV2]_.

Step 2
++++++

Classify the input vegetation dataset into seven vegetation types
defined in Table 2.3 in the Standard AS 3959 (2009). AS 3959 also
provides indicative illustrations of the range of vegetation types. 

* 1: Forest, 
* 2: Woodland, 
* 3: Shrubland, 
* 4: Scrub, 
* 5: Mallee/Mulga, 
* 6: Rainforest, 
* 7: Grassland/Tussock moorland. 

Where there is more than one vegetation type, then the classification
should be based on that which results in the worst case scenario. When
used in a spatial framework, the digital classification is likely to
correspond to the predominant vegetation in a grid cell, which is not
necessarily the worst case scenario. 

The numbers from 1 to 7 are assigned to these vegetation classes
respectively for calculating BAL.

Step 3
++++++

Calculate the distance of the site from the classified
vegetation. According to AS 3959 (2009), the vegetation is considered
when its distance from the site of interest is within 100 metres.

Step 4
++++++

Determine the effective slopes (the gradient from each cell) and their
aspects under the classified vegetation types. If a slope's aspect is
in the same direction as the vegetation from the site, this slope is
regarded as a downslope that will be further analysed. Otherwise the
slope is regarded as an upslope.

When calculating BAL, upslopes and flat lands are treated as a single
category. For downslopes, the Standard breaks them down into five
classes:

* 0 < downslope <= 5 degrees
* 5 < downslope <= 10 degrees
* 10 < downslope <= 15 degrees
* 15 < downslope <= 20 degrees
* > 20 degrees (beyond consideration of Method 1)

Step 5
++++++

Determine the BAL from an appropriate table defined in AS 3959 (2009)
based on the input FDI. For example, for Western Australia, the FDI is
80 and thus Table 2.4.3 is adopted for deriving the BAL.

Deriving and interpreting BAL
-----------------------------

We consider eight cardinal directions: north, northeast, east,
southeast, south, southwest, west, and northwest.

For each cardinal direction, we consider the neighbouring cells up to
100 metres from the site. We calculate the BAL for each neighbouring
cell with regards to the site based on the neighbouring cell's
vegetation type, upslope or downslope degrees, and its distance to the
site.

The BAL falls into a list of (12.5, 19, 29, 40, 100), where 100
represents Fire Zone (FZ). There is one more circumstances beyond
Method 1 in AS 3959 (2009).

* Where the downslope is greater than 20 degrees and there is
  vegetation, a constant value of 200 is given to the BAL.

The maximum BAL is selected among all neighbouring cells in a given
cardinal direction to represent the BAL for that direction.

The final BAL for the site of interest is determined by selecting the
maximum BAL from all eight cardinal directions.



.. [NCCV2] National Construction Code, Volume 2. http://www.abcb.gov.au/Resources/Publications/NCC/NCC-2016-Volume-Two
.. [AS3959] Construction of buildings in bushfire-prone areas (2009). Standards Australia.
