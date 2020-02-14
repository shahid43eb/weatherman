#!/usr/bin/env python
import sys

from setuptools import setup

py_version = sys.version_info[0]
if py_version < 3:
    raise RuntimeError('Python 3 or greater is required')

setup(
    name='weatherman',
    version='0.1.0',
    author="Shahid Rasaheed",
    author_email="shahid.rasheed@arbisoft.com",
    description="for weather reporting",
    install_requires=['xlrd', 'pandas'],

)
