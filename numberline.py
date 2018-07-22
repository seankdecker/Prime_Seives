"""
numberline.py

Here we create a numberline to be used by a sieve
in order to print out primes
"""
import sys

SPACING = 4

class colors:
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printPrimes(primes, n):
    for i in range(n):
        if i in primes:
            sys.stdout.write(colors.PINK + str(i) + colors.END)
        else:
            sys.stdout.write(str(i))
        for _ in range(SPACING - len(str(i))):
            sys.stdout.write(' ')
    sys.stdout.write('\n')

if __name__ == "__main__":
    pass
