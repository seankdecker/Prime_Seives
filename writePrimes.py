'''
writePrimes.py

writes primes at primes.txt
up to come constant n
using a sieve
'''
if __name__ == '__main__':
    primesFile = open('primes.txt', 'w')
    primes = euler(100000)
    for prime in primes:
        primesFile.write(str(prime) + ' ')
    primesFile.write('\n')
    primesFile.close()
    print 'Done'
