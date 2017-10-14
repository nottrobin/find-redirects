#! /usr/bin/env python3

# Core
import sys
from setuptools import setup

# The importer relies heavily on glob recursive search capability.
# This was only introduced in Python 3.5:
# https://docs.python.org/3.6/whatsnew/3.5.html#glob
assert sys.version_info >= (3, 5), (
    "upload-assets requires Python 3.5 or newer"
)

setup(
    name='canonicalwebteam.find-redirects',
    version='0.1.0',
    author='Canonical webteam',
    author_email='robin+pypi@canonical.com',
    url='https://github.com/canonical-webteam/find-redirects',
    packages=[
        'canonicalwebteam.find_redirects',
    ],
    description=(
        'Find URLs that lead to 301 or 302 redirects '
        'in the specified set of files. '
        'Optionally, update the redirected URLs in-place to their '
        'targets URLs.'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        'requests[security]>=2.13.0'
    ],
    scripts=['find-redirects']
)
