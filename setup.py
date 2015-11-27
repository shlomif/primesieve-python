from setuptools import setup, Extension
from glob import glob
from distutils.command.build_ext import build_ext
from distutils.command.build_clib import build_clib
import os
import shutil
import subprocess
import tempfile

extensions = []
extra_compile_args = []
extra_link_args = []

# If this C/C++ test program compiles the compiler supports OpenMP
# http://stackoverflow.com/questions/16549893/programatically-testing-for-openmp-support-from-a-python-setup-script
omp_test = \
    r"""
    #include <omp.h>
    #include <stdio.h>

    int main()
    {
        #pragma omp parallel
        printf("Hello from thread %d, nthreads %d\n", omp_get_thread_num(), omp_get_num_threads());
        return 0;
    }
    """

# Get the current compiler's OpenMP flag
def get_compiler_openmp_flag():
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)
    filename = r'omp_test.c'
    openmp_flag = ""

    try:
        cc = os.environ['CC']
    except KeyError:
        cc = 'cc'
    with open(filename, 'w', 0) as file:
        file.write(omp_test)

    # Compile test program using different OpenMP compiler flags
    with open(os.devnull, 'w') as fnull:
        exit_code = subprocess.call([cc, '-fopenmp', filename], stdout=fnull, stderr=fnull)
        if exit_code == 0:
            openmp_flag = '-fopenmp'
        else:
            exit_code = subprocess.call([cc, '-openmp', filename], stdout=fnull, stderr=fnull)
            if exit_code == 0:
                openmp_flag = '-openmp'
            else:
                exit_code = subprocess.call([cc, '/openmp', filename], stdout=fnull, stderr=fnull)
                if exit_code == 0:
                    openmp_flag = '/openmp'

    #clean up
    os.chdir(curdir)
    shutil.rmtree(tmpdir)
    return openmp_flag

openmp_flag = get_compiler_openmp_flag()
print 'get_compiler_openmp_flag():', openmp_flag
extra_compile_args.append(openmp_flag)
extra_link_args.append(openmp_flag)

library = ('primesieve', dict(
    sources = glob("lib/primesieve/src/primesieve/*.cpp"),
    include_dirs = ["lib/primesieve/include"],
    language = "c++",
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args
    ))

if glob("primesieve/*.pyx"):
    from Cython.Build import cythonize
else:
    # fallback to compiled cpp
    cythonize = None

extensions.append(Extension(
        "primesieve.core",
        ["primesieve/core.pyx"] if cythonize else ["primesieve/core.cpp"],
        include_dirs = ["lib/primesieve/include"],
        language = "c++",
        extra_compile_args = extra_compile_args,
        extra_link_args = extra_link_args
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
        include_dirs = ["lib/primesieve/include", numpy_include_dir],
        language = "c++"
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
    name = 'primesieve',
    version = "0.1.3",
    url = "https://github.com/hickford/primesieve-python",
    description = "Fast prime number generator. Python bindings for primesieve C/C++ library",
    license = "MIT",
    libraries = [library],
    packages = ["primesieve", "primesieve.numpy"],
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext_subclass, 'build_clib' : build_clib_subclass},
    classifiers = [
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
