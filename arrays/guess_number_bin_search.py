# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns 3 possible results:
#
# -1: The number I picked is lower than your guess (i.e. pick < num).
# 1: The number I picked is higher than your guess (i.e. pick > num).
# 0: The number I picked is equal to your guess (i.e. pick == num).
# Return the number that I picked.
#
#
#
# Example 1:
#
# Input: n = 10, pick = 6
# Output: 6
# Example 2:
#
# Input: n = 1, pick = 1
# Output: 1
# Example 3:
#
# Input: n = 2, pick = 1
# Output: 1
# Example 4:
#
# Input: n = 2, pick = 2
# Output: 2
# -------------------------------------------------------------------------------------------------------------------------

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# ------------------------------------------------------------------------------------------------------------------------
# Naive solution will be to try out linear search for guessing number 1.....n and then returing whenever it is equal to input number, 
# TIME : 0(N), SPACE:0(1)
# can we do better ?
# Yes, search space allows us to do binary search here, 
# TIME : 0(log2(N)), SPACE : 0(1)
# ------------------------------------------------------------------------------------------------------------------------
# We can also apply ternary search to reduce time complexity to more : 0(log3(N))

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = start + (end - start) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
