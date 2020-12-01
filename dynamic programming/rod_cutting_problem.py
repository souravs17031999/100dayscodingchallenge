# Program for computing maximum value by cutting the rod in given pieces.
# rod cutting problem basically defines the following  :
# We have been given a rod of length L, and a length array containing lengths of different measurements, and price array containing price for
# different segments, and finally, we need to compute the max value / price obtained after cutting the rod of length L by cutting various segments.
# length   | 1   2   3   4   5   6   7   8
# price    | 1   5   8   9  10  17  17  20
# L= 8, output : 22
# length   | 1   2   3   4   5   6   7   8
# price    | 3   5   8   9  10  17  17  20
# Length = 8, output = 24.
# -------------------------------------------------------------------------------------------------
# If we observe carefully, then it matches knapsack problem and it exactly matches with Unbounded knapsack problem as here we can cut the
# rod into segments of same type more than once.
# Since, let's say if we have rod of length = 4m, then we can say rod of length 2 + 2, and we can also go for 1 + 1 + 2 and so on....
# Now, the code is completely same with knapsack problem.
# Weight array is matched with  : length array
# profit array is matched with  : price array
# W is matched with : N.
# ------------------------------------------------------------------------------------------------

#
# cR() ---> cutRod()
#
#                              cR(4)
#                   /        /
#                  /        /
#              cR(3)       cR(2)     cR(1)   cR(0)
#             /  |         /         |
#            /   |        /          |
#       cR(2) cR(1) cR(0) cR(1) cR(0) cR(0)
#      /        |          |
#     /         |          |
#   cR(1) cR(0) cR(0)      cR(0)
#    /
#  /
# CR(0)
#
#
# WE CAN VISUALIZE WHAT SUBPROBLEMS WE ARE SOLVING AND HOW OPTIMAL SUBTRUCTURE WILL HELP US IN FINDING OVERALL SOLUTION : 
#  
#                     SEGMENT: 0 1 2 3 4  5  6  7  8     
# LET'S SAY PRICE/PROFIT ARR :   1 5 8 9 10 17 17 20 
# 
# SO, LIKE AT EVERY POINT, STARTING FROM 0TH INDEX OF 0 LENGTH OF ROD : CAN WE DO ANYTHING NO, SO, FOR 0 LENGTH , IT'S OVERALL PROFIT IS 0
# NOW, FOR 
#               /   1 [1]
#             L           => MAX(1, 0) => 1
#               \   0 
#
# SIMILARLY, FOR L = 2
#                             1 + 1   [2] 
#                          /                => MAX(2, 5) = 5   , NOW HERE WHEN WE CHECK FOR BEST COST OF CUTTING ROD OF L = 1, THEN WE ALREADY SAVE THE BEST OPTIMUM = 1 THERE 
#                        L   ---  2 [5]
#
#
# SIMILARLY, FOR L = 3, 
#
#
#                                  3 [8]
#                               /  
#                            3  ----  1 [1] + 2 [5] => MAX(8, 6, 6) => 8 , AND ALSO HERE WHEN WE WANT TO KNOW THE OPTIMUM FOR SMALLER ROD LENGTHS, WE DONOT WANT TO COMPUTE IT AGAIN, 
#                                                                          BUT RATHER WE SAVED IT
#                               \   
#                                   2 [5] + 1 [1]
#
# SIMILARLY, L = 4, 
#
#
#
#                                        3[8] + 1[1]  
#
#                                              4 [9]      
#                                          |  /
#                                      L = 4 ----- 1[1] + 3[8]  =>  MAX(9, 9, 9, 10) => 10 AND SAME HERE CASE WITH RECOMPUTION, WE HAVE ALREADY SAVED BEST OPTIMUM FOR SMALLER ONES
#                                            \ 
#                                                2[5] + 2[5]
#
#                                          
#
# SIMILALRY, WE CAN GO FOR MORE LENGTHS OF ROD SEGMENTS AND SEE HOW WE ARE AVOIDING RECOMPUTATION OF SMALLER SUBPROBLEMS AND ALSO HOW SMALLER SUBPROBLEMS ARE LEADING US TO 
# OVERALL OPTIMAL SOLUTION.
#
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def compute_max_value(val, wt, W, n):

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            if i == 0 and j == 0:
                dp[i][j] = 0

            elif j >= wt[i - 1]:
                dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j]) # just one line optimized

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]

price = [1, 5, 8, 9, 10, 17, 17, 20]
arr = [i for i in range(1, len(price))]
size = len(arr)

print(compute_max_value(price, arr, 8, size))
