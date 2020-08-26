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
#   2   0 ...int_max or 1... *
#   3   0
#   5   0
#
# NOTE* : Second row is also initialized here, in the way that, it denotes that size of array is 1, and so if we want to make upto coins sum N,
# so, either we can do it direclty or we can't do it anyhow, so in former case we can check it by dividing value at array by coin value, and in
# latter case if not able to make upto N, then we will put INT_MAX.

# Now, recurrence relations :
for ():
    for ():
        if j >= coin[i]:
            dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coin[i]])
        else:
            dp[i][j] = dp[i - 1][j]


# OPTIMIZED USING 1-D ARRAY:

dp[i] = min(dp[i], dp[i - coins[j]]) if i > coins[j]
