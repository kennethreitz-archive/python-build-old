#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup


def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

# required = ['clint>=0.2.1', 'github2', 'requests']

# if sys.version_info[0:2] < (2, 6):
#     required.append('simplejson')

setup(
    name='pyenv',
    version='0.0.0',
    description='Builds Pythons.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/pyenv',
    packages= ['pyenv'],
    # install_requires=required,
    license='MIT',
    classifiers=(
#       'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
    entry_points = {
        'console_scripts': [
            'pyenv = python.cli:main'
        ]
    }
)
