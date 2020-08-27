# Program for computing longest common subsequence for the two given strings.
# --------------------------------------------------------------------------------------
# Naive approach would be to generate all the substrings and then check which one is common to both
# and also update the length in that same iteration.
# So, that would be expensive exponential operation.
# -----------------------------------------------------------------------------------------
# So, we would have to deeply think about how do we actually compute this using recursion tree visualization :
# its' no more different than what we have seen in other problems
# we make call to lcs("s1", "s2")
#
#               lcs("AXYT", "AYZX")
#                    /        \
#    LCS("AXY", "AYZX")       LCS("AXYT", "AYZ")
#        /           \                     /              \
# LCS("AX", "AYZ")  LCS("AXY", "AYZ")  LCS("AXY", "AYZ")  LCS("AXYT", "AY")
#                        __________         __________
#
# now, we compare last two chars, and then if they are equal then we chop off that char from both string,
# and then it will be 1 + lcs("s1-matching_char", "s2-matching_char")
# similarly, if there is no match, then we would have to think , there is a competion between either of the chars being chopped off
# let's say last char of s1 => "a", and last char of s1 => "b", so, it will be max(lcs("s1-a"), lcs("s2-b")).
# So, this proves that this problem has optimal substruture property and drawing out this recursion tree will yield overalapping
# subproblems.
# Hence, we are going to use DP.
# ---------------------------------------------------------------------------------------------
# In the dp table we are filling , it's very similar actually if we see recurence relations and match it against our intuitive understanding
# Make dimensions of one more length, because of base case (extra string).
# in the matrix, when we match a char, then we simply chop off both, that means going up and going left , so we would end up at dp[i - 1][j - 1] + 1
# now, when there is a mismatch, then we simply take max(both chopped off from their respective string), so we go left, we go up and get max of those.
# -------------------------------------------------------------------------------------------------
# TIME : 0(M * N), SPACE : 0(M * N), M, N IS length OF STRINGS.
# Here also we can think of state and dimensions of dp, what is important for us is that last char of both strings, so dp[i][j], where i and j are
# pointing to last chars of both strings.
# --------------------------------------------------------------------------------------------------
# If we need to print the lcs, then we can simply start traversing the matrix created above starting from rightmost corner,
# and going up till leftmost corner and tracing back from where we got till where.
# So, if chars of both strings are same, include this in answer,
# Else compare values of L[i-1][j] and L[i][j-1] and go in direction of greater value.
# This can be done using one while loop and two pointers i, j.


# SIMPLE RECURISVE SOLUTION :
def compute_max_subsequence_recr(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0

    if s1[m - 1] == s2[n - 1]:
        return 1 + compute_max_subsequence_recr(s1, s2, m - 1, n - 1)

    return max(compute_max_subsequence_recr(s1, s2, m, n - 1), compute_max_subsequence_recr(s1, s2, m - 1, n))


# topdown memoized
cache = {}
def compute_max_subsequence_memo(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0

    if (m, n) in cache:
        return cache[(m, n)]

    if s1[m - 1] == s2[n - 1]:
        cache[(m, n)] = 1 + compute_max_subsequence_memo(s1, s2, m - 1, n - 1)
        return cache[(m, n)]

    cache[(m, n)] = max(compute_max_subsequence_memo(s1, s2, m, n - 1), compute_max_subsequence_memo(s1, s2, m - 1, n))
    return cache[(m, n)]



# BOTTOM UP DP OPTIMIZED:
def compute_max_subsequence(s1, s2):

    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == '__main__':
    print(compute_max_subsequence("AGGTAB", "GXTXAYB"))
    print(compute_max_subsequence_recr("AGGTAB", "GXTXAYB", 6, 7))
    print(compute_max_subsequence_memo("AGGTAB", "GXTXAYB", 6, 7))
