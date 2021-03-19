#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Oscar Martínez'
__copyright__ = 'Copyleft 2021'
__date__ = '19/03/21'
__credits__ = ['Oscar Martínez', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martínez'
__email__ = 'omartinez@ifae.es'

import os

import setuptools
from setuptools import find_packages

# Read README and CHANGES files for the long description
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as fh:
      long_description = fh.read()

# print(find_packages(exclude=('tests',)))
setuptools.setup(
      name="pyvsr53dl",
      version="0.1.0",
      description="Python Library to interface with Thyracont's VSR53DL Vacuum Sensor through RS458 interface",
      long_description_content_type="text/markdown",
      long_description=long_description,
      install_requires=[''],
      python_requires='>=3',
      provides=[""],
      author="Oscar Martínez",
      author_email="omartinez@ifae.es",
      license="CC0 1.0 Universal",
      url="https://github.com/IFAEControl/pyvsr53dl",
      zip_safe=False,
      classifiers=[
                   "Development Status :: 4 - Beta",
                   "Programming Language :: Python :: 3",
                  ],
      package_dir={'': 'src'},
      packages=find_packages(where=os.path.join('.', 'src'), exclude=('tests',))
)