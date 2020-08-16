# Program for computing how many distinct ways of climbing up the stairs.
# It takes n steps to reach to the top.
# NOTE : we can either climb 1 or 2 steps.
# -------------------------------------------------------------------------------
# So, we can observe that to reach nth floor, we can actually combine steps to reach (n - 1)th stair and
# (n- 2)th stair, as we can either climb 1 or 2 steps.
# So, let's say if we are at 6th step, then either we can climb from 4th stair directly to 6th stair (2 steps) or we can
# climb from 5th stair to 6th stair (1 step).
# -------------------------------------------------------------------------------
# We can now directly understand the recursive tree :
#
#                          f(5)
#                       /       \
#                      /          \
#                    f(3)          f(4)
#                    / \        /      \
#                  f(1) f(2)   f(3)      f(2)
#                 / \     / \   / \
#                /   \   /   \ f(1) f(0)
#               /    \  /     \
#              f(-1)  f(0) .......
#              ..........................
#
# The tree will be same as fibonaaci recursion tree, infact the answer can be directly the value of fib number n .
# as the recursive relations are same in both cases.
# --------------------------------------------------------------------------------
# So, we can apply the same approach of memoization technique for DP.
# ---------------------------------------------------------------------------------
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}

# If more steps like 1, 2, or 3, then similar above can be extended for more steps as well keeping same asymtodic bounds.
