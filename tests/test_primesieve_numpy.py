def is_numpy_installed():
    is_numpy = True
    try:
        import numpy
    except ImportError:
        is_numpy = False
    return is_numpy

if is_numpy_installed():
    from primesieve.numpy import *
    from numpy.testing import assert_array_equal

    def test_generate_primes_numpy():
        assert_array_equal(generate_primes(10), [2,3,5,7])
        assert_array_equal(generate_primes(10, 20), [11,13,17,19])

    def test_generate_n_primes_numpy():
        assert_array_equal(generate_n_primes(7), [2,3,5,7,11,13,17])
        assert_array_equal(generate_n_primes(5, 100), [101,103,107,109,113])
