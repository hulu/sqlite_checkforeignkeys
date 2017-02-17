#!/usr/bin/env python
"""The standard setup.py file"""

from setuptools import setup, find_packages


setup(
    name='sqlite_checkforeignkeys',
    version='1.0.3',
    author='McKay Salisbury',
    author_email='mckay.salisbury@hulu.com',
    description='A sqlite engine that checks foreign keys',
    keywords=['foreign key', 'sqlite'],
    packages=['sqlite_checkforeignkeys_engine'],
    long_description=
    'This references the django sqlite engine and overrides one of its methods. '
    'When a new connection is created it [turns on the foreign key checking as per the sqlite '
    'documentation](http://www.sqlite.org/foreignkeys.html)'
)
