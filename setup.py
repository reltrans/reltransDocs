#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['numpy']

test_requirements = [ ]

setup(
    author="Matteo Lucchini",
    author_email='m.lucchini@uva.nl',
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: End Users',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
    description="The reltrans model documentation.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='reltrans',
    name='reltrans',
    #packages=find_packages(include=['ndspec']),
    #test_suite='tests',
    #tests_require=test_requirements,
    url='git@github.com:reltrans/reltransDocs.git',
    version='2.3.0',
    zip_safe=False,
)
