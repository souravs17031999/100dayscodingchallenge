# Program for computing the shortest/smallest window in a string containing all characters of another string.
# Input: string = “this is a test string”, pattern = “tist”
# Output: Minimum window is “t stri”
# Explanation: “t stri” contains all the characters of pattern.
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

# ---------------------------------------------------------
