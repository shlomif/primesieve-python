"""Tests for primesieve module.

NOTE!! Please keep this module dependent only on unittest.py and other
cpython3 core-library modules. Using py.test / etc. interferes with
the build-process too much.

"""

import unittest

import primesieve
import subprocess


def assert_array_equal(have, want):
    """Convert array to list and compare to desired output."""
    assert list(have) == want


class TestPrimeSieve(unittest.TestCase):
    def test_count_primes(self):
        """Test count_primes function."""
        assert primesieve.count_primes(100) == 25
        assert primesieve.count_primes(10**6) == 78498
        assert primesieve.count_primes(100, 10**6) == 78473
        assert primesieve.count_primes(10**10) == 455052511
        assert primesieve.count_primes(10**9, 10**10) == 404204977

    def test_nth_prime(self):
        """Test nth prime function."""
        assert primesieve.nth_prime(25) == 97
        assert primesieve.nth_prime(26) == 101
        assert primesieve.nth_prime(1, 100) == 101
        assert primesieve.nth_prime(100, 1000000) == 1001311
        assert primesieve.nth_prime(10**8) == 2038074743

    def test_iterator(self):
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

    def test_primes_array(self):
        """Test primes array output."""
        assert_array_equal(primesieve.primes(10), [2, 3, 5, 7])
        assert_array_equal(primesieve.primes(10, 20), [11, 13, 17, 19])

    def test_n_primes_array(self):
        """Test n_primes array output."""
        assert_array_equal(primesieve.n_primes(7),
                           [2, 3, 5, 7, 11, 13, 17])
        assert_array_equal(
            primesieve.n_primes(5, 100), [101, 103, 107, 109, 113])

    def test_print_primes(self):
        if False:
            assert True
            return
        text = subprocess.run(
            ["python", "-c",
             "import primesieve; primesieve.print_primes(4, 24); "],
            capture_output=True,
        )
        output = text.stdout.decode('utf-8')
        print(output)
        self.assertEqual(output, "".join(
            "{}\n".format(p) for p in [5, 7, 11, 13, 17, 19, 23]
        ), "print_primes output")


if __name__ == '__main__':
    unittest.main()
