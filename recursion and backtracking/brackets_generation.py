# Program for generating balanced set of brackets possible for given n.
# In this also, we can use recursion and check some conditions based on number of opening
# of opening and closing brackets.
# Also, we know that in a balanced brackets, opening and closing will be same and will
# be equal to given n, which can help in our base case.
# ALso, we knwo string length generated will be maximum 2 * n.
# TIME: (2^N) , EXPONENTIAL COMPLEXITY, SPACE : 0(N)

def printBrackets(s, pos, open, close, n):
    if open == close == n:
        for i in s:
            print(i, end = " ")
        print()
        return

    else:
        if open > close:
            s[pos] = '}'
            printBrackets(s, pos + 1, open, close + 1, n)

        if open < n:
            s[pos] = '{'
            printBrackets(s, pos + 1, open + 1, close, n)


n = 3
s = [""] * 2 * n
printBrackets(s, 0, 0, 0, n)
