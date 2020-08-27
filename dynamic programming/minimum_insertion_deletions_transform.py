# Program for printing minimum insertions and deletions required to transform a string "X" to string "Y".
# This question is solved using the concept of LCS.
# Now, when we insert and delete the string "X" to transform into "Y".
#
# X : "str1 = "heap"
# Y : "str2" = "pea"
#
# Now, when we go to X, then first we insert p infront of str1, so str1 => "pheap"
# Then, we delete "h" and "p" to transform into "pea".
# So, total 1 insertion and 2 deletions.
# Thus, if we observe carefully then, remaining string in X and Y is the LCS(X, Y).
# LCS(X, Y) => "ea"
# Only this LCS is not changed, other chars changed.
# Now, to transform X to Y, first we insert X => LCS and then LCS to Y.
# So, minimum deletions : len(X) - LCS(X, Y)
# and minimum insertions : Len(Y) - LCS(X, Y)
#
#     (s1)"heap"    "pea"  (s2)
#           \      /
#             "ea" (LCS)
#
# -----------------------------------------------------------------------------------------------------------------
# TIME : 0(M * N), M AND N ARE LENGTHS OF TWO STRINGS.

import sys
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

def compute_min_insert_del(s1, s2):

    deletions = len(s1) - LCS(s1, s2)
    insertions = len(s2) - LCS(s1, s2)

    print(f"insertions : {insertions}, deletions : {deletions}")

if __name__ == '__main__':
    str1 = "heap"
    str2 = "pea"
    compute_min_insert_del(str1, str2)
