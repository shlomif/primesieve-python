from setuptools import setup, Extension
from Cython.Build import cythonize
from glob import glob

library = ('primesieve', dict(
    sources=glob("lib/primesieve/src/primesieve/*.cpp"),
    include_dirs=["lib/primesieve/include"],
    language="c++",
    ))

extension = Extension(
        "primesieve",
        ["primesieve/primesieve.pyx"],
        include_dirs = ["lib/primesieve/include"],
        language="c++",
        )

setup(
    name='primesieve',
    url = "https://github.com/hickford/primesieve-python",
    license = "MIT",
    libraries = [library],
    ext_modules = cythonize(extension),
    packages = ['primesieve'],
)
