# Program for getting the most profit by buying and selling stocks given in the form of input array.
# Note1 : Multiple transactions can be made
# Note2 : Only one transaction can be made on one day.
# Note3 : Before buying any stock, we need to sell previous stock.
# -----------------------------------------------------------------------------------------------------
# Third constraint is very simple as it is obvious trivial.
# Now, second and first one is important as we will se in a moment.
# -------------------------------------------------------------------------------------------------------
# EX. [7,1,5,3,6,4], MAXPROFIT : 7
# Naive way would be to simply generate all possible sets of buying and selling stocks at each ith day, and
# get the max profit by comparing these buy and sell stock values each time.
# Since, this is an optimization problem and a choice is given, we can do exhaustive search.
# we can see we can apply recursive approach to solve this, in the following way :
# # class Solution {
#     public int maxProfit(int[] prices) {
#         return calculate(prices, 0);
#     }
#
#     public int calculate(int prices[], int s) {
#         if (s >= prices.length)   # this tells us we reached dead end of array, so we need to return.
#             return 0;
#         int max = 0;
#         for (int start = s; start < prices.length; start++) {    # starting by taking var of outer loop as a buying time
#             int maxprofit = 0;
#             for (int i = start + 1; i < prices.length; i++) {   # finding the best time to sell
#                 if (prices[start] < prices[i]) {                # so, if start < i, that means, this is best time to sell as of now., so update our calculation
#                     int profit = calculate(prices, i + 1) + prices[i] - prices[start];     # here, we retreive recursion stack value and compute the diff of (S.P. - C.P.)
#                     if (profit > maxprofit)    # we update profit for this particular case
#                         maxprofit = profit;
#                 }
#             }
#             if (maxprofit > max)   # we update global profit in this case
#                 max = maxprofit;
#         }
#         return max;   # we return global profit
#     }
# }
#
# This is too inefficnet, as time complexity : 0(N^N), Space : 0(N).
# ---------------------------------------------------------------------------------------------------
# Actually, we can do much better than brute force, by simply visualizing it clearly on a graph by plotting these points.
#
#
#
#  7            *
#  6             *              #
#  5              *       #    * *
#  4               *     * *  *   *
#  3                *   *   #
#  2                 * *
#  1                  #
#  0
#
# If we observe clearly, then we can see lowest points (local minima) is the best time to buy the stocks, and the highest points (local maxima) are the best points to sell.
# These points are pointed by "#".
# So, we are actually interested in getting the sigma(difference of (peak(i)) - difference of valley(i))
# If we sum all these slopes difference, then we are able to find the max. profit.
# TIME : 0 (N), SPACE : 0(1).
# ---------------------------------------------------------------------------------------------------------
# There is actually a much cleaner way to acheive the above thing with same asymtodic bounds,
# the key is to not actually compute all the local minima and local maxima, and skip those which are not useful for us.
# So, if the stocks are increasing, keep adding them, and if decrease, then skip them.
# ----------------------------------------------------------------------------------------------------------
# class Solution {
#     public int maxProfit(int[] prices) {
#         return calculate(prices, 0);
#     }
#
#     public int calculate(int prices[], int s) {
#         if (s >= prices.length)
#             return 0;
#         int max = 0;
#         for (int start = s; start < prices.length; start++) {
#             int maxprofit = 0;
#             for (int i = start + 1; i < prices.length; i++) {
#                 if (prices[start] < prices[i]) {
#                     int profit = calculate(prices, i + 1) + prices[i] - prices[start];
#                     if (profit > maxprofit)
#                         maxprofit = profit;
#                 }
#             }
#             if (maxprofit > max)
#                 max = maxprofit;
#         }
#         return max;
#     }
# }
# CODE IS SHOWN FOR THIRD APPROACH (SIMILAR TO SECOND ONE BUT MORE CLEANER AND CONCISE WAY) :

def compute_max_profit(arr):
    n = len(arr)
    max_profit = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            max_profit += arr[i] - arr[i - 1]

    return max_profit

if __name__ == '__main__':
    assert compute_max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert compute_max_profit([1,2,3,4,5]) == 4
    assert compute_max_profit([7,6,4,3,1]) == 0            
