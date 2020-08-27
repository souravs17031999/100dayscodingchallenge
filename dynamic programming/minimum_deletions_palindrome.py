# Program for computing minimum number of deletions to make a given string a palindrome.
# This problem is again a variation of LPS ( evetually which is variation of LCS).
# So, we can actually check it from an example :
# EX.
# s  : "agbcba"
#       /  \  \
#    "bcb" "c" "abcba"
# we are deleting 3, 5, 1 characters respectively in the above string to get the palindromic substring.
# Now, we need to find the minimum of all of them which is 1, and the palindromic subsequence is "abcba".
# If we observe carefully, then first thing is that we can delete from anywhere so the resulting string is a subsequence
# and now important thing is that for minimizing the deletions, we need to get maximum length of paldindromic subsequence which is clear from above.
# Hence, for computing no. of min deletions :
# min deletions = len(string) - LPS(s)
# where, LPS(S) = LCS(S, reverse(S)).
# -----------------------------------------------------------------------------------------------------
# TIME : 0(N ^ 2)


# helper function to compute LCS
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

# helper function to compute LPS
def LPS(s):
    return LCS(s, s[::-1])


def compute_min_deletions(s):
    return len(s) - LPS(s)


print(compute_min_deletions("agbcba"))
