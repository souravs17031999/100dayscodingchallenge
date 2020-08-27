# Program for printing shortest common supersequence
# Logic is similar to what we have seen in printing LCS.
# Some difference is in that in while loop,
# if last pointer to chars matches, we add char to our string as usual.
# But if they don't match, then also we need to add that char based on whichever direction we go (in direction of max)
# but we need to add the char first and then move in the respective direction.
# Now, also we can't stop when any of the pointer reaches zero, we need to add the remaining string of whichever it is part of except that ended
# with 0.
# As supersequence should contain both of the strings, so we can think as "" and "geek" => "geek", and not "".

# helper function for computing LCS
def LCS(s1, s2, m, n):

    dp = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 0

    for i in range(n + 1):
        dp[0][i] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp

def print_SCS(s1, s2):

    dp = LCS(s1, s2, len(s1), len(s2))

    i, j = len(s1), len(s2)
    result = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                result.append(s2[j - 1])
                j -= 1
            else:
                result.append(s1[i - 1])
                i -= 1

    # if anything is left over
    while i > 0:
        result.append(s1[i - 1])
        i -= 1

    while j > 0:
        result.append(s2[j - 1])
        j -= 1

    print("".join(result)[::-1])
if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print_SCS(X, Y)
