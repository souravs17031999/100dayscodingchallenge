# Program for unbounded knapsack problem.
# In unbounded knapsack, it is allowed to take same item more than once, that is multiple occurences of same type is allowed.
# That means, once we take that item, then again we have option of taking that same item.
# EX. W = 100
# val[]  = {1, 30}
# wt[] = {1, 50}
# OUTPUT : 100, There are many ways to fill knapsack.
# 1) 2 instances of 50 unit weight item.
# 2) 100 instances of 1 unit weight item.
# 3) 1 instance of 50 unit weight item and 50
#    instances of 1 unit weight items.
# We get maximum value with option 2.
# Input : W = 8
#        val[] = {10, 40, 50, 70}
#        wt[]  = {1, 3, 4, 5}
# Output : 110
# We get maximum value with one unit of
# weight 5 and one unit of weight 3.
# -------------------------------------------------------------------------------------------

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

W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)

print(compute_max_value(val, wt, W, n))

# ------------------------------------------------------------------------------------------
# we can optimize it more for space complexity.
# Just using 1-d array as now only 1 d state information is required, because we just want to know what is the max value obtained for weight i,
# in dp[i], and we don't really need to know which item is actually included or not (which was important for classical knapsack).


# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.

# Returns the maximum value
# with knapsack of W capacity
def unboundedKnapsack(W, n, val, wt):

	# dp[i] is going to store maximum
	# value with knapsack capacity i.
	dp = [0 for i in range(W + 1)]

	ans = 0

	# Fill dp[] using above recursive formula
	for i in range(W + 1):
		for j in range(n):
			if (wt[j] <= i):
				dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

	return dp[W]

# Driver program
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)

print(unboundedKnapsack(W, n, val, wt))
