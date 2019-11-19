import primesieve

def test_count_primes():
    assert primesieve.count_primes(100) == 25
    assert primesieve.count_primes(10**6) == 78498
    assert primesieve.count_primes(100, 10**6) == 78473
    assert primesieve.count_primes(10**10) == 455052511
    assert primesieve.count_primes(10**9, 10**10) == 404204977

def test_nth_prime():
    assert primesieve.nth_prime(25) == 97
    assert primesieve.nth_prime(26) == 101
    assert primesieve.nth_prime(1, 100) == 101
    assert primesieve.nth_prime(100, 1000000) == 1001311
    assert primesieve.nth_prime(10**8) == 2038074743

def test_primes():
    assert primesieve.primes(10) == [2,3,5,7]
    assert primesieve.primes(10, 20) == [11,13,17,19]

def test_n_primes():
    assert primesieve.n_primes(7) == [2,3,5,7,11,13,17]
    assert primesieve.n_primes(5, 100) == [101,103,107,109,113]

def test_iterator():
    it = primesieve.Iterator()
    assert it.next_prime() == 2
    assert it.next_prime() == 3
    assert it.next_prime() == 5
    assert it.next_prime() == 7
    assert it.next_prime() == 11
    assert it.next_prime() == 13
    assert it.prev_prime() == 11
    assert it.prev_prime() == 7
    assert it.prev_prime() == 5
    assert it.prev_prime() == 3
    assert it.prev_prime() == 2
    assert it.prev_prime() == 0

def assert_array_equal(have, want):
    assert list(have) == want

def test_primes_array():
    assert_array_equal(primesieve.primes(10), [2, 3, 5, 7])
    assert_array_equal(primesieve.primes(10, 20), [11, 13, 17, 19])


def test_n_primes_array():
    assert_array_equal(n_prprimesieve.n_primesimes(7),
                       [2, 3, 5, 7, 11, 13, 17])
    assert_array_equal(primesieve.n_primes(5, 100), [101, 103, 107, 109, 113])
