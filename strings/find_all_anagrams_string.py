# Program to find all the possible anagrams of the string "p" in the given string "s".
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# ----------------------------------------------------------------------------------------------------------------------------
# So, we have already done how to check if two strings are anagrams of each other using hashmaps, so, this will be useful here also.
# Now, we are going to extend the above version and think how about we can go checking for all possible anagrams in the string "s".
# Brute force method would be to generate all the substrings of length of string "p", and then count each one of them in "s" and compare their counts
# with chars of "p".
# with little optimizations we could do it in 0(N^2) time with space : 0(1).
# But can we do more better keeping space : 0(1).
# We can use sliding window approach which can be useful to traverse the entire string in 0(N) time, and also while we match the window size of lenght
# of stirng "p", we keep maintaingin a hashmap of size 26 (constant), which tracks count of all chars in the current window, and now we compare
# both hashmaps (one for dynamic current window and one constant for "p"), which will be done in 0(1), because size 26 is fixed here.
# Hence, using both sliding window approach + hashing here
# ------------------------------------------------------------------------------------------------------------------------------
# We can dry run on the above exmaple 1 :
# ex.
# p = "abc"
# p_map : {'a': 1, 'b': 1, 'c': 1}
# s = "cbaebabacd"
# we start off with left pointer of window pointing to 0th index, and start putting into map alng with it,
# first window : starting at 0, ending at 2, => "cba" matches frequnecy count with p_map, so we include it in out result.

#  ____
# |cba|ebabacd   => "cba" anagram of "abc"
# ----
# Then second window,
#   ____
# c|bae|babacd
#  ----
# Similarly, we check it doesn;t matches with p_map.
# keep doing it and there will be one more match at starting index from 6, to 8
#        ___
# cbaeba|bac|d  => "bac" anagram of "abc"
#        ---
# we include it in result output.
# --------------------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(1)
# ----------------------------------------------------------------------------------------------------------------

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map = [0] * 26
        map = [0] * 26
        output = []

        count = 0
        start = 0
        k = len(p)

        for i in p:
            p_map[ord(i) - ord('a')] += 1

        for i in range(0, len(s)):
            count += 1
            map[ord(s[i]) - ord('a')] += 1

            if count == k:
                if map == p_map:
                    output.append(start)

                map[ord(s[start]) - ord('a')] -= 1
                start += 1
                count -= 1

        return output
