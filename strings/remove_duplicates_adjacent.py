# Program to remove adjacent duplicates in the given string.
# We have to completely remove everything that is in a stream.
# EX.
# "geeksforgeek" => "gksforgk"
# "acaaabbbacdddd" => "acac"
# -------------------------------------------------------------------------------------------------------------
class Solution:
    def removeDuplicates(self, S: str) -> str:

        if not S:
            return

        stack = [S[0]]
        for i in range(1, len(S)):
            if stack and S[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[i])

        return "".join(stack)
            
