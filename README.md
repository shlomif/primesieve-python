# primesieve-python

[![Build Status](https://travis-ci.org/kimwalisch/primesieve-python.svg?branch=master)](https://travis-ci.org/kimwalisch/primesieve-python) [![PyPI](https://img.shields.io/pypi/v/primesieve.svg)](https://pypi.python.org/pypi/primesieve)

# Summary

Python bindings for the [primesieve](https://github.com/kimwalisch/primesieve)
C++ library.

Generates primes orders of magnitude faster than any pure Python code!

**Features:**

* Get an array of primes
* Iterate over primes using little memory
* Find the nth prime
* Count/print primes and [prime k-tuplets](https://en.wikipedia.org/wiki/Prime_k-tuple)
* Multi-threaded for counting primes and finding the nth prime
* NumPy support

# Prerequisites

We provide primesieve wheels (distribution packages) for Windows, macOS
and Linux for x86 and x64 CPUs. For other operating systems and/or CPUs
you need to have installed a C++ compiler.

```bash
# Ubuntu/Debian
sudo apt install g++ python-dev

# Fedora
sudo dnf install gcc-c++ python-devel

# macOS
xcode-select --install
```

# Installation

```bash
# Python 3.5 or later
pip install primesieve

# For Python 2.7 use:
pip install "primesieve<=1.4.4"
```

# Conda Installation

[![TravisCI](https://travis-ci.org/conda-forge/python-primesieve-feedstock.svg?branch=master)](https://travis-ci.org/conda-forge/python-primesieve-feedstock)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/github/conda-forge/python-primesieve-feedstock?svg=True)](https://ci.appveyor.com/project/conda-forge/python-primesieve-feedstock/branch/master)
[![Circle CI](https://circleci.com/gh/conda-forge/python-primesieve-feedstock.svg?style=shield)](https://circleci.com/gh/conda-forge/python-primesieve-feedstock)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/python-primesieve/badges/downloads.svg)](https://anaconda.org/conda-forge/python-primesieve)

You don't need to install a C++ compiler when installing python-primesieve using Conda.

```
conda install -c conda-forge python-primesieve
```

# Usage examples

```Python
>>> from primesieve import *

# Get an array of the primes <= 40
>>>  primes(40)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# Get an array of the primes between 100 and 120
>>>  primes(100, 120)
[101, 103, 107, 109, 113]

# Get an array of the first 10 primes
>>>  n_primes(10)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Get an array of the first 10 primes >= 1000
>>>  n_primes(10, 1000)
[1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]

# Get the 10th prime
>>> nth_prime(10)
29

# Count the primes below 10**9
>>> count_primes(10**9)
50847534
```

Here is a [list of all available functions](primesieve/_primesieve.pyx).

# Iterating over primes

Instead of generating a large array of primes and then do something
with the primes it is also possible to simply iterate over the primes
which uses less memory.

```Python
>>> import primesieve

it = primesieve.Iterator()
prime = it.next_prime()

# Iterate over the primes below 10000
while prime < 10000:
    print prime
    prime = it.next_prime()

# Set iterator start number to 100
it.skipto(100)
prime = it.prev_prime()

# Iterate backwards over the primes below 100
while prime > 0:
    print prime
    prime = it.prev_prime()
```

# NumPy support

Using the ```primesieve.numpy``` module you can generate an array of
primes using native C++ performance!

In comparison the ```primesieve``` module generates an array of primes
about 3 times slower mostly because the conversion of the C primes
array into a python array is quite slow.

```Python
>>> from primesieve.numpy import *

# Generate a numpy array with the primes below 100
>>>  primes(100)
array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
       61, 67, 71, 73, 79, 83, 89, 97])

# Generate a numpy array with the first 100 primes
>>>  n_primes(100)
array([  2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
        43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
       103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
       173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
       241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
       317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
       401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
       479, 487, 491, 499, 503, 509, 521, 523, 541])
```

# Development

You need to have installed a C++ compiler, see [Prerequisites](#prerequisites).

```bash
# Install prerequisites
pip install cython pytest numpy

# Clone repository
git clone --recursive https://github.com/kimwalisch/primesieve-python

cd primesieve-python

# Build and install primesieve-python
pip install . --upgrade

# Run tests
pytest
```

# How to do a new release

* You need to be a maintainer of the [primesieve-python](https://github.com/kimwalisch/primesieve-python) repo.
* You need to be a maintainer of the [primesieve pypi](https://pypi.org/project/primesieve) project.
* Compare ```.travis.yml``` with [cibuildwheel#example-setup](https://github.com/joerick/cibuildwheel#example-setup) and update ```.travis.yml``` if needed.
* Update the supported Python versions in ```setup.py``` (we support the same versions as [cibuildwheel](https://pypi.org/project/cibuildwheel)).
* Increment the primesieve-python version in ```setup.py```. Ideally this should be the last commit before the release as this uploads the new primesieve wheels to [https://test.pypi.org](https://test.pypi.org/project/primesieve/#files).
* Check if all primesieve wheels (Windows, macOS, Linux) have been uploaded to [https://test.pypi.org](https://test.pypi.org/project/primesieve/#files).
* If not, read the [Travis CI logs](https://travis-ci.org/github/kimwalisch/primesieve-python) and fix the bugs.
* Finally, do a new release on GitHub.
