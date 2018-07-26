"""
euler.py

Here we implement Euler's Sieve!
This Sieve appears in Euler's proof of the
Zeta product formula and was rediscovered and
analyzed by Gries and Misra.

This sieve can be thought of as an optimized Sieve of
Eratosthenes in which each composite number is removed
exactly once.

This sieve works as follows:

1. Create a list of integers 2 up to some limit we define as n
2. Initilize p to be 2
3. Multiply p by itself and mark the result in the list. Coninue to do this
   for each element after p until the result is past out our limit n.
4. Remove all marked elements from the list
4. Let p be the next element in the list, which will be the next prime. If p^2
   is > n, then stop, else repeat step 3
5. After the stop, we should have a list of prime numbers up to n
"""

# returns the list of primes up to n
# These primes are found by by Euler's Sieve
def euler(n):
    if n < 2: return []
    numbers = range(2, n + 1)
    p = 2
    while p**2 <= n:
        i = numbers.index(p)
        toRemove = []
        while p * numbers[i] <= n:
            toRemove.append(p * numbers[i])
            i += 1
        for num in toRemove:
            numbers.remove(num)
        p = numbers[numbers.index(p) + 1]
    return numbers

if __name__ == "__main__":
    euler(10)
