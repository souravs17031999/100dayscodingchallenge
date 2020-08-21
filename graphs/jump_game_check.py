# Program for checking if it is possible to reach the index with value '0' from a given start index.
# Given, we can make a jump for every index, two possible options :
# i + arr[i] or i - arr[i], i >= 0 and i <= n .
# ---------------------------------------------------------------------------------------------------
# Note : first observation is that we can't have fractional jump but the jump will be complete.
# Next, we can visualize the problem as a graph whose nodes are indices of array and then
# edges are those values which are options for us to explore (jump) that is i - arr[i] or i + arr[i].
# --------------------------------------------------------------------------------------------------
# Naive solution would be to explore all the paths using recursion + backtracking which can be exponential.
# Can we do better ?
# Now, we can apply BFS/DFS to explore and check if there is any node (index) at which arr[node] == 0.
# There we stop, otherwise finally we return False after queue is empty in BFS or stack in DFS.
# TIME : 0(N), SPACE : 0(N)

from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = deque()
        queue.append(start)

        while queue:
            curr = queue.popleft()
            if arr[curr] == 0:
                return True
            if arr[curr] < 0:
                continue
            for i in [curr - arr[curr], curr + arr[curr]]:
                if 0 <= i < n and i not in visited:
                    queue.append(i)
                    visited.add(i)

        return False
