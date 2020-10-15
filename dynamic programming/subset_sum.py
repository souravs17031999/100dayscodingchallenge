# Program to check if there is any possible solution or any possible subset for a given sum.
# ------------------------------------------------------------------------------------------
# Recursion tree will be same as like knapsack or coin change , at every possible element, we have two choice
# either we can take it or not take it.
# We can draw and verify recursion tree has overlapping subproblems.
# ALso naive recursive method is too inefficient and time is exponential.
# -------------------------------------------------------------------------------------------
# So, we write DP solution for it.
# -------------------------------------------------------------------------------------------
# Values are filled very similarly to the knapsack problem.
# at eevry point, we ask if we can inlucde the value or not, if we go up, then we don't include the item
# if we wanna include the item, then we should go up and move difference of (j - s[i]) number os steps backward
# and get the value from there.
# Since, we just have to return True/False, we maintain dp[value][sum], which is a boolean matrix.
# --------------------------------------------------------------------------------------------------
# TIME : 0(SUM * N), SPACE : 0(SUM * N)

# A Dynamic Programming solution for subset
# sum problem Returns true if there is a subset of
# set[] with sun equal to given sum

# Returns true if there is a subset of set[]
# with sun equal to given sum
def isSubsetSum(set, n, sum):

	# The value of subset[i][j] will be
	# true if there is a
	# subset of set[0..j-1] with sum equal to i
	subset =([[False for i in range(sum + 1)]
			for i in range(n + 1)])

	# If sum is 0, then answer is true
	for i in range(n + 1):
		subset[i][0] = True

	# If sum is not 0 and set is empty,
	# then answer is false
	for i in range(1, sum + 1):
		subset[0][i]= False

	# Fill the subset table in botton up manner
	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if j<set[i-1]:
				subset[i][j] = subset[i-1][j]
			if j>= set[i-1]:
				# NOTE : OR IS USED BECAUSE MAX DOESN'T MAKE SENSE FOR BOOLEAN VALUES, SO OR USED 
				subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]])

	# uncomment this code to print table
	# for i in range(n + 1):
	# for j in range(sum + 1):
	# print (subset[i][j], end =" ")
	# print()
	return subset[n][sum]

# Driver program to test above function
if __name__=='__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")


