#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
from filezen.version import VERSION
__version__ = VERSION


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='Filezen',
    author='Abhinav Anand',
    version=VERSION,
    author_email='abhinavanand1905@gmail.com',
    description="An Intelligent file organizer module that reads your file storing pattern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ab-anand/Filezen',
    license='MIT',
    install_requires=[
            "pathlib >= 1.0.1",
            "setuptools >= 44.1.1"
        ],
    # dependency_links=dependency_links,
    # adding package data to it
    packages=find_packages(exclude=['contrib', 'docs']),
    download_url='https://github.com/ab-anand/Filezen/tarball/' + __version__,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System",
        "Topic :: System :: Operating System",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
    keywords=['Operating System', 'Utility', 'Automation', 'Heaps', 'File Organizer']
)
