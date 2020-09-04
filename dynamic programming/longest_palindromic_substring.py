# Program for getting the longest palindromic substring and print the substring.
# We have already seen one of the solution using expanding around center in 0(N^2), space : 0(1).
# Other solution is to use dynamic programming.
# So, this problem is similar to bottom up dp table for MCM, palindromic partitioning......
# and fill only the half up table.
# DP[i][j] state is a boolean value which solves the subproblem  whether s[i].....s[j]  is palindrome or not ?
# Base case :
# if only one char is there, that is always palindromic (it is T) : dp[i][i] = T, if s[i] == s[j], where i == j
# if there are two chars, we can simply check if both chars are same, then it T, otherwise F., dp[i][i + 1] = T (if s[i] == s[i + 1])
# Other values will be filled as follow :
# Now, we can observe that in "xabax", if we know "aba" is palindrome, so, we can check if dp[i + 1][j - 1] is T and s[i] == s[j]
# where i and j are denoting left and right pointer to first index ("x") and last index ("x") respectively.
# In this way, total dp table will be filled.
# While filling the dp table, if we found anywhere it is palindrome then we update the max_length overall.
# and also update the start index for palindrome (pointed by "k").

for k in range(n):
    for i in range(n - k + 1):
        j = i + k - 1
        .........
        check conditions and fill the table.
        update the max_length overall,
        start = i,

end = start + max_length - 1

print(s[start : end + 1])
