import primesieve
import array
import typing
def primes() -> array.array:
    """
    ## funciton to genrate a array of primes numpers less than the inputed argumnt

    #### input: int
    #### returns: array
    """
    pass

def n_primes() -> array.array:
    """
    function to genreate a array of prime numpers with the size of input N
    """
    pass

def primes_range(**args:int) -> typing.Generator[int,int,int]:
    """
    these is a genrator function for iterate over the primes without storing the primes in the memory.

    1th argumnet is inclued and the 2th is excluded

    input: (int,int)
    return: genrator opject

    example:
    `for prime in primes_range(500,10e7):
    pass`
    """
    pass
