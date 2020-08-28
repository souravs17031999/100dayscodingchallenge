# We have to paint n boards of length {A1, A2…An}. There are k painters available and # each takes 1 unit time to paint 1 unit of board. The problem is to find the minimum # time to get this job done under the constraints that any painter will only paint
# continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but # not board {2, 4, 5}.
# -----------------------------------------------------------------------------------
# Given an array A of non-negative integers and a positive integer k, we have to
# divide A into k of fewer partitions such that the maximum sum of the elements in a # partition, overall partitions is minimized.
# -----------------------------------------------------------------------------------
# A brute force solution is to consider all possible set of contiguous partitions and
# calculate the maximum sum partition in each case and return the minimum of all #
# these cases.
# That would take exponential time.
# -----------------------------------------------------------------------------------
# Now, we need to optimize using DP.
# Let's see optimal substructure and overlapping subproblems.
#         T(4, 3)
#      /    /    \ ..
# T(1, 2)  T(2, 2) T(3, 2)
#           /..      /..
#       T(1, 1)    T(1, 1)
#
# T(n, k) = min(max(T(i, k - 1), sigma(A(j))))
# Base case : T(1, k) = A1
# T(n, 1) : sigma(A(i))
# --------------------------------------------------------------------
# Overalpping subproblems :
#
#   10 | 40 | 20 | 30 | 40 | 50
#   10 | 40 | 20 30 | 40 | 50
#
# -------------------------------------------------------------------------
# state of dp[painter][painting]
# -------------------------------------------------------------------------
#
# so, each state of dp[i][j] represents i painters, and j paintings (j elements of array )
# and we have to try all possible partitions and get the max for all the possible paritions.
# and then fill in the min of all those max calculated values.
# This will be the optimal value.
# ---------------------------------------------------------------------------
# TIME : 0(K * N^3), Now, if we preompute the cumulatove sum into a separate array and sum can be done in 0(1) time.
# So, it will be brought down in 0(K * N^2)

# A DP based Python3 program for
# painter's partition problem

# function to calculate sum between
# two indices in list
def sum(arr, start, to):
	total = 0
	for i in range(start, to + 1):
		total += arr[i]
	return total

# bottom up tabular dp
def findMax(arr, n, k):

	# initialize table
	dp = [[0 for i in range(n + 1)]
			for j in range(k + 1)]

	# base cases
	# k=1
	for i in range(1, n + 1):
		dp[1][i] = sum(arr, 0, i - 1)

	# n=1
	for i in range(1, k + 1):
		dp[i][1] = arr[0]

	# 2 to k partitions
	for i in range(2, k + 1): # 2 to n boards
		for j in range(2, n + 1):

			# track minimum
			best = 100000000

			# i-1 th separator before position arr[p=1..j]
			for p in range(1, j + 1):
				best = min(best, max(dp[i - 1][p],
								sum(arr, p, j - 1)))

			dp[i][j] = best

	# required
	return dp[k][n]

# Driver Code
arr = [10, 20, 60, 50, 30, 40]
n = len(arr)
k = 3
print(findMax(arr, n, k))
