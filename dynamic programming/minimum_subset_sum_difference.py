# Program for computing the minimum difference of two partitions of the subsets of the given array.
# EX.
# arr[] = {1, 6, 11, 5}
# Subset1 = {1, 5, 6}, sum of Subset1 = 12
# Subset2 = {11}, sum of Subset2 = 11
# ---------------------------------------------------------------------------------------------------
# We have already seen this problem in equal sum parition problem which eventually was dependent on subset sum problem.
# The recursive approach is to generate all possible sums from all the values of array and to check which solution is the most optimal one.
# To generate sums we either include the i’th item in set 1 or don’t include, i.e., include in set 2, and this is exponential time complexity.
# Let's think in terms of DP.
# Now, if we observe carefully,
#         S (total subset)
#       /  \
#      s1   s2
# initially, we observe that we have two partitions, s1, and s2 and we need to minimize it but if we think that we already know the value of the sum
# of the array, and hence can calculate the value of second parition sum, if we know the first parition sum, so now the problem will be little simpler
# and we just now have 1 variable and we need to only minimize (sum(arr) - 2*s1), where s1 is sum of first partition.
# Min(sum - 2 * s1)
# Now, also we don't exactly what s1 will be, but we will try to estimate the value of s1, and for that we can think in terms of number line,
# firstly our search space will be containing all the values from 0......Sum, because s1 can be any of them, but since we already saw that we need not
# search for complete search space, and we can only search for half of search space that is sum//2 as the comlementary value will be always there.
# and so, we can now narrow down our search to the problem that for the numbers 0.......sum//2, if there exists the value which is the s1, and
# then we compute s2 by using sum - s1, and get the minimum for all possible values from 0.....sum//2.
# ----------------------------------------------------------------------------------------------------------
# Now, we can get the table of the subset sum problem passing the sum of array and the array as subset as the input.
# Then, the last row is the actual number line or the search space that we are observing here, 0.....N, if there is any value(s) that will sumupto
# the given sum.
# Hence, by doing this, there will be some number which is possible and there are some numbers which are not possible.
# so, we can simply get all those for which it is possible and compute the complementary sum, and then update the minimum and return the overall minsum.
# -----------------------------------------------------------------------------------------------------------
# TIME : 0(N * SUM)

# computing the table for subset sum
def isSubsetSum(set, n, sum):

    subset =([[False for i in range(sum + 1)]
    		for i in range(n + 1)])

    for i in range(n + 1):
    	subset[i][0] = True

    for i in range(1, sum + 1):
    	subset[0][i]= False

    for i in range(1, n + 1):
    	for j in range(1, sum + 1):
    		if j<set[i-1]:
    			subset[i][j] = subset[i-1][j]
    		if j>= set[i-1]:
    			subset[i][j] = (subset[i-1][j] or
    							subset[i - 1][j-set[i-1]])

    return subset

import sys
def compute_min_subset_diff(arr):

    n = len(arr)
    sum_range = sum(arr)
    subset = isSubsetSum(arr, n, sum_range) # we can actually, get it done in dp[n][sum_range//2]
    min_diff = sys.maxsize
    for i in range(sum_range//2, -1, -1):
        if subset[n][i] == True:
            min_diff = min(min_diff, sum_range - 2 * i)

    return min_diff

if __name__ == '__main__':
    arr = [1, 6, 11, 5]
    print(compute_min_subset_diff(arr))
