# Program for reversing bits of a given unsigned integer.
# Input : binary string of length = 32
# Example 1:
#
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so
# return 964176192 which its binary representation is 00111001011110000010100101000000.
# Example 2:
#
# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
# so return 3221225471 which its binary representation is 10111111111111111111111111111111.
# ---------------------------------------------------------------------------------------------------------------------------

# One thing we can do is to simple extract last bit one by one for 32 times, and check if bit is set, then we add 1 to the result
# which is initialized to 0, and keep left shifting it so that it moves to the correct position.
# So, simulataneously right shifting the i/o and left shifting the o/p will produce the right effect.

# TIME : 0(1), BOTH SOLUTION

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res << 1
            if n & 1:
                res += 1

            n = n >> 1

        return res


# There is another more intuitive approach using bitmasking.
# Suppose the input is broken down into chunks of 16 bits : so that we have two parts of input binary string and we have two masks
# which extract the two chunks by ANDing the mask with the input chunk respectively.
# Mask output: (n & 0xffff0000), (n & 0x0000ffff) => we do left shift and right shift for this extracted above two parts :
# this reverses the 16 bit chunks and take the OR of both of them.
# Then, (n & 0xffff0000) >> 16 | (n & 0x0000ffff) << 16
# Then, repeat this for 8bits chunks, 4bit chunks, 2bit chunks, 1bit chunks.


class Solution:
    def reverseBits(self, n: int) -> int:
        n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)  #0xffff0000 represents 16bits set for 32 bit representation since one f represents 4 bits
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

        return n
