import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'testpackage'
AUTHOR = 'Rajesh Balakrishnan'
AUTHOR_EMAIL = 'rajeshbalakrishan24@email.com'
URL = 'https://github.com/you/your_package'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Collection Machine Learning algorithm beyond papers'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'tensorflow',
      'scikit-learn',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )