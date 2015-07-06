from setuptools import setup, Extension
from glob import glob

library = ('primesieve', dict(
    sources=glob("lib/primesieve/src/primesieve/*.cpp"),
    include_dirs=["lib/primesieve/include"],
    language="c++",
    ))

try:
    from Cython.Build import cythonize
except ImportError:
    # fallback to compiled cpp
    cythonize = None

extension = Extension(
        "primesieve",
        ["primesieve/primesieve.pyx"] if cythonize else ["primesieve/primesieve.cpp"],
        include_dirs = ["lib/primesieve/include"],
        language="c++",
        )

ext_modules = cythonize(extension) if cythonize else [extension]

setup(
    name='primesieve',
    url = "https://github.com/hickford/primesieve-python",
    license = "MIT",
    libraries = [library],
    ext_modules = ext_modules,
)
