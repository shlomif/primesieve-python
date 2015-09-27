from setuptools import setup, Extension
from glob import glob
from distutils.command.build_ext import build_ext
from distutils.command.build_clib import build_clib

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

class build_clib_subclass(build_clib):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions"""
    def build_libraries(self, libraries):
        if self.compiler.compiler_type == "msvc" and int(self.compiler._MSVCCompiler__version) <= 9:
            for lib_name, build_info in libraries:
                build_info['include_dirs'].append("lib/primesieve/src/msvc_compat")
                print(build_info)
        build_clib.build_libraries(self, libraries)

class build_ext_subclass(build_ext):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions"""
    def build_extensions(self):
        if self.compiler.compiler_type == "msvc" and int(self.compiler._MSVCCompiler__version) <= 9:
            for e in self.extensions:
                e.include_dirs.append("lib/primesieve/src/msvc_compat")
        build_ext.build_extensions(self)

setup(
    name='primesieve',
    version="0.1.0",
    url = "https://github.com/hickford/primesieve-python",
    description="Fast prime number generator. Python bindings around C++ library primesieve",
    license = "MIT",
    libraries = [library],
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext_subclass, 'build_clib' : build_clib_subclass},
    classifiers=[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ],
)
