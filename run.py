"""
run.py

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
from numberline import printNumbers

def runSieve(n, sieve):
    start = time.time()
    printNumbers(sieve(n), n)
    print "sieve of " + sieve.__name__ + " done in:", time.time() - start

if __name__ == "__main__":
    runSieve(1000, eratosthenes)
