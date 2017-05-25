.. _installation:

Installation
============

Installing BAL Toolbox is intended to be a simple process, requiring
only basic understanding of ArcGIS toolbox operations. It has been
installed and tested on ArcGIS 10.2.


Unzipping the toolbox
---------------------

The software package is delivered as a compressed zip file. Unzip the
toolbox into a location on your computer, for example :file:`C:\\bal`. Then
you will have stored all the files at folder :file:`C:\\bal`.


Dependencies
------------

* `Python <https://www.python.org/>`_ - v2.7 
* `Numpy <http://www.numpy.org/>`_ - v1.6.2
* `Arcpy in ArcGIS 10.2 <http://resources.arcgis.com/en/help/main/10.2/index.html#//000v000000v7000000/>`_

.. warning:: ArcGIS 10.2 is packaged with a modified version of
             ``Numpy``. In our experience, attempting to update the
             ``Numpy`` package will cause the ``arcpy`` package to fail
             catastrophically, and usually without reporting any error
             message. We strongly recommend against trying to upgrade
             the version of ``Numpy`` linked to your ``ArcGIS``
             installation.

Setting the environment 
------------------------ 

To enable BAL toolbox to run flawlessly, you may need to change some
environment settings. The important variable to set is the
``PYTHONPATH`` variable. This should be set to the path where you have
extracted the contents of the zip file. A complete discussion on
environment variables in Python is given in the `Python documentation
<https://docs.python.org/2/using/cmdline.html#environment-variables>`_.

Windows 
~~~~~~~~
 
The Python documentation contains some simple instructions for setting
environment variables on Windows systems `here
<https://docs.python.org/2/using/windows.html>`_. See `this link
<http://www.computerhope.com/issues/ch000549.htm>`_ for setting the
variables on different Windows systems.

Testing the installation
------------------------

The code includes a suite of unit tests that ensure elements of the
code base work as expected. The code should be tested before running
the toolbox. Users will need to install the `Nose
<http://nose.readthedocs.io/en/latest/index.html>`_ package to run
these tests.

The test suite can be run from the main directory. On Windows, run the
:command:`run_test_all.cmd` script from the main BAL directory.


If the test suite fails, there will be a message indicating which
test failed and a description of the failure. If you receive this, copy
the description and create a ticket on the |project_name| `Issue
Tracker <https://github.com/GeoscienceAustralia/BAL/issues>`_. 
