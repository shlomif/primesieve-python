from libc.stdint cimport uint64_t, int64_t

cdef extern from "primesieve.h":
    void* primesieve_generate_primes(uint64_t start, uint64_t stop, size_t* size, int type)
    void* primesieve_generate_n_primes(uint64_t n, uint64_t start, int type)
