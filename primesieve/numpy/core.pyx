from libc.stdint cimport int64_t
cimport cpp_core
import numpy as np
cimport numpy as np

np.import_array()

cdef extern from "primesieve.h":
    cpdef enum:
        INT64_PRIMES

cdef extern from "numpy/arrayobject.h":
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)

cdef extern from 'errno.h':
    int errno

cdef c_to_numpy_array(void* ptr, np.npy_intp N, int t):
    """Bind C array allocated using malloc to NumPy ndarray"""
    cdef np.ndarray[np.int64_t, ndim=1] arr = np.PyArray_SimpleNewFromData(1, &N, t, ptr)
    PyArray_ENABLEFLAGS(arr, np.NPY_OWNDATA)
    return arr

cpdef np.ndarray[np.int64_t, ndim=1] generate_primes(int64_t a, int64_t b = 0):
    """Generate a numpy primes array"""
    a = max(a, 0)
    b = max(b, 0)
    if b == 0:
        (a,b) = (0,a)

    # Rest errno
    global errno
    errno = 0

    cdef size_t size = 0
    cdef void* c_primes = cpp_core.primesieve_generate_primes(a, b, &size, INT64_PRIMES)

    if errno != 0:
        raise RuntimeError("Failed generating primes, most likely due to insufficient memory.")

    primes = c_to_numpy_array(c_primes, size, np.NPY_INT64)
    return primes

cpdef np.ndarray[np.int64_t, ndim=1] generate_n_primes(int64_t n, int64_t start = 0):
    """Generate a numpy array with the next n primes"""
    n = max(n, 0)
    start = max(start, 0)

    # Rest errno
    global errno
    errno = 0

    cdef void* c_primes = cpp_core.primesieve_generate_n_primes(n, start, INT64_PRIMES)

    if errno != 0:
        raise RuntimeError("Failed generating primes, most likely due to insufficient memory.")

    primes = c_to_numpy_array(c_primes, n, np.NPY_INT64)
    return primes
