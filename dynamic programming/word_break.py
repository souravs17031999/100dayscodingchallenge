# Program for checking whether given a string S can be segmented into a valid list of strings.
# Validity is defined by whether it is in dictionery or not.
# -------------------------------------------------------------------------------------------------
# Again we can see how this problem can be solved by breaking it down further and there are overlapping subproblems.
#
#
#                      abcde
#                   /    |  \ \  \          ..............
#                 bcde  cde de e ""
#                / \ |\     | \    |        ..............
#              cde de e ""  d  e  ""
#                     .............
# -----------------------------------------------------------------------------------------------
# So, here we are seeing overlapping problems.
# -----------------------------------------------------------------------------------------------
# Algorithm is basically breaking it down by considering every prefix and then recursively calling for remaining suffix.
# ------------------------------------------------------------------------------------------------
# We will use DP to optimize it.
# --------------------------------------------------------------------------------------------------
# State is represented by dp[i][j] i, j are pointers to the chars of string denoting substring from i to j.
# so, we have to check for every state, if string[i:j] is in input, then we will fill dp[i][j] = True otherwise we will
# break it or partition it at every possible index, so let's say "k", so then string[i : k] and string[k + 1: j] should
# be true, for substring to be true.
# The matrix will be boolean valued.
# All the diagonal elements are single valued chars as i from j are just single char at position i or j in the string.
# ---------------------------------------------------------------------------------------------------------------
# if input[i....j] is in dict:
#     dp[i][j] = T
# # else :
#     dp[i][j] = T if there is some k such that dp[i][k] = T and dp[k + 1][j] = T
# --------------------------------------------------------------------------------------------
# This can also be optimized with using just single boolean array.
# ---------------------------------------------------------------------------------------------
# So, for every index in dp[index], we solve subproblem if string ending at that index is in dict or not marked by True and False.
# Now, we keep two pointers i, j , where i marks the dp table index, and j moves from i - 1 to 0
# and checks whether start of the string starts at j and ends at i is in dict or not.
# If it's the case, we mark dp[i] = True.
# ------------------------------------------------------------------------------------------------------------
# Length of dp array is one more than len(s) for considering empty string.

def word_break(s, dict):

    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] and s[j : i] in dict:
                dp[i] = True
                break

    return dp[len(s)]            
