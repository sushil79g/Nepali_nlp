#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from structure import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# the setup
setup(
    name='Nepali nlp',
    version=__version__,
    description='Natural language processing library for Nepali langauge',
    # long_description=read('README'),
    url='https://github.com/sushil79g/Nepali_nlp',
    author=['Anish Pandey','Sushil Ghimire'],
    author_email=['sharmaanix@gmail.com','sushil79g@gmail.com'],
    license='MIT',
    keywords='NLP ml ai nepali',
    packages=find_packages(exclude=('docs', 'tests', 'env', 'index.py')),
    include_package_data=True,
    install_requires=[
    ],
    extras_require={
    'dev': [],
    'docs': [],
    'testing': [],
    },
    classifiers=[],
    )
