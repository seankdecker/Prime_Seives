"""
run.py

UNDER CONSTRUCTION

This is the thing to run!
Just type

    python run.py N {0, 1}

where N is the limit, up to what number do you want to search
and 0 represents not printing the primes while 1 represents printing

if no command line arguments are passed, we default N = 1000 and
printing is off
"""
import sys
import time

from listOprimes import listOprimes
from eratosthenes import eratosthenes
from eratosthenes import eratosthenesWithSpeedup
from euler import euler
from sundaram import sundaram
from numberline import printNumbers

def runSieve(n, sieve, toPrint):
    start = time.time()
    primes = sieve(n)
    end = time.time() - start

    if toPrint: printNumbers(sieve(n), n)
    if primes != truePrimes:
        print 'sieve of ' + sieve.__name__ + ' FAILED'
    print 'sieve of ' + sieve.__name__ + ' done in:', end

def parseArgs():
    if len(sys.argv) == 1:
        return 1000, False
    N = int(sys.argv[1])
    if len(sys.argv) == 2:
        return N, False
    printing = False
    if sys.argv[2] == '0':
        printing = False
    elif sys.argv[2] == '1':
        printing = True
    return N, printing

if __name__ == "__main__":
    print('---------------------BOOTING------------------------')
    N, printing = parseArgs()
    print 'sieving up to ', N
    if printing:
        print('printing is on')
    else:
        print('printing has been turned off')
    print('---------------------SIEVING------------------------')
    truePrimes = euler(N)
    # print truePrimes
    runSieve(N, eratosthenes, printing)
    runSieve(N, eratosthenesWithSpeedup, printing)
    runSieve(N, euler, printing)
    runSieve(N, sundaram, printing)
    # runSieve(N, )
