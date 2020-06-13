# Program to compute modular inverse for a given number such that a*x + b*y = 1, find x.
# computation for (a.b) % m = 1, where m is in range : [1, m-1]
# This is basically application of modular exponentiation
# TIME : 0(log(M))

def mod_exp(a, b, m):

    ans = 1
    a = a % m

    if a == 0:
        return 0

    while b > 0:
        if b & 1:
            ans = (ans * a) % m
        a = (a * a) % m
        b = b // 2
    return ans


def mod_inverse(a, n):
    return mod_exp(a, m-2, m)
