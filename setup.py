import os

from distutils.core import setup

version = '1.2'
README = os.path.join(os.path.dirname(__file__), 'README')

setup(
  name='xtermcolor',
  version=version,
  description='Python module for colorizing output with xterm 256 color support',
  author='Scott Frazer',
  author_email='sfrazer@broadinstitute.org',
  packages=['xtermcolor'],
  scripts=['scripts/xtermcolor'],
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
