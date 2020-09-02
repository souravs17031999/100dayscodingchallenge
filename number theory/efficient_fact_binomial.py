# Program for efficient computation of binomial coefficient using factorials.
# We have already seen the efficient method of fact computation using DP, and that we are going to use it for binomial computations.
# The MAX_VALUES Depends on the contraints given in the problem.

MAX_INT = 100
import sys
def get_fact():

    fact = [0] * MAX_INT
    fact[0] = 1
    for i in range(1, len(fact)):
        fact[i] = (fact[i - 1] * i) % sys.maxsize

    return fact

def get_binom(n, k, factorial):
    return factorial[n] // (factorial[k] * factorial[n - k])

factorial = get_fact()
print(get_binom(40, 2, factorial))

# Use pascal's triangle to generate DP bottom up table.
