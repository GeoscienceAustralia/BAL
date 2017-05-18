.. _contributing:

Contributing code
=================

The preferred way to contribute to |project_name| is to fork the 
`main repository <http://github.com/GeoscienceAustralia/BAL>`_ on GitHub:

1. Fork the `project repository <http://github.com/GeoscienceAustralia/BAL>`_:
   click on the 'Fork' button near the top of the page. This creates
   a copy of the code under your account on the GitHub server.

2. Clone this copy to your local disk::

          $ git clone git@github.com:YourLogin/bal.git
          $ cd tcrm

3. Create a branch to hold your changes::

          $ git checkout -b my-feature

   and start making changes. Never work in the ``master`` branch!

4. Work on this copy on your computer using Git to manage version
   control. When you're done editing, do::

          $ git add modified_files
          $ git commit

   to record your changes in Git, then push them to GitHub with::

          $ git push -u origin my-feature

Finally, go to the web page of the your fork of the BAL repo,
and click 'Pull request' to send your changes to the maintainers for
review. This will send an email to the code managers.

(If any of the above seems like magic to you, then look up the 
`Git documentation <http://git-scm.com/documentation>`_ on the web.)

It is recommended to check that your contribution complies with the
following rules before submitting a pull request:

-  All public methods should have informative docstrings with sample
   usage presented as doctests when appropriate.

-  When adding additional functionality, provide at least one
   example script in the ``examples/`` folder. Have a look at other
   examples for reference. Examples should demonstrate why the new
   functionality is useful in practice.

-  At least one paragraph of narrative documentation with links to
   references in the literature (with PDF links when possible) and
   an example.

You can also check for common programming errors with the following
tools:

-  Check your code complies with good unittest coverage::

          $ pip install nose coverage
          $ nosetests --with-coverage path/to/tests_for_package
