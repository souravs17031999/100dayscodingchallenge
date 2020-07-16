# Program for counting labelled and unlabelled binary trees possible
# IDEA: Naive approach would be to compute all the permutations and combinations for the binary tree :
#--------------------------------------------------------------------
# The below example is explained for unlabelled trees.
#--------------------------------------------------------------------
# Like as we can see from the examples :
# T(0) : 1 (empty tree)       => 1
# T(1) : *                    => 1
# T(2) : *   *                => 2
#       *     *
#
# T(3) : *   *           *            *        *
#       *     *        *   *        *            *     => 5
#      *       *                     *          *
#
# T(4) ..... => 14
#---------------------------------------------------------------------
# Counting all the permutations and combinations is not so easy but surely we can observe a pattern
# : 1, 1, 2, 5, 14..... which is
# pattern formed by Catalan number.
# Also we can get the intuition by observing that for a n node, there are (i - 1) nodes on left sub tree , and
# (n - i) nodes on the right sub tree.
# nth catalan number is given by : T(n) = sigma [from i = 1 to n]( T(i - 1)T(n - i)) which givesn total number of
# unlabelled possible trees formed.
# Now, we can see for any given unlabelled combination, we can make n! permutations for labelled tree
# of labels to all nodes.
# So, number of labelled trees = (number of unlabelled trees) * n!
#-----------------------------------------------------------------------
# Labelled trees examples :
#    A            C
#  B   C        A   B ....
#------------------------------------------------------------------------
# function to return the binomal coefficent of n C k

# TIME : 0(N).
from math import factorial

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

# function to get nth catalan numbers  / number of unlabelled trees possible
def compute_unlablled(n):
    c = binom(2*n, n)
    return c // (n + 1)

# function to get number of labelled trees possible
def compute_labelled(n):
    unlabelled = compute_unlablled(n)
    return unlabelled * factorial(n)

# driver test function
if __name__ == '__main__':
    n = 100
    print(f"Total possible unlabelled trees for {n} nodes : {compute_unlablled(n)}")
    print(f"Total possible unlabelled trees for {n} nodes : {compute_labelled(n)}")
