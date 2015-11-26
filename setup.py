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

extensions = []

extensions.append(Extension(
        "primesieve.core",
        ["primesieve/core.pyx"] if cythonize else ["primesieve/core.cpp"],
        include_dirs=["lib/primesieve/include"],
        language="c++",
        ))

def is_pypy():
    import platform
    try:
        if platform.python_implementation() == 'PyPy':
            return True
    except AttributeError:
        pass
    return False

def can_import(module_name):
    """can_import(module_name) -> module or None"""
    try:
        return __import__(module_name)
    except ImportError:
        return None

def is_Numpy_installed():
    if is_pypy():
        return False
    return bool(can_import("numpy"))

# Add primesieve.numpy extension if NumPy is installed
if is_Numpy_installed():
    import numpy
    numpy_include_dir = numpy.get_include()
    extensions.append(Extension(
        "primesieve.numpy.core",
        ["primesieve/numpy/core.pyx"] if cythonize else ["primesieve/numpy/core.cpp"],
        include_dirs=["lib/primesieve/include", numpy_include_dir],
        language="c++",
        ))

ext_modules = cythonize(extensions) if cythonize else [extensions]

def old_msvc(compiler):
    """Test whether compiler is msvc <= 9.0"""
    return compiler.compiler_type == "msvc" and hasattr(compiler, "_MSVCCompiler__version") and int(compiler._MSVCCompiler__version) <= 9

class build_clib_subclass(build_clib):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions"""
    def build_libraries(self, libraries):
        if old_msvc(self.compiler):
            for lib_name, build_info in libraries:
                build_info['include_dirs'].append("lib/primesieve/src/msvc_compat")
                print(build_info)
        build_clib.build_libraries(self, libraries)

class build_ext_subclass(build_ext):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions"""
    def build_extensions(self):
        if old_msvc(self.compiler):
            for e in self.extensions:
                e.include_dirs.append("lib/primesieve/src/msvc_compat")
        build_ext.build_extensions(self)

setup(
    name='primesieve',
    version="0.1.3",
    url = "https://github.com/hickford/primesieve-python",
    description="Fast prime number generator. Python bindings for primesieve C/C++ library",
    license = "MIT",
    libraries = [library],
    packages = ["primesieve", "primesieve.numpy"],
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
