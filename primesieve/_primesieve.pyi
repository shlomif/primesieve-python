from typing import List, Union
from array import array


class Iterator:
    """
    Iterator is an object that allows you to navigate between prime numbers (forward or backward).

    Methods:
        - `skipto(start: int, stop_hint: int = 2**62) -> None`: Skip to the specified number or the nearest prime number.
        - `next_prime() -> int`: Get the next prime number in the sequence.
        - `prev_prime() -> int`: Get the previous prime number in the sequence.


    Example:
        ```
        >>> import primesieve
        >>> from primesieve import Iterator
        >>> # Try it and you will git it 
        >>> number = 225627040
        >>> I = Iterator()
        >>> I.skipto(number)
        >>> I.next_prime()
        225627049
        >>> I.prev_prime()
        225627037
        >>> 
        ```
    """
    def __init__(self) -> None:
        ...

    def skipto(self, start: int, stop_hint: int = 2**62) -> None:
        """
        Skip to the specified number or the nearest prime number.
        
        Arguments:
        
            :param start: The target number or a number before the target prime.
            :param stop_hint: An optional hint for the upper limit.

            
        Example:
            ```
            >>> import primesieve
            >>> from primesieve import Iterator

            >>> number = 225627040
            >>> I = Iterator()
            >>> I.skipto(number)
            >>> I.next_prime()
            225627049
            ```
        """
        ...


    def next_prime(self) -> int:
        """
        Get the next prime number in the sequence.

        :return: The next prime number.

        Example:
            ```
            >>> import primesieve
            >>> from primesieve import Iterator

            >>> number = 225627040
            >>> I = Iterator()
            >>> I.skipto(number)
            >>> I.next_prime()
            225627049
            ```
        """
        ...

    def prev_prime(self) -> int:
        """
        Get the previous prime number in the sequence.

        :return: The previous prime number.

        Example:
            ```
            >>> import primesieve
            >>> from primesieve import Iterator

            >>> number = 225627040
            >>> I = Iterator()
            >>> I.skipto(number)
            >>> I.prev_prime()
            225627037
            ```
        """
        ...

def primes(from_limit:int, to_limit:int) -> array[int]:
    """
    Generate an array of prime integers within the specified range.

    This function generates prime numbers between 'from_limit' and 'to_limit' (inclusive if 'to_limit' is provided),
    and returns them as an array of integers.

    Parameters:
        - from_limit (int): The lower bound of the prime number range.
        - to_limit (int, optional): The upper bound of the prime number range. If not provided, only prime numbers
        up to 'from_limit' will be generated.

    Returns:
        - primes_array (array of int): An array containing prime integers within the specified range.

    Examples:
        ```
        >>> primes(15)
        array('Q', [2, 3, 5, 7, 11, 13])
        >>> primes(15, 30)
        array('Q', [17, 19, 23, 29])
        ```
    
    Note:
        - This function uses a prime number sieve algorithm for efficient prime number generation.
        - If 'to_limit' is not provided, the function will generate primes up to 'from_limit'.
        - 'from_limit' and 'to_limit' must be non-negative integers.
    """
    ...

def n_primes(n: int, start: int = 0) -> List[int]:
    """
    Generate a list of the first 'n' prime integers starting from a given value.

    This function generates 'n' prime numbers greater than or equal to 'start', 
    and returns them as a list of integers.

    Parameters:
        - n (int): The number of prime integers to generate.
        - start (int, optional): The minimum value for the generated prime integers. 
          Defaults to 0, which generates prime numbers starting from 2.

    Returns:
        - primes_list (List[int]): A list containing the first 'n' prime integers 
          greater than or equal to 'start'.

    Examples:
        ```
        >>> n_primes(5)
        [2, 3, 5, 7, 11]
        >>> n_primes(3, 10)
        [11, 13, 17]
        ```

    Note:
        - This function uses a prime number sieve algorithm for efficient prime number generation.
        - The 'start' parameter allows you to specify the minimum value for generated primes.
        - 'n' must be a positive integer, and 'start' must be a non-negative integer.
    """
    ...
def nth_prime(n: int, start: int = 0) -> int:
    """
    Find the 'n'-th prime integer starting from a given value.

    This function calculates and returns the 'n'-th prime number greater than or equal to 'start'.

    Parameters:
        - n (int): The position of the prime integer to find.
        - start (int, optional): The minimum value for the prime integer search. 
          Defaults to 0, which searches for prime numbers starting from 2.

    Returns:
        - prime (int): The 'n'-th prime integer greater than or equal to 'start'.

    Examples:
        ```
        >>> nth_prime(5)
        11
        >>> nth_prime(3, 10)
        17
        ```

    Note:
        - This function uses a prime number sieve algorithm for efficient prime number calculation.
        - The 'start' parameter allows you to specify the minimum value for the prime integer search.
        - 'n' must be a positive integer, and 'start' must be a non-negative integer.
    """
    ...

def count_primes(from_limit: int, to_limit: int) -> int:
    """
    Count the number of prime integers within a given range.

    This function calculates and returns the count of prime numbers within the range from 'from_limit' to 'to_limit'.

    Parameters:
        - from_limit (int): The lower bound of the range for prime number counting.
        - to_limit (int): The upper bound of the range for prime number counting.

    Returns:
        - count (int): The count of prime integers within the specified range.

    Examples:
        ```
        >>> count_primes(2, 10)
        4  # There are 4 prime numbers (2, 3, 5, 7) in the range [2, 10].
        >>> count_primes(20, 30)
        2  # There are 2 prime numbers (23, 29) in the range [20, 30].
        ```

    Note:
        - This function uses a prime number sieve algorithm for efficient prime number counting.
        - 'from_limit' and 'to_limit' must be non-negative integers, and 'from_limit' should be less than or equal to 'to_limit'.
    """
    ...

def count_twins(from_limit: int, to_limit: int = 0) -> int:
    ...

def count_triplets(from_limit: int, to_limit: int = 0) -> int:
    ...

def count_quadruplets(from_limit: int, to_limit: int = 0) -> int:
    ...

def count_quintuplets(from_limit: int, to_limit: int = 0) -> int:
    ...

def count_sextuplets(from_limit: int, to_limit: int = 0) -> int:
    ...

def print_primes(from_limit: int, to_limit: int = 0) -> None:
    ...

def print_twins(from_limit: int, to_limit: int = 0) -> None:
    ...

def print_triplets(from_limit: int, to_limit: int = 0) -> None:
    ...

def print_quadruplets(from_limit: int, to_limit: int = 0) -> None:
    ...

def print_quintuplets(from_limit: int, to_limit: int = 0) -> None:
    ...

def print_sextuplets(from_limit: int, to_limit: int = 0) -> None:
    ...

def get_max_stop() -> int:
    ...

def get_sieve_size() -> int:
    ...

def get_num_threads() -> int:
    ...

def set_sieve_size(sieve_size: int) -> None:
    ...

def set_num_threads(threads: int) -> None:
    ...

def primesieve_version() -> str:
    ...

def primes_range(*args: int) -> Iterator[int]:
    """
    Generate an iterator to iterate over prime numbers within a specified range.

    This function provides an iterator similar to Python's built-in `range` function, allowing you to iterate over prime numbers in a specified range. You can also reverse the iteration by providing a step value of 1 for forward iteration or -1 for reverse iteration.

    Parameters:
        - *args (int): Variable-length argument list representing the range and step value. 
        If one argument is provided, it is treated as the upper bound (exclusive) with a default step value of 1. 
        If two arguments are provided, they are treated as the lower and upper bounds with a default step value of 1. 
        If three arguments are provided, they are treated as the lower and upper bounds and the step value, which should be either 1 for forward iteration or -1 for reverse iteration.

    Returns:
        - prime_iterator (Iterator[int]): An iterator yielding prime numbers within the specified range.

    Example:
        ```
        >>> for prime in primes_range(10):
        ...     print(prime, end=' ')
        ...
        2 3 5 7

        >>> for prime in primes_range(10, 20):
        ...     print(prime, end=' ')
        ...
        11 13 17 19

        >>> for prime in primes_range(95, 10, -1):
        ...     print(prime, end=' ')
        ...
        89 83 79 73 71 67 61 59 53 47 43 41 37 31 29 23 19 13 11
        ```

    Note:
        - This function uses a prime number sieve algorithm for efficient prime number generation.
        - The range is specified as one or two arguments, similar to the `range` function.
        - The upper bound is exclusive, just like Python's `range`.
        - You can specify a step value of 1 for forward iteration or -1 for reverse iteration.
    """
    ...

