.. _running_bal_training:

Runnning the tool
=================

To calculate the BAL,  we use the **BAL calculation** tool within the **BAL** 
toolbox installed in ArcGIS 10.2.

Select the :menuselection:`BAL --> BAL calculation` tool, see :numref:`select_bal`. 

.. _select_bal:

.. figure:: /docs/images/select_bal.jpg
     :align: center
     :alt: Select the tool **BAL calculation**.
     :figclass: align-center

     Select the tool **BAL calculation**.

Then the **BAL calculation** window is open, see :numref:`bal_window`.

.. _bal_window:

.. figure:: /docs/images/BAL_calculation_window.jpg
     :align: center 
     :alt: The **BAL calculation** window.
     :figclass: align-center

     The **BAL calculation** window.


Getting help from within the toolbox
------------------------------------

On the left of the dialog window is the input fields, options and the
output fields. We will work through these in turn. On the right, help
content for each of the dialog's entry fields are displayed. As you
move to different entry fields the content in this panel will update.

You can toggle the tool help on and off, by clicking the
:guilabel:`Tool Help` button on the lower right corner of the dialog
window.

Another way to access the help is via the menus. Right click on the
:menuselection:`BAL calculation` script and select "Help". This will
display the full help menu for the |project_name|. 

.. _bal_toolbox_help:

.. figure:: /docs/images/001_bal_toolbox_help.png
   :align: center
   :alt: Accessing the BAL Toolbox help menu.
   :figclass: align-center

   Accessing the BAL Toolbox help menu.

Input fields
------------

Input digital elevation model
.............................

The first input field is the digital elevation model. Click the folder
icon button (|folder_icon|) to browse to the location of the required
DEM raster file. The DEM should be in a projected coordinate system,
with a linear unit of metres. Additional information can be found in
the :ref:`dem_projection` section.

.. figure:: /docs/images/001_bal_input_dem.png
   :align: center
   :alt: DEM input field
   :figclass: align-center

   Digital Elevation Model input field.

.. _vegetation_input:

Input classified vegetation raster
..................................



.. figure:: /docs/images/001_bal_input_vegetation.png
   :align: center
   :alt: Classified vegetation input field
   :figclass: align-center

   Classified vegetation raster input field.
