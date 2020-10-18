# cython: language_level=3

import array
from libc.stdint cimport uint64_t, int64_t
from libcpp.string cimport string
import sys

from primesieve cimport cpp_primesieve

__all__ = [
    'Iterator',
     'arr_type',
     'count_primes',
     'count_quadruplets',
     'count_quintuplets',
     'count_sextuplets',
     'count_triplets',
     'count_twins',
     'get_max_stop',
     'get_num_threads',
     'get_sieve_size',
     'n_primes',
     'nth_prime',
     'primes',
     'primesieve_version',
     'print_primes',
     'print_quadruplets',
     'print_quintuplets',
     'print_sextuplets',
     'print_triplets',
     'print_twins',
     'set_num_threads',
     'set_sieve_size',
]

cdef extern from "primesieve.h":
    cdef enum:
        INT64_PRIMES
        ULONG_PRIMES
        ULONGLONG_PRIMES

cdef extern from 'errno.h':
    int errno

cdef int is_py3 = sys.version_info >= (3,)
arr_type = ("Q" if is_py3 else "L")
cdef size_t item_size = (sizeof(unsigned long long) if is_py3 else sizeof(unsigned long))
cdef int primes_type = (ULONGLONG_PRIMES if is_py3 else ULONG_PRIMES)

cdef c_to_array_array(void* ptr, size_t N):
    """Create a python array from a C array."""
    arr = array.array(arr_type, (<char*>ptr)[:(N*item_size)])
    return arr

cpdef primes(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Generate a primes array from from_limit to to_limit (or up to
    from_limit if to_limit is unspecified or 0.)"""
    from_limit = max(from_limit, 0)
    to_limit = max(to_limit, 0)
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)

    # Rest errno
    global errno
    errno = 0

    cdef size_t size = 0
    cdef void* c_primes = cpp_primesieve.primesieve_generate_primes(from_limit, to_limit, &size, primes_type)

    if errno != 0:
        raise RuntimeError("Failed to generate primes, most likely due to insufficient memory.")

    primes = c_to_array_array(c_primes, size)
    cpp_primesieve.primesieve_free(c_primes)
    return primes

cpdef n_primes(uint64_t n, uint64_t start = 0) except +:
    """List the first n primes >= start."""
    n = max(n, 0)
    start = max(start, 0)

    # Rest errno
    global errno
    errno = 0

    cdef void* c_primes = cpp_primesieve.primesieve_generate_n_primes(n, start, primes_type)

    if errno != 0:
        raise RuntimeError("Failed to generate primes, most likely due to insufficient memory.")

    primes = c_to_array_array(c_primes, n)
    cpp_primesieve.primesieve_free(c_primes)
    return primes

cpdef uint64_t nth_prime(int64_t n, uint64_t start = 0) except +:
    """Find the nth prime > start"""
    return cpp_primesieve.nth_prime(n, start)

cpdef uint64_t count_primes(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Count the prime numbers from from_limit to to_limit (or up to
        from_limit if to_limit is unspecified or 0.)"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    return cpp_primesieve.count_primes(from_limit, to_limit)

cpdef uint64_t count_twins(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Count twin primes """
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    return cpp_primesieve.count_twins(from_limit, to_limit)

cpdef uint64_t count_triplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Count prime triplets """
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    return cpp_primesieve.count_triplets(from_limit, to_limit)

cpdef uint64_t count_quadruplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Count prime quadruplets """
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    return cpp_primesieve.count_quadruplets(from_limit, to_limit)

cpdef uint64_t count_quintuplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Count prime quintuplets """
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    return cpp_primesieve.count_quintuplets(from_limit, to_limit)

cpdef uint64_t count_sextuplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Count prime sextuplets """
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    return cpp_primesieve.count_sextuplets(from_limit, to_limit)

cpdef void print_primes(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Print prime numbers to stdout"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    cpp_primesieve.print_primes(from_limit, to_limit)

cpdef void print_twins(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Print twin primes to stdout"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    cpp_primesieve.print_twins(from_limit, to_limit)

cpdef void print_triplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Print prime triplets to stdout"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    cpp_primesieve.print_triplets(from_limit, to_limit)

cpdef void print_quadruplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Print prime quadruplets to stdout"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    cpp_primesieve.print_quadruplets(from_limit, to_limit)

cpdef void print_quintuplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Print prime quintuplets to stdout"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    cpp_primesieve.print_quintuplets(from_limit, to_limit)

cpdef void print_sextuplets(uint64_t from_limit, uint64_t to_limit = 0) except +:
    """Print prime sextuplets to stdout"""
    if to_limit == 0:
        (from_limit,to_limit) = (0,from_limit)
    cpp_primesieve.print_sextuplets(from_limit, to_limit)

cpdef uint64_t get_max_stop() except +:
    """Returns the largest valid stop number for primesieve. 2^64-1 (UINT64_MAX)"""
    return cpp_primesieve.get_max_stop()

cpdef int get_sieve_size() except +:
    """Get the current set sieve size in KiB"""
    return cpp_primesieve.get_sieve_size()

cpdef int get_num_threads() except +:
    """Get the currently set number of threads"""
    return cpp_primesieve.get_num_threads()

cpdef void set_sieve_size(int sieve_size) except +:
    """Set the sieve size in KiB (kibibyte).  The best sieving performance is achieved with a sieve size of your CPU's L1 or L2 cache size (per core)."""
    cpp_primesieve.set_sieve_size(sieve_size)

cpdef void set_num_threads(int threads) except +:
    """Set the number of threads for sieving"""
    cpp_primesieve.set_num_threads(threads)

cpdef string primesieve_version() except +:
    """Get the primesieve version number"""
    return cpp_primesieve.primesieve_version()

cdef class Iterator:
    cdef cpp_primesieve.iterator _iterator
    def __cinit__(self):
        self._iterator = cpp_primesieve.iterator()
    cpdef void skipto(self, uint64_t start, uint64_t stop_hint = 2**62) except +:
        self._iterator.skipto(start, stop_hint)
    cpdef uint64_t next_prime(self) except +:
        return self._iterator.next_prime()
    cpdef uint64_t prev_prime(self) except +:
        return self._iterator.prev_prime()
