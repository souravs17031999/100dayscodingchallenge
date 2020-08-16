# Program for computing longest chain of pairs of (a, b).
# Pairs can be formed using (a, b) , (c, d).... if b < c for all the pairs.
# Compute and return the length of longest chain possible using the pairs of above type.
# -------------------------------------------------------------------------------------
# If we think carefully, then this problem is similar to longest increasing subsequence, there also we check,
# if the arr[j] < arr[i], and we take that add it our original count, and call for subproblems.
# ----------------------------------------------------------------------------------------
# Here, also the calls are same, whether a given pair is a part of longest chain or not ?
# So, applying same principle and just one new addition like sorting on the basis of values and then applying DP.
# We also need to sort on the basis of first element of pair, and then similar dp state, dp[length], length is longest
# length till that index.
# --------------------------------------------------------------------------------------
# TIME : 0(N^2),

class Pair(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

# This function assumes that arr[] is sorted in increasing
# order according the first (or smaller) values in pairs.
def maxChainLength(arr, n):

	res = 0

	# Initialize MCL(max chain length) values for all indices
	mcl = [1 for i in range(n)]

	# Compute optimized chain length values in bottom up manner
	for i in range(1, n):
		for j in range(0, i):
			if (arr[i].a > arr[j].b):
				mcl[i] = max(mcl[i], mcl[j] + 1)

	# mcl[i] now stores the maximum
	# chain length ending with pair i

	# Pick maximum of all MCL values
	for i in range(n):
		if (res  < mcl[i]):
			res  = mcl[i]

	return res

# Driver program to test above function
arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]

print('Length of maximum size chain is',
	maxChainLength(arr, len(arr)))
