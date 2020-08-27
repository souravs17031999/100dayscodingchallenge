# Program for computing length of longest palindrome subsequence.
# EX.
# S => "agbcba",
# Now, we can generate various subsequences but we will take only palindromic subsequences in a set, and then compute the length of all
# and get the longest of them but time complexity is expoential.
# Now, we will see in terms of DP.
# If we think about optimal substructure property and palindrome definition, then we can think it as first and last char should match, if not then we
# need to check if there is any other match keep one side same, and another side length decreases.
# That means :
# Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest palindromic subsequence of X[0..n-1].
# If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2
# Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).
# Also, overlapping subproblems :
#
# #              L(0, 5)
#              /        \
#             /          \
#         L(1,5)          L(0,4)
#        /    \            /    \
#       /      \          /      \
#   L(2,5)    L(1,4)  L(1,4)  L(0,3)
#
# So, DP can be applied clearly and also this problem is an variation of LCS.
# In LCS we need  two strings but here we only have one string, and since second string should be derivable from first string.
# Now, given we have to find palindromic subsequence, that means we can take second string as reverse of first string and compute LCS of them.
#
# LPS(S) = LCS(S, REVERSE(S))
# ------------------------------------------------------------------------------------------------------------------------------------------

# helper function for computing LCS
def LCS(s1, s2):

    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def compute_longest_palindrome_subs(s):
    return LCS(s, s[::-1])


if __name__ == '__main__':
    print(compute_longest_palindrome_subs("GEEKS FOR GEEKS"))
