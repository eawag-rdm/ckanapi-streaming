#!/usr/bin/env python

from setuptools import setup
import sys


install_requires=[
    'setuptools',
    'docopt',
    'requests',
    'requests-toolbelt',
    'clint',
]

if sys.version_info <= (3,):
    install_requires.append('simplejson')


setup(
    name='ckanapi',
    version='999.0.0',
    description=
    'A command line interface and Python module for '
    'accessing the CKAN Action API. Forked from ckanapi with additions '
    'to enable streaming. See https://github.com/ckan/ckanapi/pull/109',
    license='MIT',
    author='Harald von Waldow',
    author_email='harald.vonwaldow@eawag.ch',
    url='https://github.com/eawag-rdm/ckanapi-streaming.git',
    packages=[
        'ckanapi',
        'ckanapi.tests',
        'ckanapi.tests.mock',
        'ckanapi.cli',
        ],
    # A workaround for a bug in setuptools that prevents correct installation
    # of "requests". See http://stackoverflow.com/questions/27497470.
    setup_requires='requests',
    install_requires=install_requires,
    test_suite='ckanapi.tests',
    zip_safe=False,
    entry_points = """
        [console_scripts]
        ckanapi=ckanapi.cli.main:main

        [paste.paster_command]
        ckanapi=ckanapi.cli.paster:CKANAPICommand
        """
    )

