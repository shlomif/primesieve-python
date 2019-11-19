"""Setup file for primesieve Python bindings."""

import distutils.ccompiler
from distutils.command.build_ext import build_ext  # type: ignore
from glob import glob
import os
import platform
import shutil
import subprocess
import sys
import tempfile

from setuptools import Extension, setup

# The primesieve package (https://pypi.python.org/pypi/primesieve)
# distributes the generated C++ rather than the pyx file.
# So Cython isn't needed as a dependency.
if glob("primesieve/*.pyx"):
    from Cython.Build import cythonize
    module_file_ext = 'pyx'
else:
    module_file_ext = 'cpp'

# --------------------- Initialization ------------------------------

extensions = []
extra_compile_args = []
if not sys.platform.startswith('win'):
    extra_compile_args.append('-std=c++11')
extra_link_args = []
include_dirs = []

# --------------------- Get OpenMP compiler flag --------------------


def get_compiler_openmp_flag():
    """Get OpenMP compiler flag."""
    # If this C test program compiles the compiler supports OpenMP
    # http://stackoverflow.com/a/16555458/363778
    omp_test = \
        r"""
        #include <omp.h>
        #include <stdio.h>
        int main()
        {
            #pragma omp parallel
            printf("Hello from thread %d, nthreads %d\n",
                    omp_get_thread_num(), omp_get_num_threads());
            return 0;
        }
        """

    openmp_flag = ''
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)
    filename = r'omp_test.c'

    with open(filename, 'w') as file:
        file.write(omp_test)
        file.flush()

    try:
        cc = os.environ['CC']
    except KeyError:
        cc = 'cc'

    # Compile omp_test.c program using different OpenMP
    # compiler flags. If compilation fails continue without
    # OpenMP support.
    with open(os.devnull, 'w') as fnull:
        exit_code = 1
        try:
            exit_code = subprocess.call(
                [cc, '-fopenmp', filename],
                stdout=fnull,
                stderr=fnull)
        except Exception:
            pass
        if exit_code == 0:
            openmp_flag = '-fopenmp'
        else:
            try:
                exit_code = subprocess.call(
                    [cc, '/openmp', filename],
                    stdout=fnull,
                    stderr=fnull)
            except Exception:
                pass
            if exit_code == 0:
                openmp_flag = '/openmp'

    # clean up
    os.chdir(curdir)
    shutil.rmtree(tmpdir)
    return openmp_flag


openmp_flag = get_compiler_openmp_flag()

if openmp_flag:
    print('get_compiler_openmp_flag(): ' + openmp_flag)
    extra_compile_args.append(openmp_flag)
    extra_link_args.append(openmp_flag)

# ------------------ Check if NumPy is installed --------------------


def is_pypy():
    """Check if running in PyPy."""
    try:
        if platform.python_implementation() == 'PyPy':
            return True
    except AttributeError:
        pass
    return False


def can_import(module_name):
    """Check if module can be imported.

    can_import(module_name) -> module or None.
    """
    try:
        return __import__(module_name)
    except ImportError:
        return None


def is_numpy_installed():
    """Check if Numpy is installed."""
    if is_pypy():
        return False
    return bool(can_import("numpy"))

# --------------------- primesieve module ---------------------------


extensions.append(Extension(
    "primesieve._primesieve",
    ["primesieve/_primesieve." + module_file_ext] +
    glob("lib/primesieve/src/*.cpp") +
    glob("lib/primesieve/src/primesieve/*.cpp"),
    include_dirs=["lib/primesieve/include"],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
    language="c++",
    ))

include_dirs.append("lib/primesieve/include")

# --------------------- primesieve.numpy module ---------------------

if is_numpy_installed():
    import numpy

    include_dirs.append(numpy.get_include())
    extensions.append(Extension(
        "primesieve.numpy._numpy",
        ["primesieve/numpy/_numpy." + module_file_ext] +
        glob("lib/primesieve/src/*.cpp") +
        glob("lib/primesieve/src/primesieve/*.cpp"),
        include_dirs=["lib/primesieve/include", numpy.get_include()],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language="c++",
        ))

# --------------------- Parallel build -------------------------------
# http://stackoverflow.com/a/13176803/363778


def parallel_cpp_compile(self,
                         sources,
                         output_dir=None,
                         macros=None,
                         include_dirs=None,
                         debug=0,
                         extra_preargs=None,
                         extra_postargs=None,
                         depends=None):  # noqa
    """Compile cpp files in parallel."""
    macros, objects, extra_postargs, pp_opts, build = \
        self._setup_compile(output_dir, macros, include_dirs,
                            sources, depends, extra_postargs)
    cc_args = self._get_cc_args(pp_opts, debug, extra_preargs)
    import multiprocessing.pool

    def _single_compile(obj):
        try:
            src, ext = build[obj]
        except KeyError:
            return
        self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
    list(multiprocessing.pool.ThreadPool().imap(_single_compile, objects))
    return objects

if not sys.version.startswith('3.6') and not sys.version.startswith('3.7'):
    distutils.ccompiler.CCompiler.compile = parallel_cpp_compile  # type: ignore

# --------------------- Build ---------------------------------------

if module_file_ext == 'pyx':
    ext_modules = cythonize(  # type: ignore
        extensions, include_path=include_dirs)
else:
    ext_modules = extensions


def old_msvc(compiler):
    """Test whether compiler is msvc <= 9.0."""
    return compiler.compiler_type == 'msvc' and \
        hasattr(compiler, '_MSVCCompiler__version') and \
        int(compiler._MSVCCompiler__version) <= 9


class BuildExtSubclass(build_ext):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions."""

    def build_extensions(self):
        """Build extensions."""
        if old_msvc(self.compiler):
            for e in self.extensions:
                e.include_dirs.append('lib/primesieve/src/msvc_compat')
        build_ext.build_extensions(self)  # type: ignore


setup(
    name='primesieve',
    version='1.5.0',
    url='https://github.com/hickford/primesieve-python',
    long_description=open('README.md', "rb").read().decode('utf8'),
    long_description_content_type='text/markdown',
    maintainer='Kim Walisch',
    maintainer_email='kim.walisch@gmail.com',
    license='MIT',
    packages=['primesieve', 'primesieve.numpy'],
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExtSubclass},
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
