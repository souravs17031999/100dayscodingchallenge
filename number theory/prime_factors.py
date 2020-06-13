# Program to compute prime factors in most efficient way
# IDEA: Naive solution takes 0(N) time,  One optimization to naive solution is that we can actually loop and iterate over sqrt(N) instaead of N because
# divisors occur in pairs, for the same reason as was in computing prime numbers.
# Time complexity then reduces to 0(Sqrt(N))
# But for range of queries, we can optimize it further using prime seives.

import math

def prime_factor(n):
    l = []  # list storing prime factors
    # iterating till sqrt(N)
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        # reducing number by keep dividing by the same number till it exhausts
        while (n % i == 0):
            l.append(i)
            n = n / i

    # handling prime number situation
    if n > 2:
        l.append(n)

    return l


# One more optimization is that, we can first exploit its composite parts by keep dividing by 2 and then once it's done, then start with 3 and then go over
# by jumping 2 each time, like 3, 5, 7, .... because whatever is left is odd number now onwards.
# def prime_factor3(n):
#     l = []
#     while n % 2 == 0:
#         l.append(2)
#         n = n / 2
#
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#             while (n % i == 0):
#                 l.append(i)
#                 n = n / i
#     if n > 2:
#         l.append(n)
#

if __name__ == '__main__':
    print(prime_factor(121))
