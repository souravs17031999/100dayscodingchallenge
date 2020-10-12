# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# --------------------------------------------------------------------------------------------------------------------------------------------------
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Naive solution will be to traverse through the string, and one by one delete the current char / skip that char and check whether remaining string is palindrome 
# and finally, return the euqality of s == [::-1], so that if there is no need to deleting the occurence of char for making it palindrome then we can anyway return True
# based on last condition which returns True when string is palindrome and doesn't requires any deletion.
# TIME : 0(N ^ 2), so, can we do better than this ?
# Yes, we can actually apply the two pointers approach which is used for checking if given string is palindrome or not, then we can modify the pointers and check like 
# if two chars match, then move both towards mid (for convergence for while loop), otherwise there would be two conditions and only these two conditions arises of which :
# * one where left pointer is not matched, and after skipping it, all others matched
# * one where right pointer is not matched, and after skipping it, all otherse matched.
# We can apply above approach which works efficiently in 0(N) time complexity.
# --------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    
    def is_palindrome(self, s, left, right):
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                if self.is_palindrome(s, start + 1, end):
                    return True
                if self.is_palindrome(s, start, end - 1):
                    return True
                
                return False
        
        return True
