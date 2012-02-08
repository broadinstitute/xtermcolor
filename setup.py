import os

from xtermcolor import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

version = '1.0.3'
README = os.path.join(os.path.dirname(__file__), 'README')
long_description = open(README).read()

setup(
  name='xtermcolor',
  version=version,
  description=long_description,
  author='Scott Frazer',
  author_email='sfrazer@broadinstitute.org',
  packages=['xtermcolor'],
  package_data={'xtermcolor': ['distribute_setup.py']},
  install_requires=[],
  entry_points={
    'console_scripts': [
      'xtermcolor = xtermcolor.Main:Cli'
    ]
  },
  license = "MIT",
  keywords = "xterm, ANSI, xterm-256, terminal, color",
  url = "http://github.com/broadinstitute/xtermcolor",
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Terminals :: Terminal Emulators/X Terminals',
    'Topic :: Utilities'
  ]
)
