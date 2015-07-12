from libc.stdint cimport uint64_t, int64_t
from libcpp.vector cimport vector
cimport cpp_primesieve

cpdef vector[uint64_t] generate_primes(uint64_t a, uint64_t b = 0) except +:
    """Generate a list of primes"""
    cdef vector[uint64_t] primes
    if b != 0:
        cpp_primesieve.generate_primes[uint64_t](a, b, &primes)
    else:
        cpp_primesieve.generate_primes[uint64_t](b, a, &primes)
    return primes

cpdef vector[uint64_t] generate_n_primes(uint64_t n, uint64_t start = 0) except +:
    """List the first n primes"""
    cdef vector[uint64_t] primes
    cpp_primesieve.generate_n_primes[uint64_t](n, start, &primes)
    return primes

cpdef uint64_t nth_prime(int64_t n, uint64_t start = 0) except +:
    """Find the nth prime after start"""
    return cpp_primesieve.nth_prime(n, start)

cpdef uint64_t parallel_nth_prime(int64_t n, uint64_t start = 0) except +:
    """Find the nth prime after start using multi-threading"""
    return cpp_primesieve.parallel_nth_prime(n, start)

cpdef uint64_t count_primes(uint64_t a, uint64_t b = 0) except +:
    """Count prime numbers"""
    if b != 0:
        return cpp_primesieve.count_primes(a, b)
    else:
        return cpp_primesieve.count_primes(b, a)
 
cpdef uint64_t count_twins(uint64_t a, uint64_t b = 0) except +:
    """Count twin primes"""
    if b != 0:
        return cpp_primesieve.count_twins(a, b)
    else:
        return cpp_primesieve.count_twins(b, a)
 
cpdef uint64_t count_triplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime triplets"""
    if b != 0:
        return cpp_primesieve.count_triplets(a, b)
    else:
        return cpp_primesieve.count_triplets(b, a)

cpdef uint64_t count_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quadruplets"""
    if b != 0:
        return cpp_primesieve.count_quadruplets(a, b)
    else:
        return cpp_primesieve.count_quadruplets(b, a)

cpdef uint64_t count_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quintuplets"""
    if b != 0:
        return cpp_primesieve.count_quintuplets(a, b)
    else:
        return cpp_primesieve.count_quintuplets(b, a)

cpdef uint64_t count_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime sextuplets"""
    if b != 0:
        return cpp_primesieve.count_sextuplets(a, b)
    else:
        return cpp_primesieve.count_sextuplets(b, a)

cpdef uint64_t parallel_count_primes(uint64_t a, uint64_t b = 0) except +:
    """Count prime numbers using multi-threading"""
    if b != 0:
        return cpp_primesieve.parallel_count_primes(a, b)
    else:
        return cpp_primesieve.parallel_count_primes(b, a)
 
cpdef uint64_t parallel_count_twins(uint64_t a, uint64_t b = 0) except +:
    """Count twin primes using multi-threading"""
    if b != 0:
        return cpp_primesieve.parallel_count_twins(a, b)
    else:
        return cpp_primesieve.parallel_count_twins(b, a)
 
cpdef uint64_t parallel_count_triplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime triplets using multi-threading"""
    if b != 0:
        return cpp_primesieve.parallel_count_triplets(a, b)
    else:
        return cpp_primesieve.parallel_count_triplets(b, a)

cpdef uint64_t parallel_count_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quadruplets using multi-threading"""
    if b != 0:
        return cpp_primesieve.parallel_count_quadruplets(a, b)
    else:
        return cpp_primesieve.parallel_count_quadruplets(b, a)

cpdef uint64_t parallel_count_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quintuplets using multi-threading"""
    if b != 0:
        return cpp_primesieve.parallel_count_quintuplets(a, b)
    else:
        return cpp_primesieve.parallel_count_quintuplets(b, a)

cpdef uint64_t parallel_count_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime sextuplets using multi-threading"""
    if b != 0:
        return cpp_primesieve.parallel_count_sextuplets(a, b)
    else:
        return cpp_primesieve.parallel_count_sextuplets(b, a)

cpdef void print_primes(uint64_t a, uint64_t b = 0) except +:
    """Print prime numbers to stdout"""
    if b != 0:
        cpp_primesieve.print_primes(a, b)
    else:
        cpp_primesieve.print_primes(b, a)
 
cpdef void print_twins(uint64_t a, uint64_t b = 0) except +:
    """Print twin primes to stdout"""
    if b != 0:
        cpp_primesieve.print_twins(a, b)
    else:
        cpp_primesieve.print_twins(b, a)
 
cpdef void print_triplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime triplets to stdout"""
    if b != 0:
        cpp_primesieve.print_triplets(a, b)
    else:
        cpp_primesieve.print_triplets(b, a)

cpdef void print_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime quadruplets to stdout"""
    if b != 0:
        cpp_primesieve.print_quadruplets(a, b)
    else:
        cpp_primesieve.print_quadruplets(b, a)

cpdef void print_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime quintuplets to stdout"""
    if b != 0:
        cpp_primesieve.print_quintuplets(a, b)
    else:
        cpp_primesieve.print_quintuplets(b, a)

cpdef void print_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime sextuplets to stdout"""
    if b != 0:
        cpp_primesieve.print_sextuplets(a, b)
    else:
        cpp_primesieve.print_sextuplets(b, a)

cdef class Iterator:
    cdef cpp_primesieve.iterator _iterator
    def __cinit__(self):
        self._iterator = cpp_primesieve.iterator()
    cpdef void skipto(self, uint64_t start, uint64_t stop_hint = 2**62) except +:
        self._iterator.skipto(start, stop_hint)
    cpdef uint64_t next_prime(self) except +:
        return self._iterator.next_prime()
    cpdef uint64_t previous_prime(self) except +:
        return self._iterator.previous_prime()
