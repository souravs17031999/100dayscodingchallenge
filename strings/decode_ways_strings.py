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
# We will use DP, below is top-down DP.
# TIME : 0(N), SPACE : 0(N)

class Solution:
    def count_decode(self, s, n, cache):
        if n == 0:
            return 1

        k = len(s) - n
        if s[k] == '0':
            return 0

        if cache[n]:
            return cache[n]

        res = self.count_decode(s, n - 1, cache)
        if n >= 2 and int(s[k:k+2]) <= 26:
            res += self.count_decode(s, n - 2, cache)

        cache[n] = res
        return res


    def numDecodings(self, s: str) -> int:
        cache = [None] * (len(s) + 1)
        return self.count_decode(s, len(s), cache)


## BOTTOM UP APPROACH :

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
