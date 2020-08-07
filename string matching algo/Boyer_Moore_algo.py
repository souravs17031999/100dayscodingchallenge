# Boyer moore algorithm implementation logic.
# Okay, so improving more on string searching algorithms, this one is mostly used in practical times in today's most algorithms.
# There are two rules on which it works :
# One of the important things is that we iterate from left from right, but when we comparison we compare from
# right to left, and apply the rule when mismatch occurs :
# ---------------------------------------------------------------------------------------------------------------------
# Bad character rule :
# * Upon mismatch, skip alignments until (a) : mismatch becomes a match, (b) : p moves past mismatched character
# Ex. shown below :
# T :  G C T T C T G C T A C C T T T T G C .....
#              _
# P :  C C T T T T G C
#        _     --
# -- is showing mismatched character, and now we search the position where the mismatched char in T, "c"
# occurs in P, and we found that in the left of mismatched direction, and so we can actually skip two alignments
# so overall we now moved onto as shown below :
# T :  G C T T C T G C T A C C T T T T G C .....
#                        _
# P :       _C C T T T T G C
#                        --
# Now, mismatch occurs at "G", but mismatched char in T -> "A" is not anywhere in the left direction
# and hence, we can simply move past the alignment from the mismatched char in T.
# T :  G C T T C T G C T A C C T T T T G C .....
# P :                      C C T T T T G C
# -----------------------------------------------------------------------------------------------
# Good Suffix rule :
# * Let "t" be substring matched by inner loop, skip until (a) there are no mismatches between P and t or
# (b) P moves past t.
# T : C G T G C C T A C T T A C T T A C T T A C T T A C G C A A ......
#                 _____
# P : C T T A C T T A C
#              -- _____
# Here, -- showing position of mismatched char, "C" <> "T", and hence, we search where pattern "TAC" which is already mismatched,
# occurs in left of pattern from the point where mismatched char occurs,
# Now, we will skip till again we found "TAC" in the left as shown below :
# T : C G T G C C T A C T T A C T T A C T T A C T T A C G C A A ......
#                 _____________
# P :         C T T A C T T A C
#                 _____________
# Now, since the matched suffix is nowehere completely found in the left, but there is a part of suffix which is present "CTTAC",
# so we will skip till these matches.
# T : C G T G C C T A C T T A C T T A C T T A C T T A C G C A A ......
#                     _________________
# P :                 C T T A C T T A C
#                     _________________
# Now pattern is completely matched !
# -------------------------------------------------------------------------------------------
# NOTE : This Algorithm uses the idea of both rules and take the skip alignment = max(both the skip alignment got from both rules).
# We will try to skip more and more....
# Precomputation of two tables for both rules is applied for efficient searching !
# Building these tables will take 0(N) time, space : 0(N).
# Best case and Average case : 0(N/M), but worst Case : 0(M*N).
