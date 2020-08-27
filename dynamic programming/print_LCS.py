# We have already discussed the computation of longest common subsequence.
# Now, we just want to print the LCS.
# So, we already know how the algorithm works, now we just reverse engineer the algorithm already designed,
# and focus on how the two pointers pointing to last char moves.
# We start with two pointers along with an empty string, pointing to the last char of the two strings, hence our position in the dp table will be somehting like dp[m][n],
# and now, we check if the two chars match, then we append the char to our result string and then move both pointers in the diagonal, i--, j--
# but if they don't match, then depending on the max direction, we move in that direction and donnot add anything to our result string.
# We keep doing this until one of the pointers hit empty string that is "0", then we have answer in our result string build so far.


# helper function to compute the LCS and return the table
import sys
def compute_max_subsequence(s1, s2):

    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # for i in range(m + 1):
    #     dp[i][0] = 0
    #
    # for i in range(n + 1):
    #     dp[0][i] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp

def print_LCS(s1, s2):
    dp = compute_max_subsequence(s1, s2)
    result = []
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    print("".join(result)[::-1])


if __name__ == '__main__':
    print_LCS("AGGTAB", "GXTXAYB")
    
