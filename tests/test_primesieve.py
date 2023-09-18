"""Tests for primesieve module."""

import primesieve


def assert_array_equal(have, want):
    """Convert array to list and compare to desired output."""
    assert list(have) == want


def test_count_primes():
    """Test count_primes function."""
    assert primesieve.count_primes(100) == 25
    assert primesieve.count_primes(10**6) == 78498
    assert primesieve.count_primes(100, 10**6) == 78473
    assert primesieve.count_primes(10**10) == 455052511
    assert primesieve.count_primes(10**9, 10**10) == 404204977


def test_nth_prime():
    """Test nth prime function."""
    assert primesieve.nth_prime(25) == 97
    assert primesieve.nth_prime(26) == 101
    assert primesieve.nth_prime(1, 100) == 101
    assert primesieve.nth_prime(100, 1000000) == 1001311
    assert primesieve.nth_prime(10**8) == 2038074743


def test_iterator():
    """Test iterator."""
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


def test_primes_array():
    """Test primes array output."""
    assert_array_equal(primesieve.primes(10), [2, 3, 5, 7])
    assert_array_equal(primesieve.primes(10, 20), [11, 13, 17, 19])


def test_n_primes_array():
    """Test n_primes array output."""
    assert_array_equal(primesieve.n_primes(7),
                       [2, 3, 5, 7, 11, 13, 17])
    assert_array_equal(primesieve.n_primes(5, 100), [101, 103, 107, 109, 113])


def test_primes_range():
    """Test primes_range iterator output."""
    assert_array_equal(list(primesieve.primes_range(10,100)), [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    assert_array_equal(list(primesieve.primes_range(100,1000)),
                       [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])