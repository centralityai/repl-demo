REPL Demo
=========
This is a companion repository for the article,
`Building REPLs for Fun and Profit`_.  Download this repository to your computer
so that you can try out the examples from the article.

Each file in this repository corresponds to one of the examples in the article:

- ``deep_thought/repl_basic.py`` shows how to start a basic Python REPL.
- ``deep_thought/repl_ipython.py`` shows how to start an IPython REPL.
- ``deep_thought/repl_compat.py`` shows how to support IPython if installed,
  using vanilla Python as a fallback.
- ``deep_thought/repl_cli.py`` iterates on the idea and uses the `click`_
  library to add command-line arguments to the REPL script.
- ``setup.py`` defines additional metadata so that the REPL can be installed as
  a regular command-line application.


.. todo Fix URL

.. _Building REPLs for Fun and Profit: https://centrality.ai
.. _click: http://click.pocoo.org/
