import primesieve
    
def test_count():
    # from https://primes.utm.edu/howmany.html
    assert primesieve.count(100) == 25
    assert primesieve.count(10**6) == 78498

def test_nth_prime():
    assert primesieve.nth_prime(25) == 97
    assert primesieve.nth_prime(26) == 101

def test_generate_primes():
    assert primesieve.generate_primes(10) == [2,3,5,7]

def test_generate_n_primes():
    assert primesieve.generate_n_primes(7) == [2,3,5,7,11,13,17]