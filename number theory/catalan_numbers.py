# Program for computing catalan numbers for upto n (can also be used to compute nth catalan number)
# Catalan numbers are sequence of natural numbers defined recursively :
# C0 = 1 and C0(i + 1) = sigma(C(i), C(i-1)) from i from 0 to n
# To compute nth catalan number, we need to return catalan[n] as we are storing all catalan numbers till n - 1.
# Time  : 0(N^2), SPACE : 0(N)
def catalan(n):

    catalan = [0 for _ in range(n + 1)]
    catalan[0] = catalan[1] = 1
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan

# more optimized version to compute just the nth catalan number in 0(N) time and 0(1) space.

# function to return the binomal coefficent of n C k
def binom(n, k):
    # if k is greater than n that means , c(n, k) = c(n, n - k) using properties of binomial , helps to reduce calculation
    if k > n - k:
        k = n - k
    # initializing result
    res = 1
    for i in range(k):
        # calculating numerator part
        res *= n - i
        # calculating denominator part
        res /= i + 1
    return int(res)

# function to get nth catalan numbers
def catalan_binom(n):
    c = binom(2*n, n)
    return c / n + 1

# main function
if __name__ == '__main__':
    print(catalan(100))
    print(catalan_binom(3))
