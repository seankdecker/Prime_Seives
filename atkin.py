'''
akin.py

This is the most modern alogorithm that I plane to implement
This sieve was created in 2003 by A.O.L. Atkin and Daniel J. Bernstein
'''

'''                         ALGORITHM
1. Create a list of [2, 3, 5]
2. Create a list of integers up to some limit we define as n
3.

hmmm I want to understand this sieve better before implementing it
still isn't completely correct
'''

import math
from euler import euler

# returns the list of primes up to n
# These primes are found by by Atkins's Sieve
def atkin(n):
    if n <= 60:
        return euler(n)
    # first we roll the wheel of factorization twice to find modulo 60 candidate prime
    hits = [1] + euler(60)
    for _ in range(3):
        del hits[1]
    # make list of candidate primes based on primes under 60
    numbers = []
    for i in range(n/60):
        for hit in hits:
            numbers.append((60 * i) + hit)
    i = n/60
    for hit in hits:
        if (60 * i) + hit > n:
            break
        numbers.append((60 * i) + hit)
    # if n < 3: return [2]
    # if n < 5: return [2, 3]
    # primes = [2, 3, 5]
    # numbers = range(1, n + 1)
    # for n in numbers:
    return numbers


if __name__ == '__main__':
    print(atkin(100))
