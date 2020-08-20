# Program to check whether we can reach the end of array from starting index 0,
# using the given positions as index of array which are maximum jumps one can do from that index.
# ------------------------------------------------------------------------------------------
# EX. [2,3,1,1,4]
# as we can see, from first index (0), we can jump to 2nd index, then, to 3rd index, and finally to last 4th index.
# so, we return True.
# EX. [3,2,1,0,4]
# as we can see, from first index, if we try to jump max (=3), it will take me to 0, from where i can not go anywhere.
# let's try for lesser value, (=2), so, again from first index, taking jump of 2, we reach 2nd index, from there only one option to jump 1 to
# next position which is again 0, from where i can not go anywhere.
# let's try for lesser value (=1), we first jump 1 from first index to second index, again we have two options of which both will not lead
# to end of array.
# Thereby not reachable.
# -------------------------------------------------------------------------------------------
# The above intuition shows that this problem is actually recursive in nature, so backtracking solution is possible - try all the
# possible solutions , exhaustive search => 0(2 ^ N)
# Therefore, we think can we do better ?
# We can try this to minimize it to 0(N^2) using recursion + memoization or bottom up DP but of that is overkill for this problem.
# It can solve simply using simple trick and observation, if we try to traverse from right to left (intuitvely more logical), so, we
# know we can know reach end, but starting from end till first index, one by one we check if it is possible to reach the end from that index,
# for that we just need to assume last_reached pos = len(arr) - 1, and now at every index, we just check if the jump is in reach / range
# so, i + arr[i] < last_reached pos, then we update last_reached pos.
# in this way if we reached first index, and last_reached pos == 0, it means it is possible to reach the end of array.
# TIME : 0(N), SPACE : 0(1).
# -------------------------------------------------------------------------------------------

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= pos:
                pos = i
        return pos == 0        
