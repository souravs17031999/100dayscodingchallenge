# IMPORTANT POINTS FOR INTERVIEW FOR APPROACHING DP (MOSTLY IN BOTTOM UP TABULATION MANNER) :   
## Typically, all the problems that require to maximize or minimize certain quantity or counting problems that say to   
## count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.   
## DP is nothing but simply usage of Caching.   
# Used when problem contains :   
## * optimization of some quantity (generally having some cost)  
## * some choice or selection   
## Write the topdown recursive approach and convert to bottom up for avoiding stack overflow or direclty write the bottom up manner .
## * Firstly, always think about after what is the state after few no. of steps in the problem ?  
## * How can we now represent those states ? We need to understand about the dimensions of array/matrix.   
## What are the important variables we need to keep about at that state ? if it is just one thing we care about, we can maintain  
## in 1-d array, if its two thing (like position in a grid), then 2-d array, if more than that, then more n-d type arrays.  
## So, it depends on what information is useful/important at a particular state.  
# Resources :    
##  https://leetcode.com/discuss/interview-question/778035/dynamic-programming-patterns     
## https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns