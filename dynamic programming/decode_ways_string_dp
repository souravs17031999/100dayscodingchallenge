# Program for counting the number of ways to decode the string.
#'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# ---------------------------------------------------------------------------------------------------------------------
# Naive solution is to simple use recursion to solve subproblems : h(s, k - 1) + h(s, k - 2)
# The solution is 0(2^N), and contains overlapping subproblems.
# We have already solved using the recursion + top_down bottom.
#
# TIME : 0(N), SPACE : 0(N)
#
#
## BOTTOM UP APPROACH :
# During the bottom up also, we can think about this in following way how to build up solutions using the previously computed solutions --
# "" => 1
# "1" => 1
# "12" => [i-1] + i[i-2], i - 1 > "1" and "2" which are valid, i - 2 > ""
# "123" => [i - 1] + [i - 2], "1" and "23" which are valid, and also "12" and "3" which is also valid 
# "1234" => "1", "234" 
# --------------------------------------------------------------------------------------------------------------------------------

def count_decode_bottom_up(s, n):

    dp = [0] * (n + 1)

    dp[0] = 1
    if s[0] != '0':
        dp[1] = 1

    for i in range(2, n + 1):
        if int(s[i - 1 : i]) > 0:
            dp[i] = dp[i - 1]
        if int(s[i - 2 : i]) >= 10 and int(s[i - 2 : i]) <= 26:
            dp[i] = dp[i] + dp[i - 2]

    return dp[n]

print(count_decode_bottom_up("12", 2))
