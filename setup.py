#!/usr/bin/env python
from setuptools import find_packages, setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='testpkg',
    version='1.0',
    author='Luc DURON',
    author_email='l.duron@cnr.tm.fr',
    packages=find_packages(),
    include_package_data=True,  # includes all non `.py` files found inside package directory (see MANIFEST.in)
    install_requires=requirements,
    description='Minimal Python package with a data file',
    url='https://github.com/CNR-Engineering/testpkg',
)
