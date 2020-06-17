# Program to compute sqrt efficiently using binary search in 0(lg(N)) where N is number.
# We use same concept of monotonicity and finding search space, so here also we know our bounds, the answer will lie between 0 - N, or more strictly,
# 0 - sqrt(N)
# So, we can set it our bounds and this all possibilities insider this range is already in sorted order, we use binary search to compute and check for every
# number if there is possibility of square that is perfect and return it or whatever the nearest number is.

import math
def sqrt_bin_search(n):
    if n == 0 or n == 1:
        return n

    start, end = 1, n  # more optimization by setting higher bound to sqrt(n)
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return mid

        elif mid * mid < n:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return mid

# For some precision , for real numbers, we can also newton-raphson's method for computing it using iterative algorithm to converge
# newton's raphson method is derived from drawing a ling as a tangent to the function f(x) at x = xi, then xi + 1 is the point at which this tangent cuts
# at x-axis
# formula by newton-raphson method : x(n+1) = x(n) - f(x)/f'(x) which gives next iterative value and this goes on until desired precision is acheived
# deriving for f(x) = 0, so f(x) = x^2 - n for given number n which will be used to compute square root of n.
# putting f(x) for sqrt in the above formula will yield,
# x(n+1) = (x(n) + (n/x(n))) / 2
# This takes much lesser time than 0(lg(N)) 

def sqrt_newton(n):
    x = 1
    eps = 1e-15
    while (1):
        xn = (x + (n / x)) / 2
        if abs(x - xn) < eps:
            break
        x = xn
    return x

if __name__ == '__main__':
    print(sqrt_bin_search(10)) #4
    print(sqrt_newton(10)) #3.162277660168379
