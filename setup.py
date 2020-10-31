# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='kmers',
      version='0.0.1',
      description='Display and count k-mers from the fast file',
      author='Roshan Shrestha',
      packages=['kmers'],
      install_requires=['biopython'])

