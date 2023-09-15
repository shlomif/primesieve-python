import primesieve
import typing

def primes(*args:int) -> typing.Generator[int,int,int]:
    if len(args) == 2:
        N = args[1]
        S = args[0]
    else:
        N = args[0]
        S = 1
    it = primesieve.Iterator()
    it.skipto(S)
    prime = it.next_prime()   
    while prime < N:
        yield prime
        prime = it.next_prime()

for p in primes(10,100):
    print(p)
