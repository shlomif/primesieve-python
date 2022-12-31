"""Setup file for primesieve Python bindings."""

import distutils.ccompiler
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

def is_mswindows():
    """docstring for is_mswindows"""
    return sys.platform.startswith('win')


extensions = []
extra_compile_args = []
extra_link_args = []
if not is_mswindows():
    extra_compile_args.append('-std=c++11')
    extra_link_args.append('-lprimesieve')
include_dirs = []

# ------------- Check if compiler supports -pthread -----------------

def use_pthread():
    # Simple C++ program which uses std::thread
    pthread_test = \
        r"""
        #include <iostream>
        #include <thread>

        void task() {
            std::cout << "Hello, World!" << std::endl;
        }

        int main() {
            std::thread t(task);
            t.join();
            return 0;
        }
        """

    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)
    filename = r'pthread_test.cpp'

    with open(filename, 'w') as file:
        file.write(pthread_test)
        file.flush()

    if "CXX" in os.environ:
        cxx = os.environ['CXX']
    else:
        cxx = 'c++'

    has_pthread = False

    with open(os.devnull, 'w') as fnull:
        exit_code = 1
        try:
            # 1st compile without -pthread and check if it works
            exit_code = subprocess.call(
                [cxx, '-std=c++11', filename],
                stdout=fnull,
                stderr=fnull)
        except Exception:
            pass
        if exit_code != 0:
            try:
                # 2nd compile with -pthread and check if it works
                exit_code = subprocess.call(
                    [cxx, '-std=c++11 -pthread', filename],
                    stdout=fnull,
                    stderr=fnull)
            except Exception:
                pass
            if exit_code == 0:
                has_pthread = True

    # clean up
    os.chdir(curdir)
    shutil.rmtree(tmpdir)
    return has_pthread

if use_pthread():
    print('Use compiler flag: -pthread')
    extra_compile_args.append(-pthread)
    extra_link_args.append(-pthread)

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
# https://stackoverflow.com/a/55670555

try:
    from numpy.distutils.ccompiler import CCompiler_compile
    import distutils.ccompiler
    distutils.ccompiler.CCompiler.compile = CCompiler_compile
except ImportError:
    print("Numpy not found, parallel compile not available.")

# --------------------- Build ---------------------------------------

if module_file_ext == 'pyx':
    ext_modules = cythonize(  # type: ignore
        extensions, include_path=include_dirs, compiler_directives={'embedsignature': True,})
else:
    ext_modules = extensions

setup(
    name='primesieve',
    version='2.3.1',
    url='https://github.com/kimwalisch/primesieve-python',
    long_description=open('README.md', "rb").read().decode('utf8'),
    long_description_content_type='text/markdown',
    maintainer='Kim Walisch',
    maintainer_email='kim.walisch@gmail.com',
    license='MIT',
    packages=['primesieve', 'primesieve.numpy'],
    ext_modules=ext_modules,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
