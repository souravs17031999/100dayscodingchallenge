# Program to compute maximum sum of increasing subsequence.
# This is very similar and a variation for Longest increasing subsequence (lis) problem as we need increasing subsequence
# but just a slight difference is that instead of length, we need the sum.
# so, just the criteria will be changed and filling of table will remain same.
# --------------------------------------------------------------------------------------------------------------
# TIME : 0(N^2)

# Dynamic Programming bsed Python
# implementation of Maximum Sum
# Increasing Subsequence (MSIS)
# problem

# maxSumIS() returns the maximum
# sum of increasing subsequence
# in arr[] of size n
def maxSumIS(arr, n):
	res = 0
	msis = [0 for x in range(n)]

	# Initialize msis values
	# for all indexes
	for i in range(n):
		msis[i] = arr[i]

	# Compute maximum sum
	# values in bottom up manner
	for i in range(1, n):
		for j in range(i):
			if (arr[i] > arr[j]):
				msis[i] = max(msis[i], msis[j] + arr[i])

	# Pick maximum of
	# all msis values
	for i in range(n):
		if res < msis[i]:
			res = msis[i]

	return res

# Driver Code
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing " +
					"subsequence is " +
				str(maxSumIS(arr, n)))
