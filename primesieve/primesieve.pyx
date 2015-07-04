from libc.stdint cimport uint64_t, int64_t
cimport cpp_primesieve

cpdef uint64_t count_primes(uint64_t start, uint64_t stop):
    return cpp_primesieve.count_primes(start, stop)

cpdef uint64_t count(uint64_t n):
    return cpp_primesieve.count_primes(0, n)

cpdef uint64_t nth_prime(int64_t n, uint64_t start = 0):
    return cpp_primesieve.nth_prime(n, start)
