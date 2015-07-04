from libc.stdint cimport uint64_t, int64_t
from libcpp.vector cimport vector
cimport cpp_primesieve
 
cpdef uint64_t count_primes(uint64_t start, uint64_t stop):
    """Count primes start <= p <= stop"""
    return cpp_primesieve.count_primes(start, stop)

cpdef uint64_t count(uint64_t n):
    """Count primes <= n"""
    return cpp_primesieve.count_primes(0, n)

cpdef uint64_t nth_prime(int64_t n, uint64_t start = 0):
    """Find the nth prime after start"""
    return cpp_primesieve.nth_prime(n, start)

cpdef vector[uint64_t] generate_primes(uint64_t stop):
    """List all primes <= stop"""
    cdef vector[uint64_t] primes
    cpp_primesieve.generate_primes[uint64_t](stop, &primes)
    return primes

cpdef vector[uint64_t] generate_n_primes(uint64_t n):
    """List the first n primes"""
    cdef vector[uint64_t] primes
    cpp_primesieve.generate_n_primes[uint64_t](n, &primes)
    return primes