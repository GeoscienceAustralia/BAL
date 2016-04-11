Installation
============

Installing BAL Toolbox is intended to be a simple process, requiring only basic understanding of ArcGIS toolbox operations. It has been installed and tested on ArcGIS 10.2.


Unzipping the toolbox
---------------------

The software package is delivered as a compressed zip file. Unzip the toolbox into a location on your computer, for example C:\\bal. Then you will have stored all the files at folder C:\\bal. 


Dependencies
------------

This toolbox is developed and tested within ArcGIS 10.2 that integrates with Python 2.7 and Numpy 1.6.2. It is not recommended to install an independent version of Python for use in ArcGIS. Using a different version of Python may lead to compatibility issues.

However, if necessary, there are several ways to obtain the required libraries -- using Python's recommended tool `pip
<https://pip.readthedocs.org/en/latest/>`_, installing a distribution such as `Python(x,y) package <http://python-xy.github.io/>`_ (for Windows environments), or installing the libraries from source or binary installers (pre-compiled binary Windows installer versions for all the libraries (both 32-bit and 64-bit) can be obtained `here <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_).

For detailed instructions on installation of these dependencies, please see the documentation for each individual library.

* `Python <https://www.python.org/>`_ - v2.7 preferred
* `Numpy <http://www.numpy.org/>`_ - v1.6.2 preferred
* `Arcpy in ArcGIS 10.2 <http://resources.arcgis.com/en/help/main/10.2/index.html#//000v000000v7000000/>`_

Setting the environment 
----------------------- 
To enable BAL toolbox to run flawlessly, you may need to change some environment settings. The important variable to set is the ``PYTHONPATH`` variable. This should be set to the path where you have extracted the contents of the zip file. A complete discussion on environment variables in Python is given in the `Python documentation <https://docs.python.org/2/using/cmdline.html#environment-variables>`_. 

Windows 
~~~~~~~ 
The Python documentation contains some simple instructions for setting environment variables on Windows systems `here <https://docs.python.org/2/using/windows.html>`_. See `this link <http://www.computerhope.com/issues/ch000549.htm>`_ for setting the variables on different Windows systems. 

Testing the installation
------------------------

The code includes a suite of unit tests that ensure elements of the code base work as expected. The code should be tested before running the toolbox.

The test suite can be run from the main directory. On Windows, run the ``run_test_all.cmd`` script from the main BAL directory. 


