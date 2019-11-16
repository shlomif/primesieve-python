# cython: language_level=3

from libc.stdint cimport uint64_t, int64_t
from libcpp.string cimport string
from libcpp.vector cimport vector

cimport cpp_primesieve

cpdef vector[uint64_t] primes(uint64_t a, uint64_t b = 0) except +:
    """Generate a list of primes"""
    cdef vector[uint64_t] primes
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.generate_primes[uint64_t](a, b, &primes)
    return primes

cpdef vector[uint64_t] n_primes(uint64_t n, uint64_t start = 0) except +:
    """List the first n primes >= start"""
    cdef vector[uint64_t] primes
    cpp_primesieve.generate_n_primes[uint64_t](n, start, &primes)
    return primes

cpdef uint64_t nth_prime(int64_t n, uint64_t start = 0) except +:
    """Find the nth prime > start"""
    return cpp_primesieve.nth_prime(n, start)

cpdef uint64_t count_primes(uint64_t a, uint64_t b = 0) except +:
    """Count prime numbers"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_primesieve.count_primes(a, b)

cpdef uint64_t count_twins(uint64_t a, uint64_t b = 0) except +:
    """Count twin primes """
    if b == 0:
        (a,b) = (0,a)
    return cpp_primesieve.count_twins(a, b)

cpdef uint64_t count_triplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime triplets """
    if b == 0:
        (a,b) = (0,a)
    return cpp_primesieve.count_triplets(a, b)

cpdef uint64_t count_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quadruplets """
    if b == 0:
        (a,b) = (0,a)
    return cpp_primesieve.count_quadruplets(a, b)

cpdef uint64_t count_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quintuplets """
    if b == 0:
        (a,b) = (0,a)
    return cpp_primesieve.count_quintuplets(a, b)

cpdef uint64_t count_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime sextuplets """
    if b == 0:
        (a,b) = (0,a)
    return cpp_primesieve.count_sextuplets(a, b)

cpdef void print_primes(uint64_t a, uint64_t b = 0) except +:
    """Print prime numbers to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.print_primes(a, b)

cpdef void print_twins(uint64_t a, uint64_t b = 0) except +:
    """Print twin primes to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.print_twins(a, b)

cpdef void print_triplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime triplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.print_triplets(a, b)

cpdef void print_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime quadruplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.print_quadruplets(a, b)

cpdef void print_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime quintuplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.print_quintuplets(a, b)

cpdef void print_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime sextuplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_primesieve.print_sextuplets(a, b)

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
