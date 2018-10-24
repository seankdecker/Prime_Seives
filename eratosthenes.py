'''
eratosthenes.py

Here we implement the Sieve of Eratosthenes!
As could probably be assumed, this sieve is
named after the Greek mathematician Eratosthenes of Cyrene.

The earliest known reference to and description of this sieve
is in Nicomachus of Gerasa's Introduction to Arithmetic.
'''

'''                     ALGORITHM

The Sieve of Eratosthenes works as follows:

1. Create a list of integers 2 up to some limit we define as n
2. Initialize p to 2, the smallest prime number
3. Starting at 2p enumerate the multiples of p in incerements of p up to n,
   removing them from the list
4. If p is the last number in the list stop. Otherwise set p to the next element
   in the list, which will be the next prime. Repeat step 3
5. Once this stops, we have a list of primes up to n

There is an obvious and immediate optimization we can do in which we instead of
starting at 2p, we start at p^2. We implement this in eratosthenesWithSpeedup()
'''

'''                     COMPLEXITY
TIME
The sieve of eratosthenes' work is in removing elements from the list it creates
It removes O(\sum_{p <= n} n/p)) elements when p is a prime
by Merten's Theorem, \sum_{p <= n} 1/p = ln ln n + M, where p is a prime, and M
is the Meissel-Mertens constant, in the limit as n goes to infinity
Thus the time complexity is
                            O(n * (lnln(n) + M))
The speedup of ending at n^1/2 though leads to a complexity of
                            O(n * (lnln(n) + M))

SPACE
The space complexity comes from the list we create. This is largest when we begin
at a length of n
                                O(n)
'''

# returns the list of primes up to n
# These primes are found by the Sieve of Eratosthenes
def eratosthenes(n):
    if n < 2: return []
    numbers = [i for i in range(2, n + 1)]
    p = 2
    while p <= n:
        multiple_of_p = 2 * p
        while multiple_of_p <= n:
            # print multiple_of_p
            if multiple_of_p in numbers:
                numbers.remove(multiple_of_p)
            multiple_of_p += p
        if numbers.index(p) + 1 == len(numbers): break
        p = numbers[numbers.index(p) + 1]
    return numbers


# returns the list of primes up to n
# This sieve is implemented the same as eratosthenes()
# but with the optimization of starting at p**2
# and ending when p**2 <= n
def eratosthenesWithSpeedup(n):
    if n < 2: return []
    numbers = [i for i in range(2, n + 1)]
    p = 2
    while p**2 <= n:
        multiple_of_p = p**2
        while multiple_of_p <= n:
            # print multiple_of_p
            if multiple_of_p in numbers:
                numbers.remove(multiple_of_p)
            multiple_of_p += p
        p = numbers[numbers.index(p) + 1]
    return numbers

if __name__ == "__main__":
    print('eratosthenes')
    eratosthenes(1000)
    print('eratosthenesWithSpeedup')
    eratosthenesWithSpeedup(1000)
