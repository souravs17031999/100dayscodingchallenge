# Program to compute longest common substring in the given two strings.
# "GeeksforGeeks", "GeeksQuiz" => "5" (Geeks)
# ------------------------------------------------------------------------------
# Naive solution would be to generate all the substrings for string1, and then for string2, now compare if the substrings generated in 1 is also in
# second one and get the longest one.
# That would take 0(M^2*N^2), M, N are lenght of both strings (generating all substrings would be done in N^2, if N is lenght of string)
# -------------------------------------------------------------------------------
# Optimal substructure property and overlapping subsproblmes are easy to see as they are same as in LCS DP problem.
# So, now we have to define the recurrence to fill out the dp table in bottom up manner.
# ----------------------------------------------------------------------------------
# So, we start off with two pointers pointing to first chars of both substrig ,
# state of dp[i][j],
# Now, if both char are same, then dp[i][j] = 1 + lcs(dp[i - 1][j - 1]), now dp[i - 1][j - 1] state represents
# basically last already matched part of the string cached on that location (i - 1, j - 1).
# Like,
# "GeeksforGeeks"
#    _
# "GeeksQuiz"
#    _
# Let's say we got a match for "e" and "e", so we take this by adding 1 to the already matched last substring for "Ge" in first string
# and "Ge" in second string which would be 2, and so at index 3, now it would be 1 + 2 => 3, which is evident "Gee" matched so far.
# In other cases, where they don;t match we simply put dp[i][j] = 0 because either it would be not part of longest substring or position would be
# different (maybe it is shifted either front or back).
# We have to also construc the matrix one extra lenght for considering emtpy string (base case) in which case, dp[i][j] = 0.
# TIME : 0(M * N)
# -----------------------------------------------------------------------------------
# NOTE : Also here answer will not be in last cell, as maybe last char is not equal, so we will put 0 there but it doesn't means that there is no
# substring which is matching, hence , we need to also keep updating the max length while updating the values when chars match.
# -----------------------------------------------------------------------------------

# Python3 implementation of Finding
# Length of Longest Common Substring

# Returns length of longest common
# substring of X[0..m-1] and Y[0..n-1]
def LCSubStr(X, Y, m, n):

	# Create a table to store lengths of
	# longest common suffixes of substrings.
	# Note that LCSuff[i][j] contains the
	# length of longest common suffix of
	# X[0...i-1] and Y[0...j-1]. The first
	# row and first column entries have no
	# logical meaning, they are used only
	# for simplicity of the program.

	# LCSuff is the table with zero
	# value initially in each cell
	dp = [[0 for k in range(n+1)] for l in range(m+1)]

	# To store the length of
	# longest common substring
	result = 0

	# Following steps to build
	# LCSuff[m+1][n+1] in bottom up fashion
	for i in range(m + 1):
		for j in range(n + 1):
			if (i == 0 or j == 0):
				dp[i][j] = 0
			elif (X[i-1] == Y[j-1]):
				dp[i][j] = dp[i-1][j-1] + 1
				result = max(result, dp[i][j])
			else:
				dp[i][j] = 0
	return result

# Driver Program to test above function
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
					LCSubStr(X, Y, m, n))
