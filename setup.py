#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

# NOTE: The configuration for the package, including the name, version, and
# other information are set in the setup.cfg file.

import os
import sys

from setuptools import setup


# First provide helpful messages if contributors try and run legacy commands
# for tests or docs.

TEST_HELP = """
Note: running tests is no longer done using 'python setup.py test'. Instead
you will need to run:

    tox -e test

If you don't already have tox installed, you can install it with:

    pip install tox

If you only want to run part of the test suite, you can also use pytest
directly with::

    pip install -e .[test]
    pytest

For more information, see:

  http://docs.astropy.org/en/latest/development/testguide.html#running-tests
"""

if 'test' in sys.argv:
    print(TEST_HELP)
    sys.exit(1)

DOCS_HELP = """
Note: building the documentation is no longer done using
'python setup.py build_docs'. Instead you will need to run:

    tox -e build_docs

If you don't already have tox installed, you can install it with:

    pip install tox

You can also build the documentation with Sphinx directly using::

    pip install -e .[docs]
    cd docs
    make html

For more information, see:

  http://docs.astropy.org/en/latest/install.html#builddocs
"""

if 'build_docs' in sys.argv or 'build_sphinx' in sys.argv:
    print(DOCS_HELP)
    sys.exit(1)

VERSION_TEMPLATE = """
# Note that we need to fall back to the hard-coded version if either
# setuptools_scm can't be imported or setuptools_scm can't determine the
# version, so we catch the generic 'Exception'.
try:
    from setuptools_scm import get_version
    version = get_version(root='..', relative_to=__file__)
except Exception:
    version = '{version}'
""".lstrip()

setup(use_scm_version={'write_to': os.path.join('pyXsurf', 'version.py'),
                       'write_to_template': VERSION_TEMPLATE})

'''
from setuptools import find_packages, setup

# or
from setuptools import find_namespace_packages

"""with this install works only if numpy is already installed, otherwise fails on wheel."""

#p = find_packages('.')
#p = find_packages("src", exclude=["test"]),

setup(
  name='pyXsurf',
  version='1.5.1',
  description="Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.",
  url='https://github.com/vincenzooo/pyXSurf',
  author='Vincenzo Cotroneo',
  author_email='vincenzo.cotroneo@inaf.it',
  install_requires=['wheel','numpy','matplotlib','scipy','IPython','astropy'],
  #package_dir={'': 'pyxsurf'} #this makes me import as old style e.g. from pySurf import data2D, but can create overlapping, e.g. `test` or `plotting` may be used for other things.
  #package_dir={'pySurf': 'pyxsurf/pySurf',
  #             'dataIO': 'pyxsurf/dataIO'}
  package_dir={'': 'source'},
  #packages=p,
  packages = ['pySurf','dataIO','utilities','plotting','pyProfile'],
  setup_requires=['numpy','astropy']
)


"""
#from https://docs.pytho
n.org/3/distutils/setupscript.html

from distutils.core import setup

setup(    name='pyXsurf',
    version='0.1.1',
    packages=['pyXsurf'],
    description="Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.",
    url='https://github.com/vincenzooo/pyXSurf',
    author='Vincenzo Cotroneo',
    author_email='vincenzo.cotroneo@inaf.it',
    #url='https://github.com/vincenzooo/pyXSurf',
    )
"""     
     
""" 

from setuptools import setup
setup(
    name='pyXsurf',
    version='0.1.1',
    packages=['pyXsurf'],
    description="Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.",
    url='https://github.com/vincenzooo/pyXSurf',
    author='Vincenzo Cotroneo',
    author_email='vincenzo.cotroneo@inaf.it',
    keywords=['surfaces', 'metrology', 'PSD'],
    tests_require=[
        'pytest'
    ],
    package_data={
        # include json and pkl files
        '': ['*.json', 'models/*.pkl', 'models/*.json'],
    },
    include_package_data=False,
    python_requires='>=3'
)

# from 

""" 
'''