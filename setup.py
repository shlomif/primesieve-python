from setuptools import setup, Extension
from glob import glob
from distutils.command.build_ext import build_ext
from distutils.command.build_clib import build_clib
import distutils.sysconfig
import platform
import os
import shutil
import subprocess
import tempfile

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
extra_link_args = []

# --------------------- Get OpenMP compiler flag --------------------

# If this C test program compiles the compiler supports OpenMP
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

def get_compiler_openmp_flag():
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

    # Compile omp_test.c program using different OpenMP compiler flags.
    # If the code below fails continue without OpenMP support.
    with open(os.devnull, 'w') as fnull:
        exit_code = 1
        try:
            exit_code = subprocess.call([cc, '-fopenmp', filename], stdout=fnull, stderr=fnull)
        except:
            pass
        if exit_code == 0:
            openmp_flag = '-fopenmp'
        else:
            try:
                exit_code = subprocess.call([cc, '-openmp', filename], stdout=fnull, stderr=fnull)
            except:
                pass
            if exit_code == 0:
                openmp_flag = '-openmp'

    #clean up
    os.chdir(curdir)
    shutil.rmtree(tmpdir)
    return openmp_flag

openmp_flag = get_compiler_openmp_flag()
print('get_compiler_openmp_flag(): ' + openmp_flag)

extra_compile_args.append(openmp_flag)
extra_link_args.append(openmp_flag)

# ------------------ OpenMP hack for build_clib --------------------

if openmp_flag != '':
    try:
        cflags = distutils.sysconfig.get_config_var('CFLAGS')
        distutils.sysconfig._config_vars['CFLAGS'] = cflags + " " + openmp_flag
    except:
        pass

# ------------------ Check if NumPy is installed --------------------

def is_pypy():
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

# --------------------- libprimesieve -------------------------------

libprimesieve = ('primesieve', dict(
    sources = glob("lib/primesieve/src/primesieve/*.cpp"),
    include_dirs = ["lib/primesieve/include"],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args,
    language = "c++"
    ))

# --------------------- primesieve module ---------------------------

extensions.append(Extension(
    "primesieve._primesieve",
    ["primesieve/_primesieve." + module_file_ext],
    include_dirs = ["lib/primesieve/include"],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args,
    language = "c++"
    ))

# --------------------- primesieve.numpy module ---------------------

if is_Numpy_installed():
    import numpy
    extensions.append(Extension(
        "primesieve.numpy._generate",
        ["primesieve/numpy/_generate." + module_file_ext],
        include_dirs = ["lib/primesieve/include", numpy.get_include()],
        extra_compile_args = extra_compile_args,
        extra_link_args = extra_link_args,
        language = "c++"
        ))

# --------------------- Build ---------------------------------------

if module_file_ext == 'pyx':
    ext_modules = cythonize(extensions)
else:
    ext_modules = extensions

def old_msvc(compiler):
    """Test whether compiler is msvc <= 9.0"""
    return compiler.compiler_type == 'msvc' and hasattr(compiler, '_MSVCCompiler__version') and int(compiler._MSVCCompiler__version) <= 9

class build_clib_subclass(build_clib):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions"""
    def build_libraries(self, libraries):
        if old_msvc(self.compiler):
            for lib_name, build_info in libraries:
                build_info['include_dirs'].append('lib/primesieve/src/msvc_compat')
                print(build_info)
        build_clib.build_libraries(self, libraries)

class build_ext_subclass(build_ext):
    """Workaround to add msvc_compat (stdint.h) for old msvc versions"""
    def build_extensions(self):
        if old_msvc(self.compiler):
            for e in self.extensions:
                e.include_dirs.append('lib/primesieve/src/msvc_compat')
        build_ext.build_extensions(self)

setup(
    name = 'primesieve',
    version = '1.1.0',
    url = 'https://github.com/hickford/primesieve-python',
    description = 'Fast prime number generator. Python bindings for primesieve C/C++ library',
    license = 'MIT',
    libraries = [libprimesieve],
    packages = ['primesieve', 'primesieve.numpy'],
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
