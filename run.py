"""
run.py

UNDER CONSTRUCTION

This is the thing to run!
Just type

    python run.py

"""
import sys
import time

from listOprimes import listOprimes
from eratosthenes import eratosthenes
from eratosthenes import eratosthenesWithSpeedup
from euler import euler
from sundaram import sundaram
from numberline import printNumbers

def runSieve(n, sieve):
    start = time.time()
    primes = sieve(n)
    # printNumbers(sieve(n), n)
    print "sieve of " + sieve.__name__ + " done in:", time.time() - start

if __name__ == "__main__":
    maybe_primes = sundaram(10000)
    primes = euler(10000)
    for p in primes:
        if p not in maybe_primes:
            print('N0OO')
    for m in maybe_primes:
        if m not in primes:
            print('FDJSAFKDDS')
    runSieve(10000, eratosthenes)
    runSieve(10000, euler)
    runSieve(10000, sundaram)
