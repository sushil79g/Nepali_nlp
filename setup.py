""" Package setup """
import os
# from pip.req import parse_requirements
from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(
    name='Nepali nlp',
    description='Natural language processing library for Nepali langauge',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sushil79g/Nepali_nlp',
    author=['Anish Pandey','Sushil Ghimire'],
    author_email=['sharmaanix@gmail.com','sushil79g@gmail.com'],
    license='MIT',
    keywords='NLP ml ai nepali',
    packages=find_packages(exclude=('docs', 'tests', 'env', 'index.py')),
    include_package_data=True,
    install_requires=required,
    dependency_links = ["https://github.com/sushil79g/spello_memory.git"],
    extras_require={
    'dev': [],
    'docs': [],
    'testing': [],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License"
    ],
    project_urls={
    "Bug Reports": "https://github.com/sushil79g/Nepali_nlp/issues",
    "Source": "https://github.com/sushil79g/Nepali_nlp",
    }
)
