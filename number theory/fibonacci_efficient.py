# program to sum up even fibonacci terms, one of the trick is to use golden ration to calculate fibonacci terms using the formula used below and then second trick is to only calculate even value terms without checking every number in the range , due to the fact that every third number in the series is already known even value, so keep and counter and increment it by 3 and then sum it up.
# here, we are only required to sum up the terms until that sum exceed 4000000

import math
# function to calculate fibonacci nth term
def fib(n):
    numr = pow((math.sqrt(5) + 1) / 2, n)
    return round(numr / math.sqrt(5))

# function to sum up even valued fib terms
def sum_even_fib():
    n = 0
    sum = 0
    while(fib(n) < 4000001):
        sum = sum + fib(n)
        n = n + 3
    return sum

# main function
if __name__ == '__main__':
    print(sum_even_fib())
