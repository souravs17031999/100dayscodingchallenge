# Program for computing minimum jumps required to reach the end of array.
# We are allowed to take three jumps :
# * i - 1, i >= 0
# * i + 1, i <= len(arr)
# * i == j, arr[i] == arr[j], i != j
# -----------------------------------------------------------------------------------------------------------------------------
# We can visualize the problem using graphs making all indices as nodes of graphs and edges are those where those conditions met.
# EX. arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
#
#
#
#                     9           1
#                   /               \
#                  8                  2
#                 /        0          |
#                7                    3
#                  \                /
#                    6 --- 5 ---- 4
#
# (edges have not been shown , but we can draw the edges)
# ----------------------------------------------------------------------------------------------------------------------------
# Now, we can simply use BFS for shortest distance (minimum jumps) start from node "0" (first index) to node "9" (last index).
# Then, one thing to note is that we can check and explore i + 1, i - 1 but how do we check those nodes exploration which are twins (i == j, arr[i] == arr[j])?
# So, for efficient nodes exploration of these twins, we can maintain a hashMap which has keys has node values and all the indices where it is occuring more
# than one so that we do not have to loop again for all the indices.
# ----------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict as dd
class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) <= 1:
            return 0

        queue = deque()
        visited = set() # seen
        graph = dd(list) # hashmap for key:[indices]
        array_size = len(arr)

        # building the dict
        for i in range(array_size):
            graph[arr[i]].append(i)

        queue.append(0)
        visited.add(0)
        jump = 0
        print(graph)
        # we search layer by layer
        while queue:

            n = len(queue)
            # search layer by layer considering all the possibilities
            for i in range(n):

                curr = queue.popleft()
                # if we reached goal state
                if curr == array_size - 1:
                    return jump

                # if two possible moves
                for c in [curr - 1, curr + 1]:
                    if 0 <= c < array_size and c not in visited:
                        queue.append(c)
                        visited.add(c)

                # if third possible move
                if arr[curr] in graph:
                    for i in graph[arr[curr]]:
                        queue.append(i)
                        visited.add(i)
                    # removing because no longer needed
                    del graph[arr[curr]]

            # for each layer, we take one jump like for above example shown
            # we take 0 jump to explore '0', then 1 jump to explore '1' and '4', then 2 jumps to explore '2', and '3', then finally 3
            # jumps for '5' and '9' and there we got '9' (last index), goal state reached.
            jump += 1

        return jump
