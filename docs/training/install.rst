.. _install_training:

Installing the |project_name|
=============================

Instructions for installing the |project_name| are given in the
:ref:`User Guide <installation>` and :ref:`Set up <setup>` sections.



Testing the installation
------------------------

.. important:: Testing the installation before using it will allow you
               to identify any issues with the installation of the
               |project_name| before using it. Without testing the
               toolbox first, you may obtain results that are
               inconsistent with the intented application of the
               toolbox.

The code includes a suite of unit tests that ensure elements of the
code base work as expected. The code should be tested before running
the toolbox. Users will need to install the `Nose
<http://nose.readthedocs.io/en/latest/index.html>`_ package to run
these tests.

The test suite can be run from the main directory. On Windows, run the
:command:`run_test_all.cmd` script from the main BAL directory.

.. figure:: /docs/images/001_bal_unittest_execution.png
   :align: center
   :width: 300 pt
   
   Running the BAL test suite in a Windows command prompt.

.. figure:: /docs/images/001_bal_unittest_complete.png
   :align: center
   :width: 300 pt
   
   Windows command prompt showing successful completion of the test
   suite. Notice the last few messages indicating the number of tests
   and "OK".

If the test suite fails, then there will be a message indicating which
test failed and a description of the failure. If you get this, copy
the description and create a ticket on the |project_name| `Issue
Tracker <https://github.com/GeoscienceAustralia/BAL/issues>`_. 


Adding the toolbox into ArcGIS 10.2
-----------------------------------

Follow the steps below to add the |project_name| into ArcGIS 10.2:

* Open the ArcToolbox window. See :numref:`arctoolbox1`.
  
.. _arctoolbox1:

.. figure:: /docs/images/arctoolbox.jpg
     :align: center
     :alt: ArcToolbox window.
     :figclass: align-center

     The ArcToolbox window.

* Right click **ArcToolbox** at the top of the window, see
  :numref:`rightclickarctoolbox1`.
 
.. _rightclickarctoolbox1:

.. figure:: /docs/images/rightclick_arctoolbox.jpg
     :align: center
     :alt: Right click ArcToolbox in the ArcToolbox window.
     :figclass: align-center

     Right click **ArcToolbox** in the ArcToolbox window.

* Select **Add Toolbox...**, a dialog box is open. See
  :numref:`addtoolboxdialog1`.
 
.. _addtoolboxdialog1:

.. figure:: /docs/images/addtoolbox_dialog.jpg
     :align: center
     :alt: Add toolbox dialog window.
     :figclass: align-center

     The **Add Toolbox** dialog window.

* In the dialog box, navigate to the location of the package, for 
  example :file:`C:\\bal`, you will find the **BAL.tbx**. See :numref:`addtoolboxdialog1`.


* Select **BAL.tbx** and click **Open**, a new toolbox called **BAL**
  is added to the ArcToolbox. See :numref:`baltoolboxloaded1`.
 
.. _baltoolboxloaded1:

.. figure:: /docs/images/BAL_toolbox.jpg
     :align: center
     :alt: BAL toolbox is added.
     :figclass: align-center

     The **BAL** toolbox is added.

 
