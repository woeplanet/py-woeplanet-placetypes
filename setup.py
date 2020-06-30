#!/usr/bin/env python

import os, sys
from shutil import rmtree
from setuptools import setup, find_namespace_packages

pkgname = 'woeplanet.docs.placetypes'
cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egginfo = '%s/%s.egg-info' % (cwd, pkgname)
if os.path.exists(egginfo):
    rmtree(egginfo)

version = open('VERSION').read()
nspkgs = find_namespace_packages(include=['woeplanet.*'])

setup(
    name=pkgname,
    python_requires='>3',
    packages=nspkgs,
    version=version,
    description='Simple Python wrapper for accessing WoePlanet/GeoPlanet placetypes in Elasticsearch',
    author='Gary Gale',
    url='https://github.com/woeplanet/py-woeplanet-placetypes',
    download_url='https://github.com/woeplanet/py-woeplanet-placetypes/releases/tag/' + version,
    license='BSD-3-Clause'
)
