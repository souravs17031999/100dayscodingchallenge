# Program for computing maximum weight that can be filled in KnapSack of max. weight "W".
# Given input two arrays : weights [1.....n], profit (values) [1......n]
# for item number 1.....n
# --------------------------------------------------------------------------------------
# If it would be fractional, then greedy would work.
# But since here either we can take the item or not take the item (include in KnapSack or not include in KnapSack).
# So, greedy will not give the best optimal solution for this case.
# Hence, we have to generate all possible subsets and get the maximum out of this, using recursion we can acheive this.
# As at every point of time, we compare with the weight constraint , then either we can take that item or not take the
# item as it is not always necessary that we will take that item because along with that our no. of remainining items
# will be also decreasing.
# So, we need to get max of both cases (defining optimal substructure):
# Maximum value obtained by n-1 items and W weight (excluding nth item).
# Value of nth item plus maximum value obtained by n-1 items and W minus the weight of the nth item (including nth item).
# --------------------------------------------------------------------------------------
# The time complexity of this naive recursive solution is exponential (2^n).
# Therefore we will apply DP and memoize it.
# ----------------------------------------------------------------------------------------
# The state will be repr by dp[item][weight], denote maximum value of ‘j-weight’ considering all values from ‘1 to ith’
# TIME : 0(N * W), SPACE : 0(N * W)

def compute_max_value(val, wt, W, n):

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            if i == 0 and j == 0:
                dp[i][j] = 0

            elif j >= wt[i - 1]:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]

if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W, n = 50, len(val)
    print(compute_max_value(val, wt, W, n))
