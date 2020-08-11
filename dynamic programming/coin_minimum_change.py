# Program to compute minimum number of coins possible to make up some given amount.
# Recursion tree overlapping subproblems visualized.
# Like, ex. [1, 2, 3, 5], and amount = 11,
#
#                   11
#                / | | \
#              10  9 8   6
#
#          ......................
#
# ------------------------------------------------------------------
# OPTIMIZED SOLUTION USING DP[coin][value] :
# NOTE : IT CAN BE OPTIMIZED USING 1-D ARRAY.

# base cases matrix filled with
#
#
#       0 1 2 3 ...... N
#   1   0 1 2 3 ....... N
#   2   0
#   3   0
#   5   0
# Now, recurrence relations :
for ():
    for ():
        if j >= coin[i]:
            dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coin[i]])
        else:
            dp[i][j] = dp[i - 1][j]


# OPTIMIZED USING 1-D ARRAY:

dp[i] = min(dp[i], dp[i - coins[j]]) if i > coins[j]
