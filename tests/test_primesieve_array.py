from primesieve.array import n_primes, primes

def assert_array_equal(have, want):
    assert list(have) == want

def test_primes_array():
    assert_array_equal(primes(10), [2,3,5,7])
    assert_array_equal(primes(10, 20), [11,13,17,19])

def test_n_primes_array():
    assert_array_equal(n_primes(7), [2,3,5,7,11,13,17])
    assert_array_equal(n_primes(5, 100), [101,103,107,109,113])
