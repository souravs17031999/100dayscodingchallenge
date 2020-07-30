# program to calculate gcd of two numbers in most efficient way,
# IDEA: logic is to use euclid's algorithm which says, gcd(a, b) = gcd(b, a%b) and gcd(a, b) = 0, when b = 0.
# or it can be also expressed as gcd doesn't changes if we subtract smaller number from larger number.
# For example, 21 is the GCD of 252 and 105 (as 252 = 21 × 12 and 105 = 21 × 5), and the
# same number 21 is also the GCD of 105 and 252 − 105 = 147
# Slightly optimized version of actual euclid's algorithm is replacing subtraction operation by moduli operator.
# TIME : (log(min(a, b))), SPACE : variable , depends on recursion calls for stack limit.
import sys

sys.setrecursionlimit(10**6)

def gcd1(a, b):
    return a if b == 0 else gcd1(b, a % b)


# actual euclid's algo : one more way
# def gcd2(a, b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     if a == b:
#         return a
#     elif a > b:
#         return gcd2(a - b, b)
#     else:
#         return gcd2(a, a - b)

# One more useful application is extended euclid's algorithm, which are helpful in various applications
# idea is to compute x and y along with gcd, such that, a*x + b*y = gcd(a, b)

# def gcd_extended(a, b):
#     if b == 0:
#         return b, 0, 1
#
#     gcd, x1, y1 = gcd_extended(b, a % b)
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd, x, y


if __name__ == '__main__':
    print(gcd1(100089, 200000))
