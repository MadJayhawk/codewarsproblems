# 5 kyu  Python
# https://www.codewars.com/kata/535bfa2ccdbf509be8000113/train/python
class Primes:
    def __init__(self):
        self.primes = [2]
        self.to_use = 1

    def test(self, candidate):
        while len(self.primes) > self.to_use:
            next = self.primes[self.to_use]
            if candidate <= next * next:
                self.to_use += 1
        return all(candidate % p != 0 for p in self.primes[: self.to_use])

    def __iter__(self):
        import itertools

        for candidate in itertools.count(3):
            if self.test(candidate):
                self.primes.append(candidate)
                yield candidate

    def first(n):
        if n == 1:
            return [2]
        my_primes = Primes()
        d = [2]
        for p in my_primes:
            d.append(p)
            if len(d) > n - 1:
                break
        return d


print(Primes.first(18))
# ---------------------------------------------------------------
"""
limit = 1000000//2
sieve = [0] * 2 + list(range(2, limit))
for i in range(2, limit):
    for j in range(i * i, limit, i):
        sieve[j] = 0
primes = [i for i in sieve if i]

class Primes:
    def __init__(self):
        pass
    @staticmethod
    def first(n) : 
        return primes[:n]

print(Primes.first(15))
#-------------------------------------------------------------------------------------
from gmpy2 import next_prime
class Primes:
    @staticmethod
    def first(n):
        p = next_prime(1)
        d = [p]
        for _ in range(1,n):
            p = next_prime(p)
            d.append(p)
        return d
"""
