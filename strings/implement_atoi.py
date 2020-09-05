# Program for conversion of string to integer.
# NOTE :
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# TIME : 0(N), SPACE : 0(1)

class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        result = 0
        if len(str) == 0: return 0

        while i < len(str) and str[i] == ' ':
            i += 1

        if i < len(str) and (str[i] == '+' or str[i] == '-'):
            if str[i] == '+':
                sign = 1
            else:
                sign = -1
            i += 1

        while i < len(str) and str[i].isnumeric():
            result = result * 10 + (ord(str[i]) - ord('0'))
            i += 1

        return max(-2**31, min(sign * result,2**31-1))
