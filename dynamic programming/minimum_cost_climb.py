# Program for computing the minimum cost for climbing the stairs to the highest building.
# We can either start from first and second index at every time.
# EX.
# INPUT : [16, 19, 10, 12, 18]
# OUTPUT : 31
# 19 -> 12
# INPUT : [2, 5, 3, 1, 7, 3, 4]
# OUTPUT : 9
# 2-> 3-> 1->3
# ---------------------------------------------------------------------------------------------------------------------------
# We use DP to solve this.
# At every state, we store the subproblem of finding the minimum cost to reach ith step.
# We can clearly see the optimal substructure and overlapping subproblems.

def compute_cost(cost, n):

    dp = [None] * n
    if n == 1:
        return cost[0]

    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    print(dp)
    return min(dp[n - 2], dp[n - 1])


a = [16, 19, 10, 12, 18 ]
n = len(a)
print(compute_cost(a, n))
