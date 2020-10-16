# Program to check if given "k", and string "s", if s contains all possible binary codes of length k as substring in s.
# Example 1:
#
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
# Example 2:
#
# Input: s = "00110", k = 2
# Output: true
# Example 3:
#
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
# Example 4:
#
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
# Example 5:
#
# Input: s = "0000000001011100", k = 4
# Output: false
# --------------------------------------------------------------------------------------------------
# Like , k = 2, all possible binary codes : '00', '01', '10', '11'
# and k = 3, '000', '001', '010', '011', '100', '101', '110', '111'
# total binary codes for a given k =  2^(k)
# Now, also what we can do here is we are not going to generate all the binary codes, because that would be too inefficient,
# so, we will use sliding window approach (similar to other substirng problems using a count var), and then when we get the desired window,
# we simply add the substring taken from start to k steps further from that point to a hashtable, so that all unique binary codes possible in the given string, can be maintained
# in a hashtable.
# Now, we can simply check the size of the hashtable if it matches with the required binary codes (2 ^ k).
# So, basically, all we do is we maintain a set of all unique binary codes of length k taken from the string (as a substring) and then check if its length matches with the
# required binary code number.
# -------------------------------------------------------------------------------------------------
# TIME : 0( N * K), SPACE : 0(N * K), N IS LENGTH OF STRING, K IS THE NUMBER OF BINARY CODE LENGTH REQUIRED.
# --------------------------------------------------------------------------------------------------
# Follow up - can we do more better ?
# Yes, we can actually, design our hash function (without using built-in set function), and using rolling hash function
# we can get it done in 0(1) time.
# But premature optimization is not good, and hence, we should first run the above approach, and then check if custom defined hash function if it gives better runtime.
# --------------------------------------------------------------------------------------------------

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        count = 0
        visited = set()
        start = 0
        for i in range(0, len(s)):
            count += 1
            if count == k:
                visited.add(s[start:start + k])
                start += 1
                count -= 1

        return pow(2, k) == len(visited)
