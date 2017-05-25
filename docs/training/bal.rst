.. _whatisbal:

What is the Bushfire Attack Level
=================================

The Bushfire Attack Level measures the **severity of a building's
potential exposure** to ember attack, radiant heat and direct flame
contact. It is intended to improve the resistance of buildings to
bushfire attack from burning embers, radiant heat, flame contact or a
combination of these. It applies to buildings sited in designated
bushfire-prone areas, as defined in the National Construction Code, Volume 2
[NCCV2]_.

By improving the ability of buildings in bushfire-prone areas to
withstand attack from bushfire, there is an increase in the protection
afforded to building occupants (until the fire front passes) as well
as to the building itself.

However, improving the design and construction of buildings is only
one way that property owners can address the damage caused by
bushfire. Other measures fall within the areas of planning,
subdivision, siting, landscaping and maintenance.

.. note:: It should be borne in mind that the measures contained in
          this Standard cannot guarantee that a building will survive
          a bushfire event on every occasion. This is substantially
          due to the degree of vegetation management, the
          unpredictable nature and behaviour of fire, and extreme
          weather conditions (AS 3959--2009). 

The bushfire attack level is a measure of the severity of a building's
potential exposure to ember attack, radiant heat and direct flame
contact, using increments of radiant heat expressed in kilowatts per
metre squared. When calculated, the |project_name| toolbox provides
classified levels:

* BAL--LOW
* BAL--12.5
* BAL--19
* BAL--29
* BAL--40
* BAL--FZ

Appendix G in AS 3959--2009 describes the threats associated with each BAL.

.. determinebal:

How do we determine BAL
=======================

The |project_name| toolbox applies Method 1 from AS 3959--2009 to
determine the BAL. Method 1 is a simplified procedure to determine the
BAL, which involves five steps. This method is subject to limitations
on the circumstances in which it can be used.

.. warning:: This method is not valid where the effective slope under
             the classified vegetation is more than 20 degrees
             downslope. Within the BAL toolbox, where the slope is
             greater than 20 degrees, a constant value of 200 is
             assigned to the BAL.

There are five steps in determining the BAL based on method 1 in AS 3959--2009. 

Step 1: Determine the relevant FDI

Step 2: Determine the classified vegetation type(s)

Step 3: Determine the distance of the site from the classified
vegetation type(s)

Step 4: Determine the effective slope(s) under the classified
vegetation type(s)

Step 5: Determine the BAL from the appropriate table

.. note:: AS 3959-2009 includes a sixth step, which refers to
          construction requirements. This is not of interest in the
          BAL toolbox, so is omitted here.

The following sections provide details on determining the BAL, using
|project_name|.

Determine relevant FDI
----------------------

The relevant Fire Danger Index (FDI) is based on Table 2.1 from AS
3959--2009, for each jurisdiction or region within a jurisdiction. The
FDI is an indication of the chance of a fire starting, its rate of
spread, intensity and the difficulty of suppresion based on the
combination of air temperature, relative humidity, wind speed and both
long- and short-term drought effects. The FDI used in AS 3959--2009
refers to the Forest Fire Danger Index calculated by the McArthur Mk 5
Forest Fire Danger Meter using the equations published by Noble *et
al.* (1980) [1]_.

.. table:: Jurisdictional and regional values for FDI (adapted from
           Table 2.1, `AS 3959, 2009 
           <https://www.saiglobal.com/online/Script/Details.asp?DocN=AS819920597136>`_).
   :widths: 50, 10

   +----------------------------------------------------+---------+
   | **State/region**                                   |   FDI   |
   +----------------------------------------------------+---------+
   | **Australian Capital Territory**                   |   100   |
   +----------------------------------------------------+---------+
   | **New South Wales**                                |    -    |
   +----------------------------------------------------+---------+
   | (a) Greater Hunter, Greater Sydney,                |         |
   |     Illawarra/Shoalhaven, Far South Coast,         |   100   |
   |                                                    |         |
   |     and Southern Ranges fire weather districts     |         |
   +----------------------------------------------------+---------+
   | (b) NSW alpine areas                               |   50    |
   +----------------------------------------------------+---------+
   | (c) NSW general (excluding alpine areas, Greater   |         |
   |     Hunter, Greater Sydney,                        |         |
   |                                                    |   80    |
   |     Illawarra/Shoalhaven,Far South Coast and       |         |
   |     Southern Ranges fire weather districts)        |         |
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


.. _classified_vegetation:

Vegetation classification
-------------------------

The vegetation of the site is classified in accordance with the
guidance provided in Table 2.3 and the corresponding figures in AS
3959--2009. Where there is more than one vegetation type, each
vegetation type is classified separately with the worst case scenario
applied. For example, if there is a mix of grassland and shrubland,
then the vegetation would be classified as shrubland, as this results
in a higher BAL. 

.. note:: The predominant vegetation type of a site may not
          necessarily be the worst case scenario.

In general, the land cover datasets often only present the predominant
vegetation type. Therefore, we cannot always determine the "worst
case" value of BAL. This could also be determined by validation on the 
ground.

AS 3959--2009 provides a list of exclusions for low threat vegetation
and non-vegetated areas, where the BAL is classified as LOW. This
includes vegetation greater than 100 metres from the site, small (< 1
ha) areas of vegetation that are also more than 100 metres from other
vegetation and low threat vegetation that includes grassland managed
in minimal fuel conditions. This includes lawns, golf courses,
orchards and cultivated gardens, amongst others. Non-vegetated areas
include waterways, roads, buildings, footpaths and rocky outcrops.

Table 2.3 in AS 3959--2009 sets out seven major vegetation
classifications::
  
* Forest
* Woodland
* Shrubland
* Scrub
* Mallee/mulga
* Rainforest
* Grassland

Each of these major vegetation classifications has between one and
eleven types, each of which has an indicative figure in the
Standard. See Figures 2.3 and 2.4(A) to 2.4(G) in the Standard for
these figures. There is also a brief text description of the
vegetation types (height, foliage cover, habit, etc.).

.. note:: Overstoreys of open woodland, low open woodland, tall open
          shrubland and low open shrubland should be classified to the
          vegetation type on the basis of their understoreys; others
          to be classified on the basis of their overstoreys.

Distance to vegetation
----------------------

The distance to from the site to the classified vegetation is measured
in the *horizontal plane*.

.. figure:: /docs/images/001_bal_vegetation_distance.png
   :align: center
   :width: 300 pt
 
   Determination of distance from site from classified vegetation. The
   measurement is the horizontal distance, from Point A to
   Point B. From AS 3959--2009.

In the above figure, the distance from the classified vegetation to
the site is the same in all three cases, irrespective of the slope
over the intervening distance. In |project_name|, the effective
distance is measured betwen the centre of grid cells of the input
raster elevation data. 

Effective slope under the classified vegetation
-----------------------------------------------

In determining BAL, 'slope' refers to the slope under the vegetation
in relation to the building. It is not the slope between the
vegetation and the site. The slope of the land under the classified
vegetation has a direct influence on the rate of fire spread, the
severity of the fire and the ultimate level of radiant heat flux.

The definition of upslope and downslope is the definition of the
slope, relative to the site being evaluated. If the slope of the land
under the classified vegetation is **downhill** from the edge of the
classified vegetation nearest the site, then the slope is considered
**downslope**. If the slope of the land under the classified
vegetation is **uphill** from the edge of the classified vegetation
nearest the site, then the slope is considered **upslope**.

.. figure:: /docs/images/001_bal_effective_slope.png
   :align: center
   :width: 300 pt

   Determination of effective upslope and downslope. From AS
   3959--2009.

Determine BAL from appropriate table
------------------------------------

AS 3959-2009 provides a set of lookup tables, from which we can
determine the BL based on a combination of the FDI, distance from
classified vegetation and effective slope.




.. [NCCV2] National Construction Code,
           Volume 2. http://www.abcb.gov.au/Resources/Publications/NCC/NCC-2016-Volume-Two
.. [1] Noble, I. R., G. A. V. Bary and A. M. Gill (1980): McArthur's
       fire-danger meters expressed as equations. *Australian Journal
       of Ecology*, **5**, pp 201--203,
       DOI:10.1111/j.1442-9993.1980.tb01243.x
