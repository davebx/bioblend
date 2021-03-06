# http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

import ast
import os.path
import re
import sys

from setuptools import setup, find_packages

# Cannot use "from bioblend import get_version" because that would try to import
# the six package which may not be installed yet.
reg = re.compile(r'__version__\s*=\s*(.+)')
with open(os.path.join('bioblend', '__init__.py')) as f:
    for line in f:
        m = reg.match(line)
        if m:
            version = ast.literal_eval(m.group(1))
            break

tests_require = ['mock>=0.7.0', 'nose>=1.3.1']
if sys.version_info < (2, 7):
    tests_require.append('unittest2>=0.5.1')

setup(name="bioblend",
      version=version,
      description="CloudMan and Galaxy API library",
      author="Enis Afgan",
      author_email="afgane@gmail.com",
      url="http://bioblend.readthedocs.org/",
      install_requires=['requests>=2.4.3', 'requests-toolbelt', 'boto>=2.9.7', 'pyyaml', 'six'],
      tests_require=tests_require,
      packages=find_packages(),
      license='MIT',
      platforms="Posix; MacOS X; Windows",
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Topic :: Internet",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7"],
      test_suite='nose.collector',
      )
