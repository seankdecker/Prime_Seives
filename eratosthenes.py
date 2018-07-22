"""
eratosthenes.py

Here we implement the Sieve of Eratosthenes!
This is a pretty easy sieve to implement
"""

# returns the set primes from 2 up to n
# These primes are found by the Sieve of Eratosthenes
def eratosthenes(n):
    if n < 2: return []
    numbers = range(2, n + 1)
    i = 0
    while numbers[i]**2 <= n:
        multiple_of_i = numbers[i]**2
        while multiple_of_i <= n:
            if multiple_of_i in numbers:
                numbers.remove(multiple_of_i)
            multiple_of_i += numbers[i]
        i += 1
    return numbers


if __name__ == "__main__":
    for i in range(12):
        print i, " :  ", eratosthenes(i)
