from libc.stdint cimport uint64_t, int64_t
cimport cpp_core
import numpy as np
cimport numpy as np

np.import_array()

cdef extern from "primesieve.h":
    cpdef enum:
        SHORT_PRIMES
        USHORT_PRIMES
        INT_PRIMES
        UINT_PRIMES
        LONG_PRIMES
        ULONG_PRIMES
        LONGLONG_PRIMES
        ULONGLONG_PRIMES
        INT16_PRIMES
        UINT16_PRIMES
        INT32_PRIMES
        UINT32_PRIMES
        INT64_PRIMES
        UINT64_PRIMES

cdef extern from "numpy/arrayobject.h":
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)

cdef c_to_numpy_array(void* ptr, np.npy_intp N, int t):
    """Bind C array allocated using malloc to NumPy ndarray"""
    cdef np.ndarray[np.uint64_t, ndim=1] arr = np.PyArray_SimpleNewFromData(1, &N, t, ptr)
    PyArray_ENABLEFLAGS(arr, np.NPY_OWNDATA)
    return arr

cpdef np.ndarray[np.uint64_t, ndim=1] generate_primes(uint64_t a, uint64_t b = 0) except +:
    """Generate a numpy primes array"""
    if b == 0:
        (a,b) = (0,a)
    cdef size_t size = 0
    cdef void* c_primes = cpp_core.primesieve_generate_primes(a, b, &size, UINT64_PRIMES)
    primes = c_to_numpy_array(c_primes, size, np.NPY_UINT64)
    return primes

cpdef np.ndarray[np.uint64_t, ndim=1] generate_n_primes(uint64_t n, uint64_t start = 0) except +:
    """Generate a numpy array with the next n primes"""
    cdef void* c_primes = cpp_core.primesieve_generate_n_primes(n, start, UINT64_PRIMES)
    primes = c_to_numpy_array(c_primes, n, np.NPY_UINT64)
    return primes
