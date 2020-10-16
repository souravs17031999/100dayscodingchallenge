# Program for computing Minimum number of days when given "n" number of oranges.
# Everytime we have three options :
# * Eat one orange.
# * If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
# * If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
# You can only choose one of the actions per day.
# Return the minimum number of days to eat n oranges.
# --------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: n = 10
# Output: 4
# Explanation: You have 10 oranges.
# Day 1: Eat 1 orange,  10 - 1 = 9.
# Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
# Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1.
# Day 4: Eat the last orange  1 - 1  = 0.
# You need at least 4 days to eat the 10 oranges.
# Example 2:
#
# Input: n = 6
# Output: 3
# Explanation: You have 6 oranges.
# Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
# Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
# Day 3: Eat the last orange  1 - 1  = 0.
# You need at least 3 days to eat the 6 oranges.
# Example 3:
#
# Input: n = 1
# Output: 1
# Example 4:
#
# Input: n = 56
# Output: 6
# ----------------------------------------------------------------------------------------------------------
# Let's first think about it clearly - so, we have n ornages and we need to finish it as soon as we can to minimize the number of days.
# So, first option gives us to reduce the number by 1 => 10%
# second option gives us to reduce the number by n//2 => 50%
# and third option gives us to reduce the number by 2*n//3 => 60%
# So, probably we want to apply greedy approach to try first checking if 3 rd option is possible, then if 2nd option, finally third option (which
# is always possible).
# But this gives the wrong answer in the sample example 1 only,
# n = 10
# day 1 : choose 2nd option => 10 - (10//2) => 5
# day 2 : choose 1 st option => 5 - 1 => 4
# day 3 : choose 2nd option => 4 - 4//2 = 2
# day 4 : choose 2nd option => 2 - 2//1 => 1
# day 5 : choose 1st option => 1 - 1 = 0
# so, as we can see this takes 5 days but optimal solution takes 4 days using the path shown above in the sample output for 1st example.
# -------------------------------------------------------------------------------------------------------------
# Now, we have proved greedy will not work here.
# This also means we need to explore all the possible paths possible, and whenever we reach "0" at any point in time, we need to stop exploring ,
# and should be done in minimum time (days) possible, that porbably hints us to think in terms of graph traversal algorithm, wehere every node branches
# off max 3 nodes from itself, and BFS traversal to search every possible path layer by layer in minimum time node reachable from n to 0.
# So, we can think of applying BFS here using queue as intermediate ds.
# We can also use recursion to write the same solution due the graph nature of the problem
# Following is the visualization for the exploration tree :
#
#
#
#                     n = 10      l = 0
#                   /   \
#                   5   9        l = 1
#                 |    /    \
#                 4   8     3   l =  2
#               /  \  /\    /\
#             3    2 7 4   2   1    l = 3
#           /\   /\  | /\  /\  |
#         2  1  1 1 6 3 2 1 1 0    l = 4
#
# ans : 4 as we reached "0".
#
# Note : from the above graph/tree, we also see overlapping subproblems/paths, so probaly, we need to do some memoization here and we can actually cut
# off this / remove the path / not going that path if we have seen that path, because here we need to stop as soon as we see a 0 in any layer,
# and if we did not cutoff this path further (repeated one), then it will lead to TLE (more time) for bigger value of "n".
# fOR THAT WE can use Hashset "seen" to take this into consideration so that we do not explore same paths again and again.
# This typeof memoization will be also useful in the recursive solution we will write.
# -----------------------------------------------------------------------------------------------------------------
# TIME : 0(log^2(N))
# SPACE : 0(log(N))
# -----------------------------------------------------------------------------------------------------------------
# BFS approach + DP (memoization)

from collections import deque
class Solution:
    def minDays(self, n: int) -> int:

        queue = deque()
        queue.append(n)
        min_days = 0
        a, b, c = None, None, None
        seen = set()

        while queue:
            min_days += 1
            size = len(queue)

            for i in range(size):
                curr = queue.popleft()
                a = curr - 1
                queue.append(a)
                if curr % 2 == 0:
                    b = curr // 2
                    if b not in seen:
                        queue.append(b)
                        seen.add(b)

                if curr % 3 == 0:
                    c = curr - (2 * (curr // 3))
                    if c not in seen:
                        queue.append(c)
                        seen.add(c)

                if a == 0 or b == 0 or c == 0:
                    return min_days

        return min_days

# ----------------------------------------------------------------------------------------
# Recursive solution + DP (top down memoization):
# In each step, choose between 2 options: minOranges = 1 + min( (n%2) + f(n/2), (n%3) + f(n/3) ) where f(n) is the minimum number of days to eat n oranges.

class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:

        if n <= 1:
            return n

        return 1 + min(n % 2 + self.minDays(n//2), n % 3 + self.minDays(n//3))
