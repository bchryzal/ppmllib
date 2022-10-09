# Chryzal Beaudelaire ZOSSOU 2022
# Performance Profiles for Machine Learning Python library
# Author: Chryzal Beaudelaire ZOSSOU <bchryzal@gmail.com>
#
# License: MIT


from os.path import dirname, join, realpath

from setuptools import find_packages, setup

import ppmllib

VERSION = ppmllib.__version__
PROJECT_ROOT = dirname(realpath(__file__))

REQUIREMENTS_FILE = join(PROJECT_ROOT, "requirements.txt")

with open(REQUIREMENTS_FILE) as f:
    install_reqs = f.read().splitlines()

install_reqs.append("setuptools")


from setuptools import find_packages, setup

setup(
  name='ppmllib',
  packages=find_packages(),
  version=VERSION,
  description='Performance Profiles for Machine Learning Python library',
  author='Chryzal Beaudelaire ZOSSOU',
  author_email="bchryzal@gmail.com",
  license='MIT',

  package_data={
    "": ["README.md", "requirements.txt"]
  },

  include_package_data=True,
  install_requires=install_reqs,
  platforms="any",

  classifiers=[
      "License :: MIT",
      "Development Status :: 5 - Production/Stable",
      "Operating System :: Microsoft :: Windows",
      "Operating System :: POSIX",
      "Operating System :: Unix",
      "Operating System :: MacOS",
      "Programming Language :: Python :: 3.7",
      "Topic :: Scientific/Engineering",
      "Topic :: Scientific/Engineering :: Artificial Intelligence",
      "Topic :: Scientific/Engineering :: Information Analysis",
      "Topic :: Scientific/Engineering :: Machine Learning",
  ],

  setup_requires=['pytest-runner'],
  tests_require=['pytest==4.4.1','pytest-runner==4.4'],
  test_suite='tests',

  long_description=""" 
    PPML de ouf!
  """
)