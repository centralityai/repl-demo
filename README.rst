REPL Demo
=========
This is a companion repository for the article,
"`Building REPLs for Fun and Profit`_".  Download this repository to your
computer so that you can try out the examples from the article.

Each file in this repository corresponds to one of the examples in the article:

- ``deep_thought/repl_basic.py`` shows how to start a basic Python REPL.
- ``deep_thought/repl_ipython.py`` shows how to start an IPython REPL.
- ``deep_thought/repl_compat.py`` shows how to support IPython if installed,
  using vanilla Python as a fallback.
- ``deep_thought/repl_cli.py`` iterates on the idea and uses the `click`_
  library to add command-line arguments to the REPL script.
- ``setup.py`` defines additional metadata so that the REPL can be installed as
  a regular command-line application.

Dependencies
------------
The code in this repository has been tested against Python 3.6.

If you encounter any issues, make sure you are using the latest version of
setuptools (``pip install --upgrade setuptools``).

Installation
------------
#. (optional but highly recommended) Create a `virtualenv`_.
#. For a quick start, run ``pip install -e .`` to install dependency
   libraries, and then you can run any of the code examples in the
   ``deep_thought`` package.
#. To try out the IPython REPLs, you will also need to install `IPython`_:
   ``pip install ipython``

The article "`Building REPLs for Fun and Profit`_" will take you step-by-step
through each of the scripts, so that you can get more information about exactly
what's happening in each one.


.. todo Fix URL

.. _Building REPLs for Fun and Profit: https://medium.com/centrality/building-repls-for-fun-and-profit-597ae4fcdd85
.. _click: http://click.pocoo.org
.. _IPython: https://ipython.readthedocs.io
.. _virtualenv: https://docs.pipenv.org/#install-pipenv-today
