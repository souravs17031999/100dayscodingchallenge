# Program to find smallest pair of differences or that pair whose sum is closest to given X.
# CASE 1 : ARRAYS ARE SORTED
# Input:  ar1[] = {1, 4, 5, 7};
#         ar2[] = {10, 20, 30, 40};
#         x = 32
# Output:  1 and 30
#
# Input:  ar1[] = {1, 4, 5, 7};
#         ar2[] = {10, 20, 30, 40};
#         x = 50
# Output:  7 and 40
# ---------------------------------------------------------------------------------------------

arr1 : [1, 4, 5, 7]
arr2 : [10, 20, 30, 40]

x = 32,

diff = INT_MAX
|1 + 10 - 32| = 21, diff = 21
|1 + 20 - 32| = 11, diff = 11
|1 + 30 - 32| = 1, diff = 1
|1.....40|, |4..10...40|, |5...|
0(M*N), 0(1)
# ------------------------------------------------------------------------------------------------
sorted ?

[1, 4, 5, 7, 10, 20, 30, 40]
0(N + M), 0(M + N)
# ------------------------------------------------------------------------------------------------

We actually don't want to merge the sorted arrays but rather simulate them using left pointer from first array left end,
and right pointer from second array right end.
Now, same loop and same conditions which was for one sorted array closest sum, but just the while loop conditions will be changed,,

l, r => pointers to both arrays from left end and right end repsectively

while l < m and r >= 0:
    rest same.

TIME : 0(N + M), 0(1)

# CASE 2 : UNSORTED ARRAYS

# Input : A[] = {l, 3, 15, 11, 2}
#         B[] = {23, 127, 235, 19, 8}
# Output : 3
# That is, the pair (11, 8)
#
# Input : A[] = {l0, 5, 40}
#         B[] = {50, 90, 80}
# Output : 10
# That is, the pair (40, 50)
# ------------------------------------------------------------------------------------------
Logic is to first sort the array and apply the same logic as explained above.
TIME : 0(M*log(M) + N*log(N))

M, N => LENGTHS OF TWO ARRAYS 
