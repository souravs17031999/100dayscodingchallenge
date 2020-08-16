# Program for computing shortest common supersequence.
# We need to compute shortest length possible for supersequence meaning a string comprising both strings
# as subsequences which is shortest.
# input : str1 = "geek",  str2 = "eke"
# output : "geeke", where we can see length is 5, and both strings are part as subsequences of output string.
# -----------------------------------------------------------------------------------------------------------------
# If we observe carefully, then this is a similar problem to LCS, longest common subsequences.
# Now, what can we do if are simply writing supersequence in the worst case, then we can write (taking ex. from above)
# "geekeke", and now we can see LCS is common to both, but this has been accounted two times, and so we need to
# subtract the LCS from length of both strings.
# Like LCS = "ek" which is present in both parts of final concatenation of string : "geekeke"
#                                                                                      ____
# hence, output : m + n - LCS(m, n), where m, n is length of individual strings.
# ------------------------------------------------------------------------------------------------------------------
# TIME : 0(M * N)

def LCS(s1, s2, m, n):

    dp = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 0

    for i in range(n + 1):
        dp[0][i] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def compute_shortest_supersequence(s1, s2):
    m, n = len(s1), len(s2)
    l = LCS(s1, s2, m, n)
    return m + n - l

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(compute_shortest_supersequence(X, Y))
