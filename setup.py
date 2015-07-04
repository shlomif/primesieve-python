from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='primesieve',
    url = "https://github.com/hickford/primesieve-python",
    license = "MIT",
    ext_modules = cythonize([Extension(
        "*",
        ["primesieve/primesieve.pyx"],
        include_dirs = ["lib/primesieve/include"],
        libraries = ["primesieve"],
        )])
)
