#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This is the setup file for the project."""

# yapf: disable

from __future__ import unicode_literals

import sys

from setuptools import find_packages
from setuptools import setup

try:  # for pip >= 10
  from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
  from pip.req import parse_requirements


# make sure turbinia is in path
sys.path.insert(0, '.')

import turbinia  # pylint: disable=wrong-import-position

turbinia_description = (
    'Turbinia is an open-source framework for deploying, managing, and running'
    'forensic workloads on cloud platforms. It is intended to automate running '
    'of common forensic processing tools (i.e. Plaso, TSK, strings, etc) to '
    'help with processing evidence in the Cloud, scaling the processing of '
    'large amounts of evidence, and decreasing response time by parallelizing'
    'processing where possible.')

setup(
    name='turbinia',
    version=turbinia.__version__,
    description='Automation and Scaling of Digital Forensics Tools',
    long_description=turbinia_description,
    license='Apache License, Version 2.0',
    url='http://turbinia.plumbing/',
    maintainer='Turbinia development team',
    maintainer_email='turbinia-dev@googlegroups.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['turbiniactl=turbinia.turbiniactl:main']},
    install_requires=[str(req.req) for req in parse_requirements(
        'requirements.txt', session=False)
    ],
    extras_require={
        'dev': ['mock', 'nose', 'yapf', 'celery~=4.1', 'coverage'],
        'local': ['celery~=4.1', 'kombu~=4.1', 'redis~=3.0'],
        'worker': ['plaso>=20171118', 'pyhindsight>=2.2.0']
    }
)
