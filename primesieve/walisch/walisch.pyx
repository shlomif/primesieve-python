from libc.stdint cimport uint64_t, int64_t
from libcpp.vector cimport vector
cimport cpp_walisch

cpdef vector[uint64_t] generate_primes(uint64_t a, uint64_t b = 0) except +:
    """Generate a list of primes"""
    cdef vector[uint64_t] primes
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.generate_primes[uint64_t](a, b, &primes)
    return primes

cpdef vector[uint64_t] generate_n_primes(uint64_t n, uint64_t start = 0) except +:
    """List the first n primes"""
    cdef vector[uint64_t] primes
    cpp_walisch.generate_n_primes[uint64_t](n, start, &primes)
    return primes

cpdef uint64_t nth_prime(int64_t n, uint64_t start = 0) except +:
    """Find the nth prime after start"""
    return cpp_walisch.nth_prime(n, start)

cpdef uint64_t parallel_nth_prime(int64_t n, uint64_t start = 0) except +:
    """Find the nth prime after start using multi-threading"""
    return cpp_walisch.parallel_nth_prime(n, start)

cpdef uint64_t count_primes(uint64_t a, uint64_t b = 0) except +:
    """Count prime numbers"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.count_primes(a, b)
 
cpdef uint64_t count_twins(uint64_t a, uint64_t b = 0) except +:
    """Count twin primes"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.count_twins(a, b)
 
cpdef uint64_t count_triplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime triplets"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.count_triplets(a, b)

cpdef uint64_t count_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quadruplets"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.count_quadruplets(a, b)


cpdef uint64_t count_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quintuplets"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.count_quintuplets(a, b)

cpdef uint64_t count_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime sextuplets"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.count_sextuplets(a, b)


cpdef uint64_t parallel_count_primes(uint64_t a, uint64_t b = 0) except +:
    """Count prime numbers using multi-threading"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.parallel_count_primes(a, b)
 
cpdef uint64_t parallel_count_twins(uint64_t a, uint64_t b = 0) except +:
    """Count twin primes using multi-threading"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.parallel_count_twins(a, b)

 
cpdef uint64_t parallel_count_triplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime triplets using multi-threading"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.parallel_count_triplets(a, b)


cpdef uint64_t parallel_count_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quadruplets using multi-threading"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.parallel_count_quadruplets(a, b)

cpdef uint64_t parallel_count_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime quintuplets using multi-threading"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.parallel_count_quintuplets(a, b)


cpdef uint64_t parallel_count_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Count prime sextuplets using multi-threading"""
    if b == 0:
        (a,b) = (0,a)
    return cpp_walisch.parallel_count_sextuplets(a, b)

cpdef void print_primes(uint64_t a, uint64_t b = 0) except +:
    """Print prime numbers to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.print_primes(a, b)
 
cpdef void print_twins(uint64_t a, uint64_t b = 0) except +:
    """Print twin primes to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.print_twins(a, b)

 
cpdef void print_triplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime triplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.print_triplets(a, b)


cpdef void print_quadruplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime quadruplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.print_quadruplets(a, b)


cpdef void print_quintuplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime quintuplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.print_quintuplets(a, b)

cpdef void print_sextuplets(uint64_t a, uint64_t b = 0) except +:
    """Print prime sextuplets to stdout"""
    if b == 0:
        (a,b) = (0,a)
    cpp_walisch.print_sextuplets(a, b)


cdef class Iterator:
    cdef cpp_walisch.iterator _iterator
    def __cinit__(self):
        self._iterator = cpp_walisch.iterator()
    cpdef void skipto(self, uint64_t start, uint64_t stop_hint = 2**62) except +:
        self._iterator.skipto(start, stop_hint)
    cpdef uint64_t next_prime(self) except +:
        return self._iterator.next_prime()
    cpdef uint64_t previous_prime(self) except +:
        return self._iterator.previous_prime()
