# program for counting subset sum with given difference as input for the given array (set).
# We need to count all such possible subsets such that difference between the sums is the given difference.
#              S
#             / \
#            S1  S2
# Now, given s1 - s2 = diff  (1)
# also, we know,
# s1 + s2 = sum(arr)  (2)
#
# adding 1 and 2,
# we get, s1 = (diff + sum(arr)) / 2 where, we know diff and sum(arr), so we get s1 (sum of first subset).
# Now, this problem reduces to counting all such subsets which has sum s1 which has already been discussed.
