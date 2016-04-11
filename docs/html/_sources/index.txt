.. BAL documentation master file, created by
   sphinx-quickstart on Tue Jul 14 11:29:00 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bushfire Attack Level
===============================




Overview
===========================================


This toolbox is used to compute the Bushfire Attack Level (BAL) for an area of interest within Australia based on the input vegetation and elevation datasets.

The computation algorithm is adapted spatially to Method 1 in the Australian Standard AS 3959 (2009)--*Construction of buildings in bushfire-prone areas*. 
 
The output contains eight raster files that represent the BAL for each of eight cardinal directions and an extra raster file that represents the maximum BAL of the eight directions for each grid cell. 


Disclaimer
==========
.. toctree::
   :maxdepth: 1
   
   Disclaimer <docs/disclaim>


Introduction
============
.. toctree::
   :maxdepth: 1

   Introduction <docs/intro>
   Background <docs/background>


How to use the toolbox
======================
.. toctree::
   :maxdepth: 1

   Installation <docs/install>
   Setting up the toolbox <docs/setup>
   Running the toolbox <docs/execution>
   Examples <docs/examples>


Code documentation
==================

This part is extracted from the source code in-line documentation and included in this document for the completeness of the software package. It does not directly instruct users how to use the toolbox to calculate the BAL. Instead, it might be useful for software engineers or developers to review the source code and maintain or upgrade it in the future.

.. toctree::
   :maxdepth: 2

   docs/bal
   docs/calculate_bal
   docs/utilities


References
==========

AS 3959, 2009. Construction of buildings in bushfire-prone areas, Australian Standard




