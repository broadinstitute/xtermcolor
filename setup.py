import os
from setuptools import setup, find_packages

version = '1.0.0'
README = os.path.join(os.path.dirname(__file__), 'README')
long_description = open(README).read()

setup(
  name='xtermcolor',
  version=version,
  description=long_description,
  author='Scott Frazer',
  author_email='sfrazer@broadinstitute.org',
  packages=['xtermcolor'],
  package_dir={'xtermcolor': 'xtermcolor'},
  install_requires=[],
  entry_points={
    'console_scripts': [
      'xtermcolor = xtermcolor.Main:Cli'
    ]
  },
  license = "GPL",
  keywords = "xterm, ANSI, xterm-256, terminal, color",
  url = "http://github.com/broadinstitute/xtermcolor",
  classifiers=[]
)
