# Program for counting the set bits for the given range query.
# Assume all range starts from 0 and goes till Num.
# Input : Num (int)
# 0<=n<=Num, find for all n values
# We have already seen simple solutions but here we will use a trick due to number of ranges so that query takes 0(1).

# We can observe one fact that if we know set bits of some "x", then we can find out set bits of "x/2" or vice-versa.
# If the number is odd, and we right shift (divide by 2), then we lose "1" at its least significant digit.
# so, count of set bits will also be affected.
# If the number is even, and we right shift (divide by 2), then no change in set bit count as lsb contains 0.

# So, let's say : x = 2 =>  set bits of 2 => 1, then set bits of 4 => even => 1, but if 5 => odd => 1 + (5 >> 2) => 2
# and set bits of x = 7 =: 3, set bits of 14 => even => 3, and set bits of 15 => 1 + 15>>2 => 1 + 3 => 4

# ------------------------------------------------------------------------------------------------------------------------

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num + 1):
            if i & 1:
                ans.append(1 + ans[i >> 1])  # ans[i >> 1] is same as ans[i // 2]
            else:
                ans.append(ans[i >> 1])

        return ans
