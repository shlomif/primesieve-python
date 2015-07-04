import primesieve
    
def test_count():
    # from https://primes.utm.edu/howmany.html
    assert primesieve.count(100) == 25
    assert primesieve.count(10**6) == 78498

def test_nth_prime():
    assert primesieve.nth_prime(25) == 97
    assert primesieve.nth_prime(26) == 101