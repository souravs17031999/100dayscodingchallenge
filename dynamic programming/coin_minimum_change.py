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
#   1   0 ....INT_MAX....
#   2   0 ...int_max or 1... *
#   3   0
#   5   0
#
# NOTE* : Second row is also initialized here, in the way that, it denotes that size of array is 1, and so if we want to make upto coins sum N,
# so, either we can do it direclty or we can't do it anyhow, so in former case we can check it by dividing value at array by coin value, and in
# latter case if not able to make upto N, then we will put INT_MAX.

# Now, recurrence relations :
import sys 
def compute_coins():
    n = len(coins)
    dp = [[0 for _ in range(V + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, V + 1):
        dp[0][i] = sys.maxsize
    
    for i in range(1, V + 1):
        if i % coins[0] == 0:
            dp[1][i] = 1
        else:
            dp[1][i] = sys.maxsize
    
    for i in range(2, n + 1):
        for j in range(1, V + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][V]


# OPTIMIZED USING 1-D ARRAY:

dp[i] = min(dp[i], dp[i - coins[j]]) if i > coins[j]
