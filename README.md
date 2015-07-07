primesieve-python
================

Fast prime number generator for Python. Simple bindings around the C++ library [primesieve](http://primesieve.org/). Orders of magnitude faster than any pure Python code.

Motivation
------

I enjoy algorithm problems such as those in [Google Code Jam](https://code.google.com/codejam) and [Project Euler](https://projecteuler.net/). Many pertain to number theory. It's important (and fun) to write your own prime finding code once, but it's also useful to have a fast, reliable library.

Two of my favourite problems: Google Code Jam [*Expensive Dinner*](https://code.google.com/codejam/contest/dashboard?c=1150486#s=p2) and Project Euler [Problem 500](https://projecteuler.net/problem=500)

Installation
----

[![PyPI](https://img.shields.io/pypi/v/primesieve.svg)](https://pypi.python.org/pypi/primesieve)

From [PyPI](https://pypi.python.org/pypi/primesieve)

    pip install primesieve

Usage
---

    >>> import primesieve
    >>> primesieve.count(10**9)
    50847534
    >>> primesieve.generate_primes(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> primesieve.nth_prime(10)
    29
    >>> primesieve.generate_n_primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

Benchmarks
---

Development
---------

[![Build Status](https://travis-ci.org/hickford/primesieve-python.svg?branch=master)](https://travis-ci.org/hickford/primesieve-python)

1. Install Cython `pip install cython`
2. Clone this repo `git clone --recursive https://github.com/hickford/primesieve-python && cd primesieve-python`
3. Install `pip install .` (this builds both the primesieve C++ library and Python extension)
4. Test `py.test`

### Windows build

[![Build status](https://ci.appveyor.com/api/projects/status/4chekgdj7bqx4ivt/branch/master?svg=true)](https://ci.appveyor.com/project/hickford/primesieve-python/branch/master)

See also
---

* [pyprimesieve](https://github.com/jaredks/pyprimesieve) a similar project
