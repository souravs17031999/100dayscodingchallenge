# Program for computing maximum occuring character in a input string
# NOTE : All the input letters are lower case ascii letters.
# NOTE : If same frequency, then lexographically least letter.
# EX. "test" :> "t", "test sample" :> "e", "cbbbbccc" :> "b"
# ------------------------------------------------------------------------------------------------------------
# Naive solution would be to traverse over the string one by one character using outer loop pointed by "i", and then for every string char
# we traverse the remaining string using one inner loop pointed by "j" and maintain a count (each time initializeing to 0 in outer loop)
# and maintain a max_char variable which keeps updating based on the value of count if found greater than previous one.
# But that would be taking  TIME : 0(N^2), SPACE : 0(1) WHERE N IS LENGTH OF STRING.
# -------------------------------------------------------------------------------------------------------------
# [2, 0, 2, 1, 0, 1, 0 ....... 0] # 26 array size list
#  0  1  2  3  4   5  6 .......25
#  a  b  c  d  e   f  g ....... z
#  traversing over string : build count array
#  traversing over count array : get the max
#  again traverse the count array : first time we see the max value, that is lexographically least
# CONCEPT USED : HASHMAPS
# TIME  : 0(N), SPACE : 0(N)
# CAN WE GET RID OF THOSE LOOPS AND DO IT JUST ONE LOOP ?
# --------------------------------------------------------------------------------------------------------------------
MAX_SIZE = 26
import sys
def compute_most_freq_char(s):

    if len(s) == 0:
        return -1

    count = [0] * MAX_SIZE
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1

    max_freq, max_char = -sys.maxsize-1, None
    for i in range(MAX_SIZE):
        if count[i] > max_freq:
            max_freq = count[i]
            max_char = chr(i + ord('a'))
    return max_char


# -----------------------------------------------------------------------------------------------------------------------
# If asked kth most frequent, then we need to use hashtable (dict) : containing chars as keys and count (occrences) as values.
# Now, sort it on the basis of frequency (count/occrences)
# Then, loop over and check when counter reaches K then that is our char.
# TIME : 0(N*log(N)) this is upper bound but if we assume the chars to be constant, then it can be considered in 0(N).
# -----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print(compute_most_freq_char("cbbbbccc"))
