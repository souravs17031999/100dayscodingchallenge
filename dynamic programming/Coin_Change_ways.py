# Program for counting all the unique distinct ways for making up denominations of some given value "N" for given
# denominations : {1, 2, ..... N}.
# ------------------------------------------------------------------------------------
# Let's say we are given [1, 3, 5] coins and we need to make up to amount = 5.
# So, we start with 1, then remaining amount = 5 - 1 => 4.
# Now, again we have choice to choose from [1, 3, 5] to make up to 4.
# if we again choose 1, then again remaining count => 4 - 1 => 3.
# at every recursion call level, we call for every possible coin denominations value,
# so, overall denominations ^ (max-level), that is exponential.
#
# [1, 3, 5]
#  choose this "1"   => 3 ways
# [1, 3, 5]
# choose this "1"  => 3 ways
# [1, 3, 5]
# choose this "1"  => 3 ways
# [1, 3, 5]
# choose this "1"  => 3 ways
# [1, 3, 5]
# choose this "1"   => 3 ways
# so, total : 3 ^ 5 calls, which is exponential when going for much larger numbers.
# -------------------------------------------------------------------------------------
# So, we can see and prove correctness for applying DP here : optimal substructure, and overlapping subproblems.
# ------------------------------------------------------------------------------------
# dimensions of dp , state is associated with dp[coin][value]
# at every cell, we actually for every coin have two possible options : either we take this or we don't take this.
# so, again like knapsack problem, we can write recurrence so that if we take the coin, then amount will be now reduced,
# but if we don't take that coin, then same amount.
# Total solutions will be sum of both solution sets (those which we don't take, those which we take)
# -------------------------------------------------------------------------------------
# C({1,2,3}, 5)
#                            /             \
#                          /                 \
#              C({1,2,3}, 2)                 C({1,2}, 5)
#             /       \                      /      \
#            /         \                    /         \
# C({1,2,3}, -1)  C({1,2}, 2)        C({1,2}, 3)    C({1}, 5)
#                /    \             /     \           /     \
#              /       \           /       \         /        \
#     C({1,2},0)  C({1},2)   C({1,2},1) C({1},3)    C({1}, 4)  C({}, 5)
#                    / \     / \        /\         /     \
#                   /   \   /   \     /   \       /       \
#                 .      .  .     .   .     .   C({1}, 3) C({}, 4)


def compute_total_ways(coins, m, N):

    dp = [[None] * m for _ in range(N + 1)]

    for i in range(m):
        dp[0][i] = 1

    for i in range(1, N + 1):
        for j in range(m):
            x = dp[i - arr[j]][j] if i-arr[j] >= 0 else 0
            y = dp[i][j-1] if j >= 1 else 0
            dp[i][j] = x + y

    return dp[N][m - 1]






if __name__ == '__main__':

    arr = [1, 2, 3]
    print(compute_total_ways(arr, 3, 4))
