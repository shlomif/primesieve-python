"""Tests for primesieve module."""

from importlib import import_module

import pytest


try:
    from numpy.testing import assert_array_equal as _np_assert_array_eq

    HAS_NUMPY = True
except ImportError:
    _np_assert_array_eq = None
    HAS_NUMPY = False


PRIMESIEVE_MODS = ["primesieve"]

if HAS_NUMPY:
    PRIMESIEVE_MODS.append("primesieve.numpy")


def assert_array_equal(have, want):
    """Convert array to list and compare to desired output."""
    if HAS_NUMPY:
        _np_assert_array_eq(have, want)
    else:
        assert list(have) == want


@pytest.fixture(autouse=True, params=PRIMESIEVE_MODS)
def mod_name(request):
    return request.param


class TestPrimeSieve:
    @pytest.fixture(autouse=True)
    def setup_class(self, mod_name):
        self.primesieve = import_module(mod_name)

    def test_count_primes(self):
        """Test count_primes function."""
        m = "count_primes"
        if not hasattr(self.primesieve, m):
            return
        assert self.primesieve.count_primes(100) == 25
        assert self.primesieve.count_primes(10**6) == 78498
        assert self.primesieve.count_primes(100, 10**6) == 78473
        assert self.primesieve.count_primes(10**10) == 455052511
        assert self.primesieve.count_primes(10**9, 10**10) == 404204977

    def test_nth_prime(self):
        """Test nth prime function."""
        m = "nth_prime"
        if not hasattr(self.primesieve, m):
            return
        assert self.primesieve.nth_prime(25) == 97
        assert self.primesieve.nth_prime(26) == 101
        assert self.primesieve.nth_prime(1, 100) == 101
        assert self.primesieve.nth_prime(100, 1000000) == 1001311
        assert self.primesieve.nth_prime(10**8) == 2038074743

    def test_iterator(self):
        """Test iterator."""
        m = "Iterator"
        if not hasattr(self.primesieve, m):
            return
        it = self.primesieve.Iterator()
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

    def test_primes_array(self):
        """Test primes array output."""
        assert_array_equal(
            self.primesieve.primes(10),
            [2, 3, 5, 7],
        )
        assert_array_equal(
            self.primesieve.primes(10, 20),
            [11, 13, 17, 19],
        )

    def test_n_primes_array(self):
        """Test n_primes array output."""
        assert_array_equal(
            self.primesieve.n_primes(7),
            [2, 3, 5, 7, 11, 13, 17],
        )
        assert_array_equal(
            self.primesieve.n_primes(5, 100),
            [101, 103, 107, 109, 113],
        )
