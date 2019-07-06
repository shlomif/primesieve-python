# cython: language_level=3
cimport primesieve.array.cpp_numpy as cpp_numpy
from libc.stdint cimport uint64_t, int64_t
import array

cdef extern from "primesieve.h":
    cpdef enum:
        INT64_PRIMES

cdef extern from 'errno.h':
    int errno

cdef c_to_numpy_array(void* ptr, size_t N):
    """Bind C array allocated using malloc to NumPy ndarray"""
    arr = array.array('L', [])
    arr.frombytes((<char*>ptr)[:(N*sizeof(uint64_t))])
    return arr

cpdef primes(int64_t a, int64_t b = 0):
    """Generate a numpy primes array"""
    a = max(a, 0)
    b = max(b, 0)
    if b == 0:
        (a,b) = (0,a)

    # Rest errno
    global errno
    errno = 0

    cdef size_t size = 0
    cdef void* c_primes = cpp_numpy.primesieve_generate_primes(a, b, &size, INT64_PRIMES)

    if errno != 0:
        raise RuntimeError("Failed generating primes, most likely due to insufficient memory.")

    primes = c_to_numpy_array(c_primes, size)
    return primes

cpdef n_primes(int64_t n, int64_t start = 0):
    """Generate a numpy array with the next n primes"""
    n = max(n, 0)
    start = max(start, 0)

    # Rest errno
    global errno
    errno = 0

    cdef void* c_primes = cpp_numpy.primesieve_generate_n_primes(n, start, INT64_PRIMES)

    if errno != 0:
        raise RuntimeError("Failed generating primes, most likely due to insufficient memory.")

    primes = c_to_numpy_array(c_primes, n)
    return primes
