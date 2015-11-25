from libc.stdint cimport uint64_t, int64_t
from libcpp.vector cimport vector

cdef extern from "primesieve.hpp" namespace "primesieve":
    uint64_t nth_prime(int64_t n, uint64_t start)
    uint64_t parallel_nth_prime(int64_t n, uint64_t start)
    void generate_primes[T](uint64_t start, uint64_t stop, vector[T]* primes)
    void generate_n_primes[T](uint64_t n, uint64_t start, vector[T]* primes)
    uint64_t count_primes(uint64_t start, uint64_t stop)
    uint64_t count_twins(uint64_t start, uint64_t stop)
    uint64_t count_triplets(uint64_t start, uint64_t stop)
    uint64_t count_quadruplets(uint64_t start, uint64_t stop)
    uint64_t count_quintuplets(uint64_t start, uint64_t stop)
    uint64_t count_sextuplets(uint64_t start, uint64_t stop)
    uint64_t parallel_count_primes(uint64_t start, uint64_t stop)
    uint64_t parallel_count_twins(uint64_t start, uint64_t stop)
    uint64_t parallel_count_triplets(uint64_t start, uint64_t stop)
    uint64_t parallel_count_quadruplets(uint64_t start, uint64_t stop)
    uint64_t parallel_count_quintuplets(uint64_t start, uint64_t stop)
    uint64_t parallel_count_sextuplets(uint64_t start, uint64_t stop)
    void print_primes(uint64_t start, uint64_t stop)
    void print_twins(uint64_t start, uint64_t stop)
    void print_triplets(uint64_t start, uint64_t stop)
    void print_quadruplets(uint64_t start, uint64_t stop)
    void print_quintuplets(uint64_t start, uint64_t stop)
    void print_sextuplets(uint64_t start, uint64_t stop)

cdef extern from "primesieve/iterator.hpp" namespace "primesieve":
    cdef cppclass iterator:
        iterator()
        iterator(uint64_t start, uint64_t stop_hint)
        void skipto(uint64_t start, uint64_t stop_hint)
        uint64_t next_prime()
        uint64_t previous_prime()
