from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('invokebilizer/_version.py') as fp:
    exec (fp.read(), None, _locals)
__version__ = _locals['__version__']

setup(name='invokebilizer',
      version=__version__,
      packages=[
          'invokebilizer',
      ],
      install_requires=[
          'invoke>=0.10,<0.14',
          'six'
      ],
      tests_require=[
          'nose',
          'tox',
      ])
