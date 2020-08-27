# Program for minimum insertions to make a string palindrome.
# Now, if we carefully observe then, when we delete some chars to transform the string into palindrome.
# Then, we get LPS.
# Now, if we again want to make it palindrome, then we need to insert those same chars that we deleted.
# So, crux of this question is as below :
# TOTAL insertions = total deletions (which can eventually be solved using LPS)
# EX.
# abcd: Number of insertions required is 3 i.e. dcbabcd
# If we see, then we need to delete 3 chars in order to get lps (here, "a")
# which is also equal to number of insertions required.
# TIME : 0(N ^ 2)
