from libc.stdint cimport uint64_t, int64_t
cimport primesieve

cpdef uint64_t count(uint64_t n):
    return primesieve.count_primes(1, n)

cpdef uint64_t nth(int64_t n):
    return primesieve.nth_prime(n, 1)
