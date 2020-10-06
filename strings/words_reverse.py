# Program to reverse the complete words in the list instead of specific string/char.
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. 
# Do not include any extra spaces.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
# Example 4:
#
# Input: s = "  Bob    Loves  Alice   "
# Output: "Alice Loves Bob"
# Example 5:
#
# Input: s = "Alice does not even like bob"
# Output: "bob like even not does Alice"
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# TIME  : 0(N), N is length of string, SPACE : 0(N).
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Follow up : Could you solve it in-place with O(1) extra space ?
# Idea is to first reverse the whole string and then reverse the word by word.
# Note : in python string is immutable, so we have to use split() anyhow but then we will implment this idea assuming we have some mutable string interface given to us.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Without follow up :

class Solution:
    def split(self, s, delim):
    
        split_text = [] 
        word = "" 
        ptr = 0 

        while ptr < len(s):
        
            if s[ptr] != delim:
                word = "".join((word, s[ptr]))
            else:   
                if word != "":
                    split_text.append(word)

                word = ""

            if ptr == len(s) - 1 and s[ptr] != delim:
                split_text.append(word)

            ptr += 1

        return split_text

    def reverseWords(self, s: str) -> str:
        l = self.split(s, " ")
        left, right = 0, len(l) - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        
        return " ".join(l)

 


        
