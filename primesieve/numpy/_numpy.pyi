from typing import List
import numpy as np

def primes(a: int, b: int = 0) -> np.ndarray[np.int64_t]:
    """
    Generate a numpy array of prime numbers between a and b (or up to a if b is unspecified or 0).

    :param a: The lower limit for prime generation.
    :param b: The upper limit for prime generation (optional, default is 0).
    :return: A numpy array containing prime numbers.
    """
    ...

def n_primes(n: int, start: int = 0) -> np.ndarray[np.int64_t]:
    """
    Generate a numpy array with the next n prime numbers starting from the specified start value.

    :param n: The number of prime numbers to generate.
    :param start: The starting point for generating prime numbers (optional, default is 0).
    :return: A numpy array containing the next n prime numbers.
    """
    ...
