from typing import List, Union
from libc.stdint import uint64_t, int64_t


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

def primes(from_limit: uint64_t, to_limit: uint64_t = 0) -> List[int]:
    ...

def n_primes(n: uint64_t, start: uint64_t = 0) -> List[int]:
    ...

def nth_prime(n: int, start: uint64_t = 0) -> int:
    ...

def count_primes(from_limit: uint64_t, to_limit: uint64_t = 0) -> uint64_t:
    ...

def count_twins(from_limit: uint64_t, to_limit: uint64_t = 0) -> uint64_t:
    ...

def count_triplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> uint64_t:
    ...

def count_quadruplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> uint64_t:
    ...

def count_quintuplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> uint64_t:
    ...

def count_sextuplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> uint64_t:
    ...

def print_primes(from_limit: uint64_t, to_limit: uint64_t = 0) -> None:
    ...

def print_twins(from_limit: uint64_t, to_limit: uint64_t = 0) -> None:
    ...

def print_triplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> None:
    ...

def print_quadruplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> None:
    ...

def print_quintuplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> None:
    ...

def print_sextuplets(from_limit: uint64_t, to_limit: uint64_t = 0) -> None:
    ...

def get_max_stop() -> uint64_t:
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

def primes_range(*args:int) -> Iterator[int]:
    ...
