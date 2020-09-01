# Program to count all the possible number of ways to construct the target string using characters from strings
# in the given array such that indices of the chars used in string construction forma strictly increasing sequence.
# Multiple chars can also be sued from the same string.
# Input : A = ["adc", "aec", "erg"], S = "ac"
# Output : 4
# Target string can be formed in following ways :
# 1) 1st character of "adc" and the 3rd character of "adc".
# 2) 1st character of "adc" and the 3rd character of "aec".
# 3) 1st character of "aec" and the 3rd character of "adc".
# 4) 1st character of "aec" and the 3rd character of "aec".
# Input : A = ["afsdc", "aeeeedc", "ddegerg"], S = "ae"
# Output : 12
# -------------------------------------------------------------------------------------------------------
