# library for my own purpose , for resusing maths optimized functions
# can be used by using "import mathemagica as ma"
import math as m
class mathemagica:
    # program for efficient binomial coefficent calculation
    # The idea is to use following property :
    # c(n, k) = n!/(n-k)!*k! = n(n - 1)(n - 2)(n - 3)....1 / ((n - k)(n - k - 1)....1)*(k(k-1)(k-2)......1)
    # now, n! = n(n - 1).....(n-k)(n-k-1).....1 and that cancels one part of denominator
    # so, we are left with c(n, k) = n(n-1).....(n-k+1) / k(k-1)......1
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

    def factorial(n):
        pass

    def fib(n):
        return round((((1 + m.sqrt(5))/2)**n)/ m.sqrt(5))

    # function for transpose of matrix - logic is to swap the values in upper triangular and lowe triangular part keeping diagonal elements intact
    def transpose(mat):
        n = len(mat)
        for i in range(0, n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return mat
