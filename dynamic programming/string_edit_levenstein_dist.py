# Program to compute minimum Levenshtein distance (edit distance) between the two stings.
# So, basically we want to compute the minimum number of operations required to transform a given string A to B.
# Recursion tree is similar to LCS, and explanation for why DP is also same.
# ------------------------------------------------------------------------------------------
# State of dp[i][j], where i, j points to last char to both strings.
# -------------------------------------------------------------------------------------------
# so, we also need to take more than one length extra for considering one extra empty string.
# So, if any of the pointer moves to empty string, we can return (or fill) length of traversed chars till now
# as the other one is empty, so we will need to either append or delete that many times as many times the length
# of chars are in one of the non empty string.
# Let's say "", "bana" => so, 4 will be answer (either append or delete)
# -----------------------------------------------------------------------------------------------
# In the matrix, if we consider value just above one  => insert operation
# just left one : delete operation
# replace operation : upper left diagonal
# We need to take min of these, so that our overall operations are minimized.
# ---------------------------------------------------------------------------------------------------

# if S1[i] == s2[j], then
#     dp[i][j] = dp[i - 1][j - 1]
# else:
#     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
# --------------------------------------------------------------------------------------------------------
# NOTE : We can optimize more in terms of space by using two vectors (lists) of size m, n.
# EXPLANATION OF DETAILED RECURSION CALLS TREE :
#                                               (3, 3)
#                                        /                     \
#                                                  |
#                                (2, 3)           (3, 2)            (2, 2)
#                           /     |       \         ...               / | \
#                    (1, 3)      (2, 2)    (1, 2)                  (1, 2) (2, 1) (1, 1)
#                   /  | \          ..       ...   /  |  \          ...     ...    ...
#             (0, 3) (1,2) (0,2)              (2, 2) (3, 1) (2, 1)
#                    / | \                       ...   ..  ...    
#                (0,2) (1,1) (0,1)
#                      / | \
#                  (0,1) (1,0) (0,0)
#
# -----------------------------------------------------------------------------------------------------------------

# Simple recursion :
def string_edit(s1, s2, n1, n2):
    
    if n1 == 0:
        return n2
    
    if n2 == 0:
        return n1
    
    if s1[n1 - 1] == s2[n2 - 1]:
        return string_edit(s1, s2, n1 - 1, n2 - 1)
    
    else:
        return 1 + min(string_edit(s1, s2, n1 - 1, n2 - 1), \
                       min(string_edit(s1, s2, n1 - 1, n2), string_edit(s1, s2, n1, n2 - 1)))

# bottom up DP :

# A Dynamic Programming based Python program for edit
# distance problem
def editDistDP(str1, str2, m, n):
	# Create a table to store results of subproblems
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	# Fill d[][] in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

			# If first string is empty, only option is to
			# insert all characters of second string
			if i == 0:
				dp[i][j] = j # Min. operations = j

			# If second string is empty, only option is to
			# remove all characters of second string
			elif j == 0:
				dp[i][j] = i # Min. operations = i

			# If last characters are same, ignore last char
			# and recur for remaining string
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			# If last character are different, consider all
			# possibilities and find minimum
			else:
				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
								dp[i-1][j],	 # Remove
								dp[i-1][j-1]) # Replace

	return dp[m][n]

# Driver program
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))
