# Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
# -------------------------------------------------------------------------------------------
# (ABC)D = (AB)(CD) = A(BCD) = ....
# (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
# A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
# -------------------------------------------------------------------------------------------
# Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
# return the minimum number of multiplications needed to multiply the chain.
# ---------------------------------------------------------------------------------------------
# Naive Algorithm will be to compute and partition at every single point possible, and then recursively call for remaining matrix products.
# Following the recursion tree, it will be clear that there are overlapping subproblems,
# For example, if the given chain is of 4 matrices. let the chain be ABCD, then there are 3 ways to place first set of parenthesis
# outer side: (A)(BCD), (AB)(CD) and (ABC)(D). So when we place a set of parenthesis, we divide the problem into subproblems of smaller size.
# ------------------------------------------------------------------------------------------------
#
#                                     1...4
#                                   /  | |  \  \
#                                  1.1 | 1.2  3.4  4.4
#                                  __  2.4  |     /\  __
#                                     |  | \  3.3 3.4
#                                    4.4 1.1 2.2
#                                    __  __
# Therefore simply recursion will be taking exponential time, hence we apply topdown/bottom up DP.
# Here, we show bottom up DP.
# -------------------------------------------------------------------------------------------------
# state of dp, dp[i][j], i, j represents matrix starting from index i till j products
# ------------------------------------------------------------------------------------------------

# Follwing is one of the implementation in 0(N^3)

# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
# import sys
#
# # Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
# def MatrixChainOrder(p, n):
# 	# For simplicity of the program, one extra row and one
# 	# extra column are allocated in m[][]. 0th row and 0th
# 	# column of m[][] are not used
# 	m = [[0 for x in range(n)] for x in range(n)]
#
# 	# m[i,j] = Minimum number of scalar multiplications needed
# 	# to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
# 	# dimension of A[i] is p[i-1] x p[i]
#
# 	# cost is zero when multiplying one matrix.
# 	for i in range(1, n):
# 		m[i][i] = 0
#
# 	# L is chain length.
# 	for L in range(2, n):
# 		for i in range(1, n-L+1):
# 			j = i+L-1
# 			m[i][j] = sys.maxint
# 			for k in range(i, j):
#
# 				# q = cost/scalar multiplications
# 				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
# 				if q < m[i][j]:
# 					m[i][j] = q
#
# 	return m[1][n-1]
#
# # Driver program to test above function
# arr = [1, 2, 3 ,4]
# size = len(arr)
#
# print("Minimum number of multiplications is " +
# 	str(MatrixChainOrder(arr, size)))

# OPTIMIZED CODE IN 0(N * N)
# Python3 program to implement optimized
# matrix chain multiplication problem.

# Matrix Mi has dimension
# p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):

	# For simplicity of the program, one
	# extra row and one extra column are
	# allocated in dp[][]. 0th row and
	# 0th column of dp[][] are not used
	dp = [[0 for i in range(n)]
			for i in range(n)]

	# dp[i, j] = Minimum number of scalar
	# multiplications needed to compute
	# the matrix M[i]M[i+1]...M[j] = M[i..j]
	# where dimension of M[i] is p[i-1] x p[i]

	# cost is zero when multiplying one matrix.
	for i in range(1, n):
		dp[i][i] = 0

	# Simply following above recursive formula.
	for L in range(1, n - 1):
		for i in range(n - L):
			dp[i][i + L] = min(dp[i + 1][i + L] +
								p[i - 1] * p[i] * p[i + L],
							dp[i][i + L - 1] +
								p[i - 1] * p[i + L - 1] * p[i + L])

	return dp[1][n - 1]

# Driver code
arr = [10, 20, 30, 40, 30]
size = len(arr)
print("Minimum number of multiplications is",
				MatrixChainOrder(arr, size))

# This code is contributed
# by sahishelangia
