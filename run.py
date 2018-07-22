"""
run.py

This is the thing to run!
Just type

    python run.py [the sieve to run]

"""
import sys
from listOprimes import listOprimes
from eratosthenes import eratosthenes
from numberline import printPrimes

if __name__ == "__main__":
    printPrimes(listOprimes(200), 200)
    printPrimes(eratosthenes(200), 200)
