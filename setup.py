from distutils.core import setup

import pyelife

with open('LICENSE') as fp:
    license = fp.read()

setup(name='pyelife',
      version=pyelife.__version__,
      packages=['pyelife'],
      license = license
      )