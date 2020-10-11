# Write a program that computes the length of the longest common subsequence of three given strings. 
# For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5, since the longest common subsequence is "eieio".
# We can solve this problem using the idea same as in LCS for two strings but now extended to three strings, so 3d matrix is required for bottom up DP.
#
# The idea is to take a 3D array to store the 
# length of common subsequence in all 3 given 
# sequences i. e., L[m + 1][n + 1][o + 1]
#
# 1- If any of the string is empty then there is no common subsequence at all then
#           L[i][j][k] = 0
#
# 2- If the characters of all sequences match
#   (or X[i] == Y[j] ==Z[k]) then
#        L[i][j][k] = 1 + L[i-1][j-1][k-1]
#
# 3- If the characters of both sequences do 
#   not match (or X[i] != Y[j] || X[i] != Z[k] 
#   || Y[j] !=Z[k]) then
#        L[i][j][k] = max(L[i-1][j][k], 
#                         L[i][j-1][k], 
#                         L[i][j][k-1])
#                         
#                         
# s1 = "epidemiologist"
# s2 = "refrigeration"
# s3 = "supercalifragilisticexpialodocious"
#

def LCS(s1, s2, s3, n1, n2, n3):
    
    dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(n3 + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] =  0
                elif s1[i - 1] == s2[j - 1] and s1[i - 1] == s3[k - 1]:
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                else:
                    dp[i][j][k] = max(max(dp[i - 1][j][k], dp[i][j - 1][k]), dp[i][j][k - 1])
    
    return dp[n1][n2][n3]
    
print(LCS(s1, s2, s3, len(s1), len(s2), len(s3)))
