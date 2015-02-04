from distutils.core import setup

with open('LICENSE') as fp:
    license = fp.read()

setup(name='pyelife',
      version='0.0.1',
      py_modules=['pyelife'],
      license = license
      )