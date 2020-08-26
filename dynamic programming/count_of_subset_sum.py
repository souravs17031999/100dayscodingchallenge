# Program for count of subsets with given sum in the input.
# We have already seen how to check whether given subset has that sum or not but not we need to count those subsets.
# Again, naive solution would be same as by generating all the subsets and then checking if the sum matched the given sum, it would be counted or not.
# generating the subsets itself would take expoenential time , hence not efficient for larger values of sum and subset size.
# Next, we think in terms of DP and related to subset problems / knapsack problem.
# ----------------------------------------------------------------------------------------------------
# This is very similar to the subset sum problem, and here think about base cases.
# So, if we represent dp state as dp[i][j] then, it means count of subsets taken from arr[1...i] such that their sum is J.
# if in this way, we build up all the states, then we will be able to compute the count of all subsets such that their sum is S (given sum) in the last
# cell of the table.
# recirsive relation will be same in place of OR in subset sum, now it will be +, because we have to count for all possible subsets, whether we include
# it or not include it.
# ------------------------------------------------------------------------------------------------------
def count_subset_sum(set, n, sum):


    subset =([[0 for i in range(sum + 1)]
    		for i in range(n + 1)])

    # If sum is 0, then answer is 1
    for i in range(n + 1):
    	subset[i][0] = 1

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
    	subset[0][i]= 0

    # Fill the subset table in botton up manner
    for i in range(1, n + 1):
    	for j in range(1, sum + 1):
            if set[i-1] <= j:
            	subset[i][j] = subset[i-1][j] + subset[i - 1][j-set[i-1]]
            else:
                subset[i][j] = subset[i-1][j]

    print(subset[n][sum])

count_subset_sum([1, 2, 3, 3], 4, 6)
#All the possible subsets are {1, 2, 3}, {1, 2, 3} and {3, 3}
