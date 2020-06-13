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

    def count_digits(n):
        return int(math.log10(n) + 1)

    # fast exponentiation algo
    def expo(a, n):
        ans = 1
        while n > 0:
            if n & 1:
                ans *= a

            a *= a
            n = n >> 1

        return ans

    # gives position of rightmost set bit , as in 1-based indexing from right to left
    def right_set(n):
        return math.log2(n & -n) + 1

    # returns bool depending upon if the number is a power of two
    def check_power_2(n):
        return(math.ceil(math.log(n) // math.log(2)) == math.floor(math.log(n) // math.log(2)))

    # Given two integers N and K, the task is to find the Kth root of the number N.
    def nth_root(n, k):
        return pow(k, (1.0 / k) * (math.log(n) / math.log(k)));

    # Given two integers N and K, the task is to check if Y is power of X or not.
    def check_nth_root(n, k):
        res1 = math.log(N) / math.log(K)
        res2 = math.log(N) / math.log(K)
        return (res1 == res2)

    # To find the power of K greater than equal to and less than equal to N:
    def check_power(n, k):
        pass
