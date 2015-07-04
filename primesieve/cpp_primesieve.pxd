from libc.stdint cimport uint64_t, int64_t
from libcpp.vector cimport vector

cdef extern from "../lib/primesieve/include/primesieve.hpp" namespace "primesieve":
    uint64_t count_primes(uint64_t start, uint64_t stop)
    uint64_t nth_prime(int64_t n, uint64_t start)
    void generate_primes[T](uint64_t stop, vector[T]* primes)
    void generate_n_primes[T](uint64_t n, vector[T]* primes)