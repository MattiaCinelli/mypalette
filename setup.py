from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Needed for dependencies
INSTALL_REQUIRES = [
      'wheel',
      'numpy >= 1',
      'pandas == 1.1.4',
      'webcolors == 1.11.1',
      'matplotlib == 3.3.2',
      
]

setup(name = 'mypalette',
      version = '1.0.1.2',

      url = 'https://github.com/MattiaCinelli/mycolorpalette',
      description = 'Define and manage your plot colors in Python',
      long_description_content_type = 'text/markdown',
      long_description = long_description,
      
      packages = find_packages(),
      install_requires = INSTALL_REQUIRES,
      python_requires = '>=3.7',

      author = 'Mattia Cinelli',
      author_email = '',
      license = 'MIT',

      zip_safe = False
      )
