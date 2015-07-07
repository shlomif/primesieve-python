from setuptools import setup, Extension
from glob import glob

library = ('primesieve', dict(
    sources=glob("lib/primesieve/src/primesieve/*.cpp"),
    include_dirs=["lib/primesieve/include"],
    language="c++",
    ))

if glob("primesieve/*.pyx"):
    from Cython.Build import cythonize
else:
    # fallback to compiled cpp
    cythonize = None

extension = Extension(
        "primesieve",
        ["primesieve/primesieve.pyx"] if cythonize else ["primesieve/primesieve.cpp"],
        include_dirs=["lib/primesieve/include", "lib/primesieve/include/primesieve"],
        language="c++",
        )

ext_modules = cythonize(extension) if cythonize else [extension]

setup(
    name='primesieve',
    version="0.0.2",
    url = "https://github.com/hickford/primesieve-python",
    description="Fast prime number generator. Python bindings around C++ library primesieve",
    license = "MIT",
    libraries = [library],
    ext_modules = ext_modules,
    classifiers=[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    ],
)
