# Program for computing longest substring with no repeating chars/no duplicates in the substring.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
# ----------------------------------------------------------------------------------------------------------------------------------
# Naive solution will be to use two loops to traverse from left to right part of subarray and then count if any char repeats, or not repeats, then take the max length
# of the segment in 0(N^3).
#
# Can we do better than this ?
# Now, we can use HashSet + sliding window technique to solve this problem.
# Choose left, right pointers for the current window, move right ptr till the length of entire array/string, one by one, and check if new char is in set, 
# then, we need to remove from the start of the window by moving left ptr from the left of window.
# If it is not in the set, then move it to set, and compute the max length by simply taking the length of the set as max_len.
# TIME : 0(N), SPACE : 0(N).
# ---------------------------------------------------------------------------------------------------------------------------------
#
import sys 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        if len(s) == 0:
            return 0
        
        start, end = 0, 0
        max_length = -sys.maxsize-1
        while end < len(s):
            
            if s[end] not in visited:
                visited.add(s[end])
                max_length = max(max_length, len(visited))
                end += 1
            
            else:
                visited.remove(s[start])
                start += 1
            
        return max_length
