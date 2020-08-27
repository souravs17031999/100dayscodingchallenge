# Program for computing longest repeating subsequence.
# such that the two subsequence don’t have same string character at same position, i.e.,
# any i’th character in the two subsequences shouldn’t have the same index in the original string.
# Now, this problem basically asks for LCS with one restriction, that we donot need to count for those which have chars at same position in both
# the strings.
# EX.
# S => "AABEBCDD"
# OUTPUT : 3
# Here, longest repeating subsequence is "ABD"
# Because as we can see it starts at various different positions :
# AABEBCDD
# _ _   _
# AABEBCDD
#  _  _  _
# Meaning if the chars occur in pair, then there will be some way possible for it be LCS with accomodates the above restriction.
# But if they occur in single occurnece, like "E" and "C" in the above, hence that's way they donot become part of longest repeating subsequence.
# Thus, simply pass same both strings in LCS(S1, S2) and just add one more condition along with if condition, "i != j", other things remain same.
# ----------------------------------------------------------------------------------------------------------------------------------------------
