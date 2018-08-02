"""
run.py

UNDER CONSTRUCTION

This is the thing to run!
Just type

    python run.py [the sieve to run]

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
    start = 0
    start = time.time()
    # printNumbers(sieve(n), n)
    print "sieve of " + sieve.__name__ + " done in:", time.time() - start

if __name__ == "__main__":
    if eratosthenes(3000) != euler(3000):
        print 'NOOOOOO'
    if euler(3000) != sundaram(3000):
        print 'Noooooo'
    primes = euler(3000)
    maybePrimes = sundaram(3000)
    for element in primes:
        if element not in maybePrimes:
            print element
    # runSieve(30000, eratosthenes)
    # runSieve(30000, euler)
    # runSieve(30000, sundaram)
    primesFile = open('primes.txt', 'w')
    primes = euler(100000)
    for prime in primes:
        primesFile.write(str(prime) + ' ')
    primesFile.write('\n')
    primesFile.close()
    print 'Done'
