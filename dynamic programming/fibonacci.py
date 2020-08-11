# Program for computing fibonacci numbers
# ----------------------------------------------------------------------------
# Let's analyze the recursion tree as this has following recursive relations :
# f(n) = f(n - 1) + f(n - 2)
# -----------------------------------------------------------------------------
# So, we got the follwing tree :
#
#                          f(5)
#                       /       \
#                      /          \
#                    f(4)          f(3)
#                    / \        /      \
#                  f(3) f(2)   f(2)      f(1)
#                 / \     / \   / \
#                /   \   /   \ f(1) f(0)
#               /    \  /     \
#              f(2) f(1) f(1) f(0)
#             /  \
#            f(1) f(0)
#
# Now, we actually know base case: f(0) = 0, f(1) = 1.
# Time computation takes exponential time,
# The key observation : When we solve recursion tree from left to right, then we observe when we reach right child of f(4),
# and solve for f(2), then why do we again solve f(2) when we have already solved that f(2) in left child of f(3).
# Again for all right childs of f(5) : f(3) => f(2), these all have been already computed, and again we are computing this by
# traversing down to the leaf nodes (base cases) and then backtrack to the the top of tree (root node).
# ------------------------------------------------------------------------------
# This is the idea of overalapping subproblems, we need to use some kind of caching, which is in true sense DP.
# Using TOPDOWN APPROACH :
import sys
sys.setrecursionlimit(1000000)
MAX = 1000000

def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


dp = {0: 0, 1: 1}
def fib_top(n):
    if n not in dp:
        dp[n] = fib_top(n - 1) + fib_top(n - 2)

    return dp[n]

# Using BOTTOM UP APPROACH :
def fib_bottom(n):
    dp = [None] * MAX
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    #print(fib_top(3930)) top down limited to this value
    # print(fib(35))
    print(fib_bottom(100000))
