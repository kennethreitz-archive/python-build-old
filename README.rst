Python Version Tools
====================

**tl;dr**: Pythonbrew done right.

(work in progress)


Usage
-----

List all available Pythons::

    $ pyenv list
    python-2.5 (python-2.5.6)
    python-2.6 (python-2.6.7)
    python-2.7 (python-2.7.2)
    pypy (pypy-1.6)

Update the cache::

    $ pyenv update
    # Downloads all required files and such.

Build a Python::

    $ pyenv build 2.7

Build all major versions of Python::

    $ pyenv build --all

Build all versions of Python::

    $ pyenv build --all-minor


Config
------

Contents of `~/.pyenv/`:

  `pythons`
    Python installations.
  `cache`
    Dependencies.
  `formula`
    Python version formulas.
