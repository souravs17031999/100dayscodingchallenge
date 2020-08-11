# Program to compute the largest size of square matrix filled with ones and zeros.
# -----------------------------------------------------------------------------------
# 0 1 1 0 1
# 1 1 0 1 0
# 0 (1 1 1) 0
# 1 (1 1 1) 0
# 1 (1 1 1) 1
# 0 0 0 0 0

# Above largest submatrix size is 3 filled with all "1".
# -------------------------------------------------------------------------------------
# So, Naive solution would be to start at every "1" by traversing all the cells of the matrix, and call
# DFS for right, down and right diagonal and get the minimum possible length so that it should cover all
# way up, to the left and to the left diagonal back to where we started as this is a square matrix.
# But this will be too inefficient.
# ---------------------------------------------------------------------------------------
# So, we think carefully that if we get small sub matrix containing all 1's and let's say for now it's the max
# and now, we check if all of its boundaries starting from bottom right adjacent corner to the up and left,
# are all ones' then we are sure we can increase this size from existing some (2 x 2) to (3 x 3) for ex.
# Now, we can extend this to find the overall max size of all filled with 1's.
# This shows optimal substructure property and now we can also see overlapping problems because wheneevr
# we solve for any cell, we check for its adjacent and related boundaries which are recomputed again and again for any other cell.
# Thus, we can cache it and used the already precomputed values inorder to next time get the max value for matrix.
# -----------------------------------------------------------------------------------------
# Below bottom up DP table shows how to do it, considering dp state as , dp[i][j], i, j are indices of matrices ending at the position
#
# 0  1  1  0  1
# 1  1  0  1  0
# 0  1  1  1  0
# 1  1  2  2  0
# 1  2  2  3  1
# 0  0  0  0  0
# Here, max value is 3 which we can keep updating while filling in the values.
# So, now recurrence relations (transition function) :
# If M[i][j] is 1
#     dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
# else:
#    dp[i][j] = 0
# also keep maintaing max value while updating the values.
# ----------------------------------------------------------------------------
# TIME : 0(N * N)

# Python3 code for Maximum size
# square sub-matrix with all 1s

def printMaxSubSquare(M):
    R = len(M) # no. of rows in M[][]
    C = len(M[0]) # no. of columns in M[][]

    dp = [[0 for k in range(C)] for l in range(R)]
    # here we have set the first row and column of S[][]
    max_value = 0
    # Construct other entries
    for i in range(1, R):
    	for j in range(1, C):
    		if M[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_value = max(max_value, dp[i][j])
            else:
                dp[i][j] = 0

    return dp


# Driver Program
M = [[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]]

print(printMaxSubSquare(M))

# This code is contributed by Soumen Ghosh
