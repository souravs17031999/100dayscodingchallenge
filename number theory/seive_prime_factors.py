# Program to generate factors of a number given range of queries multiple times
# IDEA: Naive solution is already dicussed in other sections for prime factors, let's move to optimized version.
# The logic is to precompute all the prime numbers using prime seives and then check divisibility by only the prime numbers as we
# know that factors will be prime numbers.
# In the worst case, we will be dividing and check for smallest possible number "2", so overall log(N) divison steps.
# So, overall Time : (Q*log(N)) where Q is number of queries, and N is maximum number given, SPACE : 0(N)
# This algorithm only works properly for numbers upto max range of 10^6 , beyond that memory problems can occur.
# Here, we have also ignored pre-computation time.

from sys import stdin, stdout
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

def factorize(n):
    prime = prime_seive()
    l = []

    i = 0  # pointer to the prime number array
    p = prime[0]  # start off with first prime

    # iterating over sqrt(N)
    while p * p <= n:
        # checking only for prime numbers as stored in our prime array
        while (n % p == 0):
            l.append(p)
            n = n / p

        i += 1  # incrementing each time
        p = prime[i]  # subsituting prime number value in place of p

    # handling prime number situation
    if n > 2:
        l.append(n)

    return l

# driver function
if __name__ == '__main__':
    # getting range of queries 
    t = int(stdin.readline().strip())
    while (t):
        number = int(stdin.readline().strip())
        print(factorize(number))
        t -= 1
