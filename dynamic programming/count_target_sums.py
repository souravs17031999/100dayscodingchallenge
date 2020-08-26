# Program for computing the count of all such possible assignments of "+" or "-" operators infront of every element
# such that evaluation leads to target sum.
# EX.
# [1, 1, 2, 3], target_sum = 1
# [+, -, -, +] => 1 (one such possible assignment)
# basically, this problem is based on one of the main observation is that if we think in terms of sets partition :
#
#             [1, 1, 2, 3]
#                 /  \
#           [+1, +3]  [-1, -2]
#             [4] - [3] => 1
#
# Now, we can think of this problem the same way as we thought of the count of subset sum difference problem,
# as the problem will be now reduced to that problem.
# Now, this problem is simply exactly the same as count of subset diff problem where input for difference is now the given evaluation value (here =1)
