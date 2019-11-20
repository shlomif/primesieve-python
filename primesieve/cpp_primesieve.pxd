from libc.stdint cimport uint64_t, int64_t
from libcpp.string cimport string

cdef extern from "primesieve.h":
    void* primesieve_generate_primes(uint64_t start, uint64_t stop, size_t* size, int type)
    void* primesieve_generate_n_primes(uint64_t n, uint64_t start, int type)
    void primesieve_free(void*)
    uint64_t primesieve_nth_prime(int64_t n, uint64_t start)
    uint64_t primesieve_count_primes(uint64_t start, uint64_t stop)
    uint64_t primesieve_count_twins(uint64_t start, uint64_t stop)
    uint64_t primesieve_count_triplets(uint64_t start, uint64_t stop)
    uint64_t primesieve_count_quadruplets(uint64_t start, uint64_t stop)
    uint64_t primesieve_count_quintuplets(uint64_t start, uint64_t stop)
    uint64_t primesieve_count_sextuplets(uint64_t start, uint64_t stop)
    void primesieve_print_primes(uint64_t start, uint64_t stop)
    void primesieve_print_twins(uint64_t start, uint64_t stop)
    void primesieve_print_triplets(uint64_t start, uint64_t stop)
    void primesieve_print_quadruplets(uint64_t start, uint64_t stop)
    void primesieve_print_quintuplets(uint64_t start, uint64_t stop)
    void primesieve_print_sextuplets(uint64_t start, uint64_t stop)
    uint64_t primesieve_get_max_stop()
    int primesieve_get_sieve_size()
    int primesieve_get_num_threads()
    void primesieve_set_sieve_size(int sieve_size)
    void primesieve_set_num_threads(int num_threads)
    string primesieve_version()

cdef extern from "primesieve/iterator.hpp" namespace "primesieve":
    cdef cppclass iterator:
        iterator()
        iterator(uint64_t start, uint64_t stop_hint)
        void skipto(uint64_t start, uint64_t stop_hint)
        uint64_t next_prime()
        uint64_t prev_prime()
