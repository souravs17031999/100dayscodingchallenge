# Program to find the count of divisors for a given number
# IDEA: Naive solution will take 0(N) but then also we can optimize it further with the fact that we can simply represent number as a prime factorization form
# represented in form a(i) ^ p(i) where p(i) are the powers of a(i) which are prime factors.
# So, total number of divisors (mathematical formula): (p0 + 1)*(p1 + 1)*(p2 + 1)*.......*(pn + 1)
# Time complexity : 0(N), with SPACE : 0(N)
# APPLICABLE FOR MEMORY CONTRAINT AS WE ARE ONLY HOLDING UPTO 10^6 PROBABLY GOOD FOR CP ENVIRONMENT BUT NOT FOR PRODUCTION.

import math

MAX_SIZE = 100005

# function to precompute prime numbers using seive
def prime_seive():
    # list of all numbers
    prime = [1 for _ in range(MAX_SIZE + 1)]
    i = 2
    # going from 2 to sqrt(n)
    while(i * i <= MAX_SIZE):
        # if found prime, then mark all multiples as composite
        if prime[i]:
            # starting with i * i (prime numbers' square)
            for j in range(i * i, MAX_SIZE + 1, i):
                prime[j] = 0
        i += 1

    # printing the prime numbers marked as True

    prime[0], prime[1] = 0, 0

    # Note : Just one tweak here, that instead of keeping "1's " and "0's ",
    # we created new array consisting of only prime numbers.
    primes = []
    for i in range(2, MAX_SIZE + 1):
        if prime[i]:
            primes.append(i)

    return primes

# FUNCTION TO COUNT THE DIVISORS
def counting_divisors(n):
    # building the prime numbers array
    prime = prime_seive()

    i = 0  # pointer to the prime number array
    p = prime[0]  # start off with first prime
    # res will contain the overall count of divisors
    res = 1
    # iterating over prime number array, so that we only divide and check by prime numbers as for prime factorization
    while p * p <= n:
        power = 0 # power contains the power of the prime factors
        # checking only for prime numbers as stored in our prime array
        while (n % p == 0):
            power += 1
            n = n / p

        i += 1  # incrementing each time
        p = prime[i]  # subsituting prime number value in place of p

        res *= (power + 1)
    # handling prime number situation
    if n > 2:
        res *= (power + 1)

    return res

if __name__ == '__main__':
    n = 60
    print(f"Total number of divisors of number {n} : {counting_divisors(n)}")
