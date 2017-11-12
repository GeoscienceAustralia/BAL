The Bushfire Attack Level Computation Software 
==============================================

This software is an ESRI ArcGIS 10.2 toolbox used to produce Bushfire
Attack Level (BAL), a measure of the severity of a building's
potential exposure to bushfire. The algorithm is based on Method 1 in
Australian Standard AS 3959 (2009)--*Construction of buildings in
bushfire-prone areas*.

Dependencies 
------------

This toolbox is developed and tested within ArcGIS 10.2 that
integrates with Python 2.7 and Numpy 1.6.2.

For more information on installation of the toolbox, see
[docs/install.rst](https://github.com/GeoscienceAustralia/BAL/blob/master/docs/install.rst),
or the [User
Guide](https://github.com/GeoscienceAustralia/BAL/blob/master/docs/BAL.pdf).

For detailed instructions on installation of these dependencies,
please see the documentation for each individual library.

* [Python](https://www.python.org/)- v2.7 preferred
* [Numpy](http://www.numpy.org/)- v1.6.2 preferred
* [Arcpy in ArcGIS 10.2](http://resources.arcgis.com/en/help/main/10.2/index.html#//000v000000v7000000/)

Usage
-----

First download the repository into your local computer,
e.g. C:\\bal. where you will find **BAL.tbx**. Then add the toolbox
into ArcGIS 10.2 following the steps below:

* Open the ArcToolBox window. 

* Right click **ArcToolbox** at the top of the window.

* Select **Add Toolbox...**, a dialog box is open. 

* In the dialog box, navigate to the location of the package, for
  example C:\\bal.

* Select **BAL.tbx** and click **Open**, a new toolbox called **BAL**
  is added to the ArcToolbox.

Testing the installation
------------------------

The code includes a suite of unit tests that ensure elements of the
code base work as expected. The code should be tested before running
the toolbox. Users will need to install the Nose package to run these
tests.

The test suite can be run from the main directory. On Windows, run the
run_test_all.cmd script from the main BAL directory.


License
-------

This repository is licensed under an Apache Version 2.0 license. See
the [LICENSE deed](LICENSE) in this repository for details.



Contacts
-------- 
**Craig Arthur**  
Geoscience Australia  
craig.arthur@ga.gov.au  

**Claire Krause**  
Geoscience Australia  
claire.krause@ga.gov.au  

**Tina Yang**  
Geoscience Australia  
tina.yang@ga.gov.au  
