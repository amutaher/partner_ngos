# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in partner_ngos/__init__.py
from partner_ngos import __version__ as version

setup(
	name='partner_ngos',
	version=version,
	description='Partner NGOs',
	author='Akram Mutaher',
	author_email='a.mutaher@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
