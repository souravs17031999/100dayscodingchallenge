# Program for computing the shortest/smallest window in a string containing all characters of another string.
# Input: string = “this is a test string”, pattern = “tist”
# Output: Minimum window is “t stri”
# Explanation: “t stri” contains all the characters of pattern.
# Program for computing length of minimum window substring and also print that substring along with length
# meaning minimum window of "s" containing all chars of "t".
# If not possible, then return ""
# It is guranateed, that if possible, then only unique minimum substring will be possible.
#
# Input: string = “geeksforgeeks”, pattern = “ork”
# Output: Minimum window is “ksfor”
# ----------------------------------------------------------------------------------------------------------------
# This means we need to get different windows in the string given to us, and then check the occurence of pattern in the different windows
# and get the shortest length of all of them.
# Naive solution is to generate all the possible substrings and then check if the particular window satisfies the pattern constrainsts, then
# we need to get the length, and overall the minimum of all window lengths.
# This will take 0(N^3) so, we need to optimize it.

# Let's think in different way but using above approach :

# We know that two pointers need to be there : left and right, and then first we keep expanding using right pointer to first check
# if the window conforms to the constrainsts and then start minimizing the window by using left pointer.
# So, we keep moving right pointer and left pointer simulatenously once expanding and then if window confirmed, then contracting from left.
# This will go on for all the windows, we need to get the overall minimum window length.

# First window :
# "this is a test string"
#  L         R

# Second window :
# "this is a test string"
#       L       R

# Third window :
# "this is a test string"
#               L    R

# # We firstly, maintain a hashMap of all the occurence of chars in "t" so that all chars are mapped with their
# occurences and at any point, if the hashmap value is positive, then we know that we are needefull of that
# character and once we hit that character using "end" ptr, we decrement it in the hashmap.
# Now, how do we know that we have got a valid window ?
# We will use a count var for that, and if the above hashmap updated on positive occurence of char, and if 
# count reaches length of "t", then we know valid window has been reached.
# Now, to again keep on searching, we start contracting from left, that means we move start ptr from left, 
# and make the window invalid by removing useful char of "t", so, if we get a useful char, we increment its 
# count in hashmap, but count is updated only if we have positive value after updation.
# and count will be decremented now in this case, as we have removed useful char of our window, so total 
# useful/valid chars in our window has decreased now by 1.
# and this inner while loop will be stopped and we will again start moving end (right) ptr.
# In this way, algo will work till end < len(s).

# ------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(|S| + |T|), SPACE : 0(|S| + |T|)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = {}
    
        if len(s) == 0 or len(s) < len(t) : return ""

        for i in t:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        start, end = 0, 0
        count = 0
        min_length = sys.maxsize
        temp = len(t)
        min_start = start
        while end < len(s):

            if s[end] in map:
                if map[s[end]] > 0:
                    count += 1

                map[s[end]] -= 1

            while count == temp:

                if (end - start + 1) < min_length:
                    min_length = (end - start + 1)
                    min_start = start

                if s[start] in map:
                    map[s[start]] += 1
                    if map[s[start]] > 0:
                        count -= 1

                start += 1

            end += 1

        if min_length != sys.maxsize:
            return s[min_start : min_start + min_length]
        else:
            return ""


# ---------------------------------------------------------
