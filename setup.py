#!/usr/bin/env python
import setuptools
import pymuse

setuptools.setup(
    name='pymuse',
    version=pymuse.__version__,
    packages=['pymuse'],
    author="PREVOST Corentin",
    author_email="cocauw@gmail.com",
    description="Library for musical theory analysis of MIDI format",
)
