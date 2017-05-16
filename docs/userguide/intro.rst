Introduction
============

Fire is a natural feature of the Australian landscape and remains an
ever-present threat. Bushfire threat analysis aims to inform the fire
authorities and the community of the bushfire hazard in an effort to
manage the risk posed to life, property and the environment.

Bushfire Attack Level (BAL) is a measure of the severity of a
building's potential exposure to bushfire. It is defined in the
`Australian Standard AS 3959 (2009)--*Construction of buildings in
bushfire-prone areas* <http://www.as3959.com.au/>`_, to serve as a 
basis for establishing the requirements for construction, to improve 
the protection of buildings from bushfire attack. The Standard 
describes how to compute the bushfire attack level for any location 
and directly links this to recommendations on the design of existing 
or planned buildings.

The BAL toolbox implements the rules described by Method 1 in AS
3959 (2009) by integrating them into a computational code that can be
run in the ESRI ArcGIS 10.2 environment.


Package structures
------------------

The toolbox name is **BAL.tbx**. This toolbox is associated with a
python script, **bal.py**, to derive BAL. The script **bal.py** links
to a python script **calculate_bal.py** and a module **Utilities**,
which includes supporting dictionaries defined in two python scripts:
 
* value_lookup.py;
* bal_database.py.

There are three more folders:

* **docs**: holding the documentation files.

* **tests**: holding the unit tests, scenario tests and their test data.

* **examples**: holding the example input and output data.   


Use limitations
---------------

The BAL tool developed in Geoscience Australia (GA) has been developed
and tested in ArcGIS 10.2. However, GA does not guarantee that the
information derived is totally accurate or complete. Therefore, you
should not solely rely on this information. Key limitations and
approximations include the following:

* The BAL is produced based on the simplified method (Method 1) in AS
  3959 (2009). When the land downslope is more than 20 degrees, more
  detailed method (Method 2) should be adopted. Method 2 has not been
  incorporated into the BAL toolbox. Instead, a constant value
  of 200 is provided as BAL for such circumstances.

* Elevation data is a critical input of the tool. Digital Elevation
  Model (DEM) with finer resolution usually leads to more accurate BAL
  results. The example data uses a DEM with a resolution of 1 second
  of arc (approximate 30 m by 30 m grid cell at the equator), the best
  available national scale elevation dataset at the time of
  modelling. As with all spatial analyses, the results are sensitive
  to the input DEM's quality, resolution, coverage and currency and
  should therefore be used with this understanding.

* Vegetation data is another critical input into the tool. Method 1 in
  AS 3959 (2009) considers the vegetation up to 100 metres from the
  site of interest. Ideally a vegetation dataset with finer resolution
  (preferred at metre level) is required to derive sensible BAL
  analyses. Where finer vegetation data is not available, the
  alternative coarse vegetation data may lead to inaccurate output
  BAL.

* The BAL toolbox is intended to run in the ArcGIS toolbox environment
  and is not intended to run in a Python script environment.

* This software algorithm adapts the Method 1 in AS 3959 (2009) by
  modelling it spatially. Readers are assumed to be familiar with AS
  3959 (2009). For the detailed description of the Method 1, please
  refer to the `Standard AS 3959 (2009) <http://www.as3959.com.au/>`_.




