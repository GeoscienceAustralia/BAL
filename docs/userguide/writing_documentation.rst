.. _writing_documentation:

Writing Documentation
=====================

The documentation for |project_name| is written using ReSTructured text (.rst)
and the Sphinx documentation builder.

The best way to learn how to write .rst is to look at the source of existing
documentation - the markup syntax is very simple.
There are a number of useful tags that you can use to make your documentation
clear and visually interesting, those more commonly used in this document are
listed below.
For a more detailed list, please visit the
`Sphinx Inline Markup page <http://sphinx.pocoo.org/markup/inline.html>`_.

A complete list of supported .rst markup is also available
`here <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#block-quotes>`_.

Here are a few tips for documentation writers:

1. Take a look in the `lookup table <./lookup_table.html>`_ to see which terms
   and phrases are used and which you should definitely **not** translate.
#. There is a "Community Edition" of
   `PyCharm <http://www.jetbrains.com/pycharm/>`_ available.
   Consider using this for writing documentation.
#. Try to not write more than **80 Characters in one line**.
   That makes the documentation much easier to maintain.
#. Try to create a reference anchor for at least every new heading (page).
   If it is useful and important you might also want to put anchors on
   subheadings.
#. Try to avoid duplicate target names (anchors).
   Always use unique identifiers.
   If you are not sure - the longer the name the more unlikely it is already used.
#. Try to use underscores (_) in filenames and links (anchors) as a separator.
#. Try to use dashes (-) in directory names as a separator.
#. Try to avoid using tables wherever possible.
   Only use tables if there is really no other way to display the
   documentation.
#. If you have to use tables try to avoid using TABS in favour of SPACES.
   TABS only confuse the computer while building documentation and leads to
   unnecessary errors.

.. _common_tags:

Common tags used in the Documentation:
--------------------------------------

Here are some useful tags
::

   |project_name|   is currently a substitution for the Project name (Bushfire Attack Level)
   Normally, there are no heading levels assigned to certain characters as the
   structure is determined from the succession of headings. However, for the
   Python documentation, this convention is used, which you may follow:

   # with overline, for parts
   * with overline, for chapters

   First two are normaly not used as we usually start with a section.

   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

   Section
   =======

   SubSection
   ----------

   Subsubsection
   .............

   Subsubsubsection (if needed)
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **bold**

   *italics*

   `web link<http://foo.org>`_  Link to a named external reference

   :ref:`my-reference-label`    points to a reference which has to be
                                implemented like:

   ..  _my-reference-label:     The anchor for the :ref: needs to be
                                in front of a Section.
   Section to cross-reference   Like it is here.
   --------------------------

   :ref:`title <my-reference-label>` Same as above except using the Title and
                                     not the referenced headline.

   :doc:`../user-docs/filename` referencing an internal file

   :samp:`flood [m]`            A piece of literal text, such as code.

   :menuselection:`Plugins --> Manage Plugins`  This is used to mark a complete
                                                sequence of menu selections,
                                                including selecting submenus.

   :guilabel:`OK`   Labels presented as part of an interactive user interface
                    should be marked using guilabel.

   :kbd:`Control-x Control-f` Mark a sequence of keystrokes.

   :command:`rm` (The name of an OS-level command, such as rm.)

   :file:`/etc/fstab` to change something

   .. note:: Note in a little call out box

   .. todo:: Todo item in a call out box

   .. warning:: Much like Note but clearly visible

   There are more markers available:

   .. attention::
   .. caution::
   .. danger::
   .. error::
   .. hint::
   .. important::
   .. tip::

   .. table:: table title

   ============  ================
     Key         Allowed Values
   ============  ================
   units         m
   units         wet/dry
   units         feet
   ============  ================

   +-----------------------+-----------------------+
   | Symbol                | Meaning               |
   +=======================+=======================+
   | .. image:: tent.*     | Campground            |
   +-----------------------+-----------------------+
   | .. image:: waves.*    | Lake                  |
   +-----------------------+-----------------------+
   | .. image:: peak.*     | Mountain              |
   +-----------------------+-----------------------+

    figure and images are easily exchangeable when using * instead of jpg or
    png. In that way the Pictures can be exchanged to a new format without
    changing the source code.

    .. figure:: picture.*
       :scale: 50 %
       :alt: map to buried treasure
       :figwidth: lenght or percentage of current line width
       :figclass: text

        This is the caption of the figure (a simple paragraph).

    .. image:: /static/tutorial/001.*
       :height: 100 px
       :width: 200 pt
       :scale: 50 %
       :alt: alternate text
       :align: center

remark: use pt instead of px because of latex output
* A4 = height ~ 1000pt
* A4 = width ~ 700pt

Help writing/fixing documentation
---------------------------------

Helping to write the documentation is an easy task.
The only thing you need to have is a local copy of the |project_name|
documentation branch.

Clone |project_name| documentation
..................................

.. note:: This is a one-time process. You do not need to repeat it - it is
          here for reference purposes only.
  
In order to help with documentation, you need:

* A GitHub account
* A fork of the BAL repository (only if you do not have commit access to
  the main repository)

Creating a GitHub account is done by clicking on the :guilabel:`Sign up for free`
button on https://github.com/ and filling out the necessary fields.

Cloning the documentation of |project_name| is easy; you only have to follow
this procedure:

.. note:: This documentation assumes that you have the whole |project_name| source
          available under :file:`$HOME/dev/python/...`

Clone your forked github |project_name| documentation by entering following
command::

         $ git clone https://github.com/<your username>/bal.git

Search for the .rst file you'd like to extend/fix and work on it.

Afterwards commit your local changes to your local clone with the command::

         $ git commit -a -m "fixed a typo"

After that you have to push your local changes to your github fork with::

         $ git push

You can then do a pull request on github to request your changes be
reviewed and added into the official documentation.
