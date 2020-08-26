# IMPORTANT POINTS FOR INTERVIEW FOR APPROACHING DP (MOSTLY IN BOTTOM UP TABULATION MANNER) :   
## Typically, all the problems that require to maximize or minimize certain quantity or counting problems that say to   
## count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.   
## DP is nothing but simply usage of Caching.   
# Used when problem contains :   
## * optimization of some quantity (generally having some cost)  
## * some choice or selection   
## Write the topdown recursive approach and convert to bottom up for avoiding stack overflow or directly write the bottom up manner .
# For topdown or simple recursion :
## * Think in terms of recursive relations, how we can breakdown problems into subproblems and that too identify overlapping subproblems.
## * Then, identify optimal subtructure, that is at every point ask what problem we are solving, and if that all subproblems lead us to overall solution.
## * when writing recursion, think about base cases : think when we would have smallest valid input what would we return ? Because eventually problems
## will broken down to converge to base cases.
# For bottom up TABULATION :   
## * Firstly, always think about after what is the state after few no. of steps in the problem ?  
## * How can we now represent those states ? We need to understand about the dimensions of array/matrix.   
## What are the important variables we need to keep about at that state ? if it is just one thing we care about, we can maintain                        in 1-d array, if its two thing (like position in a grid), then 2-d array, if more than that, then more n-d type arrays.  
## So, it depends on what information is useful/important at a particular state.  
# Resources :    
##  https://leetcode.com/discuss/interview-question/778035/dynamic-programming-patterns     
## https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns
# Identification of problem :
### Relating to knapsack problem :
### if there are some items given to us and we have choice to either include it or not include it ? Also we have some constraints in form of some value   like bag in knapsack or some another value that we have to fill up to or add up to ?
