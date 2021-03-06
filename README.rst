pyXsurf
====================

Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org
    :alt: Powered by Astropy Badge

Installation
------------

Download or clone the project. You can use git clone command by:
``git clone https://github.com/vincenzooo/pyXSurf.git`` or the button
``download`` at top of page.
At this point you have two options:

1. Python installer (suggested): move to the folder with the code and call
``python setup.py install``

2. Manual (developer): put the folder with code in a path accessible to 
python on your system (generally this means it must be in the system path) 
and start using it. In this case you must install
all dependencies by yourself.

Developers branches can be installed in the same way and they should work equally (just have more unfinished stuff), so the only thing you need to do differently, is to switch branch (e.g. ``git checkout documentation``, if ``documentation`` is the name of the branch) before running the setup. Please check developers notes for a list of active branches and their features.   

Status of the library
--------------------------------

The main part of the library is well defined and it works well. I am
constantly adding functions when I find they are needed during my daily
work. 

I have tried the installation on a few computers and it worked smoothly by `setup.py`. You are very welcome to help signaling any problem or missing information, please see :ref:`Contributing` below.

If everything worked well with the installation, there
are a decent number of tutorial and examples, but they are quite scattered around in
folders ``Demo``, ``Tutorial``, ``Test``, etc. 

You should be able to access information by usual python introspection (``?``, ``??``, autocompletion, etc.).

See developer notes :ref:`developersnotes` for a detailed status of developement, how to access more recent features and last status of documentation (on developer brach), especially if you think you can help.
Expecially installation and release mechanism, are in phase of improvement, as well as documentation.

Contributing
--------------------------------

Please report bugs or feature requests, missing documentation, or open a issue on github.

Expecially appreciated is if you can provide templates, examples or hints on how to handle, documentation (Sphinx), packaging, continuous integration (Github).

Please check :ref:`developersnotes` for the status of the development, or if you think you can help in any way. 


Modules
-------

A basic description of the different modules is: 

* **dataIO** Generic routines for accessing and manipulating data and files. 

* **notebooks**  Jupyter notebooks, not necessarily related to the libraries, include test and experiments on python. 

* **plotting** Plotting functions for pySurf data. 

* **pyGeo3D** Functions for geometry in space (lines and planes). 

* **pyProfile** Equivalent of pySurf acting on Profiles. 

* **pySurf** Functions and classes acting on 3D points or surfaces. 

* **thermal** Functions for modelling of thermal forming of glass.

Some examples and data can be found in a ``test`` subfolder of each
module.

Citation
--------

.. image:: https://zenodo.org/badge/165474659.svg
   :target: https://zenodo.org/badge/latestdoi/165474659


License
-------

This project is Copyright (c) Vincenzo Cotroneo and licensed under
the terms of the BSD 3-Clause license. This package is based upon
the `Astropy package template <https://github.com/astropy/package-template>`_
which is licensed under the BSD 3-clause license. See the licenses folder for
more information.


Author
------

Vincenzo Cotroneo vincenzo.cotroneo@inaf.it