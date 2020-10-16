# IMPORTANT POINTS FOR INTERVIEW FOR APPROACHING DP (MOSTLY IN BOTTOM UP TABULATION MANNER) :   
## Typically, all the problems that require to maximize or minimize certain quantity or counting problems that say to   
## count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.   
## DP is nothing but simply usage of Caching.   
# Used when problem contains :   
## * optimization of some quantity (generally having some cost)  
## * some choice or selection   
## Write the topdown recursive approach and convert to bottom up for avoiding stack overflow or directly write the bottom up manner .   
# For Topdown or simple recursion :   
* Think in terms of recursive relations, how we can breakdown problems into subproblems and that too identify overlapping subproblems.    
* Then, identify optimal subtructure, that is at every point ask what problem we are solving, and if that all subproblems lead us to overall solution.  
* when writing recursion, think about base cases : think when we would have smallest valid input what would we return ? Because eventually problems  
 will broken down to converge to base cases.      
* Use python dict for memory efficient TOP DOWN Approach (or maybe use Matrix for dimensions described by input values in function which are changing)   
* Use   
```@lru_cache()
   def fun():
     fun()
```   
at the just above function to direclty use in-built memoization for recursion functions.    
# For Bottom up TABULATION :   
* How to make size of dp table ? Take hint from recursive function, the variables that changes in every recursive calls are determining the size here.     
* Think then about initialization of table using the base cases derived already in recursive relation (generally first row, first col)                General values are INT_MAX, INT_MIN based on what is required in the question, it maybe 0, 1, or boolean values like true, false etc....      
* Then, always think about after what is the state after few no. of steps in the problem ?      
* How can we now represent those states ? We need to understand about the dimensions of array/matrix.       
## What are the important variables we need to keep about at that state ? if it is just one thing we care about, we can maintain                        in 1-d array, if its two thing (like position in a grid), then 2-d array, if more than that, then more n-d type arrays.  
### So, it depends on what information is useful/important at a particular state. Now, fill the other values of n-d array and then check which cell will return the answer we require.        
# Resources :    
> * https://leetcode.com/discuss/interview-question/778035/dynamic-programming-patterns      
> * https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns    
# Identification of problem :    
### Relating to knapsack problem :   
> if there are some items given to us and we have choice to either include it or not include it ? Also we have some constraints in form of some value   like bag in knapsack or some another value that we have to fill up to or add up to ?   
## Knapsack variations (we can't take one item more than once) :  subset sum problem, equal sum partition, count of subset sums, Minimum Subset Sum Difference, Count the number of subset with a given difference, Target sum.    
## Unbounded knapsack (we can take same item more than once) : rod cutting problem, coin change-I, coin change-II   
## Longest common subsequence (LCS) (when two strings are given or one string is given and another can be some function of other) :    
> longest common substring, printing LCS, shortest common supersequence, printing shortest common supersequence, string edit (insertions/deletions/replacement), minimum insertions/deletions,  longest palindrome subsequence, minimum deletion for palindrome, minimum insertions for palindrome, longest repeating subsequence, sequence pattern matching (if string is subsequence of another string).    
## Matrix chain multiplication (MCM) (when we have to apply operations one by one for all possible places/values) :    
> palindrome partition, minimum and maximum value of expression, evaluate boolean expression, scrambled string, egg dropping puzzle.    
## DP on Trees :    
> diameter of tree, max path sum from any node to any, max path sum from leaf to leaf, diameter of n-ary tree.   
