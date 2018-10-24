'''
atkin.p

akin.py

This is the most modern alogorithm that I plane to implement
This sieve was created in 2003 by A.O.L. Atkin and Daniel J. Bernstein
'''

'''                         ALGORITHM
1. Create a list of [2, 3, 5]
2. Create a list of integers up to some limit we define as n
3.
'''

import math
from euler import euler


# Trying again with the Sieve of Atkin
def atkin(limit):
    primes = []
    if limit > 2:
        primes.append(2)
    if limit > 3:
        primes.append(3)
    # defining this function to easily
    # toggle nums in primes set
    def toggle(n):
        if n in primes:
            primes.remove(n)
        else:
            primes.append(n)

    # execute sieve of atkin
    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                toggle(n)
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                toggle(n)
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                toggle(n)
            y += 1
        x += 1
    # now we just need to remove square nums
    r = 5
    primes.sort()
    while r * r < limit:
        if r in primes:
            for i in range(r * r, limit, r * r):
                if i in primes:
                    primes.remove(i)
        r = primes[primes.index(r) + 1]
    return primes


if __name__ == '__main__':
    print(atkin(20))
