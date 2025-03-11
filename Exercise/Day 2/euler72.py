from math import sqrt

def gen_primes(n):
    primes = []
    for candidate in range(2, n):
        is_prime = True
        for prime in primes:
            if prime > sqrt(candidate):
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes

def factorize(n, primes):
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
        if p > sqrt(n):
            break
    if n > 1:
        factors.append(n)
    return factors

def fast_phi(n, primes):
    factors = set(factorize(n, primes))
    phi = n
    for f in factors:
        phi *= (1 - 1/f)
    return int(phi)

primes = gen_primes(1000)
m = 10000
fraq = sum(fast_phi(i, primes) for i in range(2, m+1))

print(fraq)