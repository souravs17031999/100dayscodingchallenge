# Program for computing the fewest cuts possible for palindromic paritioning.
# EX.
# This is a variation of MCM.
# Actually, we can again think in same lines, i and j should point to the leftmost index and rightmost index
# and we have to try for all possible values from i to j where we could do a partition.
# At worst, we can partition after every char in the string, that is n-1, where n is length of string.
# Now, if the string is already a palindrome , then we can directly return 0.
# otherwise we can break it into subproblems, that is from i...k, and then k + 1....j, and add the cost for these two calculated answer which is "1".
# and we take minimum of all these partitions.
# --------------------------------------------------------------------------------------------------------

# SIMPLE RECURSION ---------------------------------------------------------------------------------------
# TIME : EXPONENTIAL

import sys
def is_palindrome(s):
    return s == s[::-1]

def compute_min_partitions(s, left, right):

    if left >= right:
        return 0

    if is_palindrome(s[left : right + 1]):
        return 0

    min_partitions = sys.maxsize
    for k in range(left, right):
        temp = 1 + compute_min_partitions(s, left, k) + compute_min_partitions(s, k + 1, right)
        min_partitions = min(temp, min_partitions)

    return min_partitions

# --------------------------------------------------------------------------------------------------------
# TOP DOWN MEMOIZED
# --------------------------------------------------------------------------------------------------------
# TIME : 0(N^3)

cache = {}
def compute_min_partitions_memo(s, left, right):

    if left >= right:
        return 0

    if is_palindrome(s[left : right + 1]):
        return 0

    if (left, right) in cache:
        return cache[(left, right)]

    min_partitions = sys.maxsize
    for k in range(left, right):
        temp = 1 + compute_min_partitions_memo(s, left, k) + compute_min_partitions_memo(s, k + 1, right)
        min_partitions = min(temp, min_partitions)

    cache[(left, right)] = min_partitions
    return min_partitions

# MORE OPTIMIZATIONS :
# TIME : 0(N^2)

cache = {}
def compute_min_partitions_mod(s, left, right):

    if left >= right:
        return 0

    if is_palindrome(s[left : right + 1]):
        return 0

    if (left, right) in cache:
        return cache[(left, right)]

    min_partitions = sys.maxsize
    for k in range(left, right):

        if (left, k) in cache:
            return cache[(left, k)]
        else:
            left = compute_min_partitions_mod(s, left, k)
            cache[(left, k)] = left

        if (k + 1, right) in cache:
            return cache[(k + 1, right)]
        else:
            right = compute_min_partitions_mod(s, k + 1, right)
            cache[(left, k)] = right

        temp = 1 + left + right
        min_partitions = min(temp, min_partitions)

    cache[(left, right)] = min_partitions
    return min_partitions


if __name__ == '__main__':
    s = "ababbbabbababa"
    print(compute_min_partitions(s, 0, len(s) - 1))
    print(compute_min_partitions_memo(s, 0, len(s) - 1))
    print(compute_min_partitions_mod(s, 0, len(s) - 1))
