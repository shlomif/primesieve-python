cimport primesieve

cpdef uint64_t count(uint64_t n):
    return primesieve_count_primes(1, n)

cpdef uint64_t nth_prime(int64_t n):
    return primesieve_nth_prime(n, 1)
