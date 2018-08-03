"""
eratosthenes.py

Here we implement the Sieve of Eratosthenes!
As could probably be assumed, this sieve is
named after the Greek mathematician Eratosthenes of Cyrene.

The earliest known reference to and description of this sieve
is in Nicomachus of Gerasa's Introduction to Arithmetic.

The Sieve of Eratosthenes works as follows:

1. Create a list of integers 2 up to some limit we define as n
2. Initialize p to 2, the smallest prime number
3. Starting at 2p enumerate the multiples of p in incerements of p up to n,
   removing them from the list
4. If p is the last number in the list stop. Otherwise set p to the next element
   in the list, which will be the next prime. Repeat step 3
5. Once this stops, we have a list of primes up to n

There is an obvious and immediate optimization we can do in which we instead of
starting at 2p, we start at p^2.
"""

# returns the list of primes up to n
# These primes are found by the Sieve of Eratosthenes
def eratosthenes(n):
    if n < 2: return []
    numbers = range(2, n + 1)
    p = 2
    while p**2 <= n:
        multiple_of_p = 2 * p
        while multiple_of_p <= n:
            if multiple_of_p in numbers:
                numbers.remove(multiple_of_p)
            multiple_of_p += p
        p = numbers[numbers.index(p) + 1]
    return numbers


# returns the list of primes up to n
# This sieve is implemented the same as eratosthenes()
# but with the optimization of starting at p**2
# and ending when p**2 <= n
def eratosthenesWithSpeedup(n):
    if n < 2: return []
    numbers = range(2, n + 1)
    p = 2
    while p**2 <= n:
        multiple_of_p = p**2
        while multiple_of_p <= n:
            if multiple_of_p in numbers:
                numbers.remove(multiple_of_p)
            multiple_of_p += p
        p = numbers[numbers.index(p) + 1]
    return numbers

if __name__ == "__main__":
    for i in range(12):
        print i, " :  ", eratosthenesWithSpeedup(i)
