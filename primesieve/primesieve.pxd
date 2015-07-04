from libc.stdint cimport uint64_t, int64_t

cdef extern from "../lib/primesieve/include/primesieve.h":
    uint64_t primesieve_count_primes(uint64_t start, uint64_t stop)
    uint64_t primesieve_nth_prime(int64_t n, uint64_t start)
