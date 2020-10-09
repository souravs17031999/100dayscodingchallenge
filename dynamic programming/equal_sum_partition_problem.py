# Program for checking whether a partition can be made like breaking the array into two sets such that
# the both sets contains equal sums.
# EX. arr[] = {1, 5, 11, 5}, True : {1, 5, 5} {11}
# arr[] = {1, 5, 3} : False
# -------------------------------------------------------------------------------------------------------
# One of the key things is to observe that partition can be only made if the sum of the array numbers are even
# as we can see any odd number can't be divided into equal partition but a even number can be !
# Next thing to observe is that since, both subsets have equal sum, hence we need not compute the partition for both
# sets, only one set is required, other is same (as stated by question).
# So, the only thing now remains is check whether S/2 sum is possible for the given subset and this problem has been already
# solved in the subset sum problem (just the sum parameter is different).
# Hence, this problem is an extension to subset sum problem.
# --------------------------------------------------------------------------------------------------------------------------------
# CODE IS SIMILAR TO SUBSET SUM PROBLEM , JUST CHECK ADDITIONAL CONSTRAINTS.
#
# Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
# there is a subset of arr[0..n-1] with sum equal to sum/2
#
# The isSubsetSum problem can be divided into two subproblems
# a) isSubsetSum() without considering last element 
#    (reducing n to n-1)
# b) isSubsetSum considering the last element 
#    (reducing sum/2 by arr[n-1] and n to n-1)
# If any of the above the above subproblems return true, then return true. 
# isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) || isSubsetSum (arr, n-1, sum/2 - arr[n-1])
