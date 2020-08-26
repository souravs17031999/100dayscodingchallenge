# Program for computing maximum value by cutting the rod in given pieces.
# rod cutting problem basically defines the following  :
# We have been given a rod of length L, and a length array containing lengths of different measurements, and price array containing price for
# different segments, and finally, we need to compute the max value / price obtained after cutting the rod of length L by cutting various segments.
# length   | 1   2   3   4   5   6   7   8
# price    | 1   5   8   9  10  17  17  20
# L= 8, output : 22
# length   | 1   2   3   4   5   6   7   8
# price    | 3   5   8   9  10  17  17  20
# Length = 8, output = 24.
# -------------------------------------------------------------------------------------------------
# If we observe carefully, then it matches knapsack problem and it exactly matches with Unbounded knapsack problem as here we can cut the
# rod into segments of same type more than once.
# Since, let's say if we have rod of length = 4m, then we can say rod of length 2 + 2, and we can also go for 1 + 1 + 2 and so on....
# Now, the code is completely same with knapsack problem.
# Weight array is matched with  : length array
# profit array is matched with  : price array
# W is matched with : N.
# ------------------------------------------------------------------------------------------------

#
# cR() ---> cutRod()
#
#                              cR(4)
#                   /        /
#                  /        /
#              cR(3)       cR(2)     cR(1)   cR(0)
#             /  |         /         |
#            /   |        /          |
#       cR(2) cR(1) cR(0) cR(1) cR(0) cR(0)
#      /        |          |
#     /         |          |
#   cR(1) cR(0) cR(0)      cR(0)
#    /
#  /
# CR(0)

def compute_max_value(val, wt, W, n):

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            if i == 0 and j == 0:
                dp[i][j] = 0

            elif j >= wt[i - 1]:
                dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j]) # just one line optimized

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]

price = [1, 5, 8, 9, 10, 17, 17, 20]
arr = [i for i in range(1, len(price))]
size = len(arr)

print(compute_max_value(price, arr, 8, size))
