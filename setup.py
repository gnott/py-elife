from distutils.core import setup

import pyelife

with open('README.md') as fp:
    readme = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

setup(name='pyelife',
      version=pyelife.__version__,
      description='Simple python distribution - testing.',
      long_description=readme,
      packages=['pyelife'],
      license = license
      )