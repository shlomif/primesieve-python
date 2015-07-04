primesieve-python
================

Fast prime number generator for Python. Simple bindings around the C++ library [primesieve](http://primesieve.org/) using [Cython](http://cython.org/). Orders of magnitude faster than any pure Python code.

Motivation
------

I enjoy algorithm problems such as those in [Google Code Jam](https://code.google.com/codejam) and [Project Euler](https://projecteuler.net/). Many pertain to number theory. It's important (and fun) to write your own prime finding code once, but it's also useful to have a fast, reliable library.

Two of my favourite problems: Google Code Jam [*Expensive Dinner*](https://code.google.com/codejam/contest/dashboard?c=1150486#s=p2) and Project Euler [Problem 500](https://projecteuler.net/problem=500)

Installation
----

From [PyPI](https://pypi.python.org/pypi/primesieve)

    pip install primesieve

Usage
---

    >>> import primesieve
    >>> primesieve.count(10**9)
    50847534

Benchmarks
---

Development
---------

[![Build Status](https://travis-ci.org/hickford/primesieve-python.svg?branch=master)](https://travis-ci.org/hickford/primesieve-python)

1. Install Cython `pip install cython`
2. Clone this repo `git clone https://github.com/hickford/primesieve-python && cd primesieve-python`
3. Build and install primesieve `cd primesieve && ./configure && make && make install`
4. Build and install the Python bindings `cd .. && pip install .` (or `python setup.py install`)
5. Test `py.test`

See also
---

* [pyprimesieve](https://github.com/jaredks/pyprimesieve) a similar project, but which isn't compatible with recent Python versions
