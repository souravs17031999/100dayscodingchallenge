# With the same mapping from 1->26 : A->Z.
# Beyond that, now the encoded string can also contain the character '*', which can be
# treated as one of the numbers from 1 to 9.
# Given the encoded message containing digits and the character '*', return the total number
# of ways to decode it.
# Also, since the answer may be very large, you should return the output mod 109 + 7.
# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# ------------------------------------------------------------------------------------------------------------------


# "123" => "12   3" or "1 23"
# "12  3" => either this is a number "1", 2, 3 or "*"
# "1  23" => either a valid 2 digit number 23, or 2* or *2 or **
#
# s => [1, 2, *, *, 6, 1, 0]
# dp =>[1, 1, 2, ]
# dp[0] = 1, s[1] > 0=> dp[1] = 1
# dp[2] : dp[0] and d[1] forms valid number "12" => dp[2] = dp[0] + d[1] => 2
# dp[3] : dp[1] = '2', dp[2] = '*', dp[3] = 24
# similarly..

# TIME : 0(N), SPACE : 0(N)

def compute_decode_ways(s, n):

    dp = [0] * (n + 1)
    mod = 10 ** 9 + 7
    dp[0] = 1
    if s[0] == '0': return 0

    if s[0] != '0':
        dp[1] = 1

    if s[0] == '*':
        dp[1] = 9

    for i in range(2, n + 1):

        if s[i - 1] > '0':
            dp[i] += dp[i - 1]

        elif s[i - 1] == '*':
            dp[i] += 9 * dp[i - 1]

        # handling "**" and "*2"
        if s[i - 2] == '*':
            if s[i - 1] == '*':
                dp[i] += 15 * dp[i - 2]    # 11....19, 20.....26 , only 15 variations possible

            elif s[i - 1] <= '6':
                dp[i] += 2 * dp[i - 2]

            else:
                dp[i] += dp[i - 2]

        # handling "2*" , "23"
        elif s[i - 2] == '1' or s[i - 2] == '2':
            if s[i - 1] == '*':
                if s[i - 2] == '1':
                    dp[i] += 9 * dp[i - 2]   # 11 12 13....19
                else:
                    dp[i] += 6 * dp[i - 2]  # 20....26

            elif int(s[i - 2]) * 10 + int(s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

    return dp[n]

print(compute_decode_ways("12**610", 7))
