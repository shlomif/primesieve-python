from libc.stdint cimport uint64_t, int64_t
from libcpp.string cimport string

cdef extern from "primesieve.h":
    void* primesieve_generate_primes(uint64_t start, uint64_t stop, size_t* size, int type)
    void* primesieve_generate_n_primes(uint64_t n, uint64_t start, int type)
    void primesieve_free(void*)

cdef extern from "primesieve.hpp" namespace "primesieve":
    uint64_t count_primes(uint64_t start, uint64_t stop)
    uint64_t count_twins(uint64_t start, uint64_t stop)
    uint64_t count_triplets(uint64_t start, uint64_t stop)
    uint64_t count_quadruplets(uint64_t start, uint64_t stop)
    uint64_t count_quintuplets(uint64_t start, uint64_t stop)
    uint64_t count_sextuplets(uint64_t start, uint64_t stop)
    uint64_t nth_prime(int64_t n, uint64_t start)
    void print_primes(uint64_t start, uint64_t stop)
    void print_twins(uint64_t start, uint64_t stop)
    void print_triplets(uint64_t start, uint64_t stop)
    void print_quadruplets(uint64_t start, uint64_t stop)
    void print_quintuplets(uint64_t start, uint64_t stop)
    void print_sextuplets(uint64_t start, uint64_t stop)
    int get_num_threads()
    uint64_t get_max_stop()
    int get_sieve_size()
    void set_sieve_size(int sieve_size)
    void set_num_threads(int threads)
    string primesieve_version()

cdef extern from "primesieve/iterator.hpp" namespace "primesieve":
    cdef cppclass iterator:
        iterator()
        iterator(uint64_t start, uint64_t stop_hint)
        # void jump_to(uint64_t start, uint64_t stop_hint)
        uint64_t next_prime()
        uint64_t prev_prime()

cdef extern from *:
    '''
    #if PRIMESIEVE_VERSION_MAJOR >= 11
    #define iterator_jumpto(it, start, hint) it.jump_to(start, hint)
    #else
    #define iterator_jumpto(it, start, hint) it.skipto(start-1, hint)
    #endif
    '''
    void iterator_jumpto(iterator & it, uint64_t start, uint64_t stop_hint)
