from distutils.core import setup

setup(name='delete',
      version='10.1',
      author='Debathena Project',
      author_email='debathena@mit.edu',
      scripts=['delete', 'undelete', 'lsdel', 'expunge'],
      py_modules=['libdelete.py'])
