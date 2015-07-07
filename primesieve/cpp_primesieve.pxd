from libc.stdint cimport uint64_t, int64_t
from libcpp.vector cimport vector

cdef extern from "primesieve.hpp" namespace "primesieve":
    uint64_t count_primes(uint64_t start, uint64_t stop)
    uint64_t nth_prime(int64_t n, uint64_t start)
    void generate_primes[T](uint64_t stop, vector[T]* primes)
    void generate_n_primes[T](uint64_t n, vector[T]* primes)

cdef extern from "iterator.hpp" namespace "primesieve":
    cdef cppclass iterator:
        iterator()
        iterator(uint64_t start, uint64_t stop_hint)
        uint64_t next_prime()
        uint64_t previous_prime()
