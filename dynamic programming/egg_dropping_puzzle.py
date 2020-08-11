# Program to compute minimum no. of trials required for getting the egg break from given no. of floors.
# There are given "k" number of floors, and "n" number of eggs.
# ------------------------------------------------------------------------------------------------------
# As we can firstly understand if there are only 1 egg, then worst case would be to start from 0th floor (or 1st floor)
# and move up one by one and check, now there are two possibilities, either it would break or not break,
# if not break, then move up, and if break move down, so in worst case we would move up to highest floor (let's say k).
# So, worst case would be k trials.
# Now, similarly we can simulate for more eggs like 2, 3, etc..
# Let's say if we have 2 eggs, then we can think recursively solving like following for 6 floors :
#
# 6 ||
# 5 ||                                      break => (2, 2)
# 4 ||                                   /
# 3 ||  => drop here (intermediate step)
# 2 ||                                   \
# 1 ||                                     not break => (3, 3)
#
# Above tuple is required in form : (eggs, floors)
# So, we can think of a recursion tree branching at every floor and every where there would be these two options
# finally converging to base cases :
# 1st base case : if floor is 1, then obvisouly only 1 trial is required
# 2nd base  case : if there are only one egg, then highest number of floor is required (going sequentially).
# ------------------------------------------------------------------------------------------------------
# Naive solution would take exponential time using simple recursion.
# So, we will write DP memoized solution.
# ------------------------------------------------------------------------------------------------------
# State is represented by dp[eggs][floors] and following recurence relations is used for filling in the entries :
# since, we want minimum trials, so we need to drop the egg from 1 to kth floor, and get the minimum out of it,
# also, since we should be able to get back the upper threshold , or upper bound on the eggs, so we take maximum for
# two cases (break or not break).
# Hence,
# min((1 + max( DP[i-1][j-1], DP[i][j-x] )) for k from 1 to jth floor)
# -------------------------------------------------------------------------------------------------------
# TIME : 0(n*k^2), SPACE: 0(n*k)

import sys
INT_MAX = sys.maxsize

def compute_min_trials(n, k):

    dp = [[None for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = 1
        dp[i][0] = 0

    for i in range(1, k + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = INT_MAX
            for x in range(1, j + 1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(res, dp[i][j])

    return dp[n][k]


if __name__ == '__main__':
    n, k = 2, 100
    print(compute_min_trials(n, k))
