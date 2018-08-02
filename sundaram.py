'''
sundaram.py

Here we implement the Sieve of Sundaram
This sieve was discovered by S.P. Sundaram in
1934. I had a hard time finding any other information
about it though.

It works as follows:
1. Create a list of integers from 1 to up to some limit we define as m.
   (we will get all primes up to (m + 1) * 2
2. From this list, remove all numbers of the form i + j + 2ij where i, j
   are natural numbers, 1 <= i <= j
3. Multiply each element in the list by 2 and add 1. Add 2 to your list
4. You are left with all primes except 2giving a list of the odd prime numbers (i.e., all primes except 2) below 2n + 2.

The sieve of Sundaram sieves out the composite numbers just as sieve of Eratosthenes does, but even numbers are not considered; the work of "crossing out" the multiples of 2 is done by the final double-and-increment step. Whenever Eratosthenes' method would cross out k different multiples of a prime {\displaystyle 2i+1} 2i+1, Sundaram's method crosses out {\displaystyle i+j(2i+1)} i + j(2i+1) for {\displaystyle 1\leq j\leq \lfloor k/2\rfloor } 1\le j\le \lfloor k/2\rfloor.
'''
import math

# returns the list of primes up to n
# These primes are found by by Sundaram's Sieve
def sundaram(n):
    if n < 2: return []
    m = (n - 1)/2
    numbers = range(1, m + 1)
    # i + j + 2ij = m  => 2i + 2i^2 = m = 0 = i + i^2 - m/2 =>
    for i in range(1, m): #int(math.sqrt(m))):
        for j in range(i, m): #int(math.sqrt(m))):
            # print (i + j + 2*i*j)
            if i + j + 2*i*j > m: continue
            if i + j + 2*i*j in numbers:
                numbers.remove(i + j + 2*i*j)
    numbers = [2 * i + 1 for i in numbers]
    return numbers

if __name__ == '__main__':
    print(sundaram(100))
