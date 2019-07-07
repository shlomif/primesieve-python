# cython: language_level=3
cimport primesieve.array.cpp_numpy as cpp_numpy
from libc.stdint cimport uint64_t, int64_t
import array
import sys

cdef extern from "primesieve.h":
    cpdef enum:
        INT64_PRIMES
        ULONG_PRIMES

cdef extern from 'errno.h':
    int errno

cdef c_to_array_array(void* ptr, size_t N):
    """Bind C array allocated using malloc to python array.array"""
    arr = array.array('L', [])
    if sys.version_info >= (3,):
        arr.frombytes((<char*>ptr)[:(N*sizeof(unsigned long))])
    else:
        arr.fromstring((<char*>ptr)[:(N*sizeof(unsigned long))])
    return arr

cpdef primes(int64_t a, int64_t b = 0):
    """Generate a primes array.array"""
    a = max(a, 0)
    b = max(b, 0)
    if b == 0:
        (a,b) = (0,a)

    # Rest errno
    global errno
    errno = 0

    cdef size_t size = 0
    cdef void* c_primes = cpp_numpy.primesieve_generate_primes(a, b, &size, ULONG_PRIMES)

    if errno != 0:
        raise RuntimeError("Failed generating primes, most likely due to insufficient memory.")

    primes = c_to_array_array(c_primes, size)
    cpp_numpy.primesieve_free(c_primes)
    return primes

cpdef n_primes(int64_t n, int64_t start = 0):
    """Generate an array.array with the next n primes"""
    n = max(n, 0)
    start = max(start, 0)

    # Rest errno
    global errno
    errno = 0

    cdef void* c_primes = cpp_numpy.primesieve_generate_n_primes(n, start, ULONG_PRIMES)

    if errno != 0:
        raise RuntimeError("Failed generating primes, most likely due to insufficient memory.")

    primes = c_to_array_array(c_primes, n)
    cpp_numpy.primesieve_free(c_primes)
    return primes
