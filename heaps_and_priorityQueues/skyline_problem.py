# Program to compute the skyline view of the given list of height of buildings/ elevation of buildings.
#
# We are given the nested list of all the positions : in the tuple [(x, y, h)] => (x, y) is the coordinates and h is the height.
# We are going to return the nested list of all the keypoints : keypoints defines the start of the segment and its height : [(x, h)]
# So, approach will be as follows : 
# Create a sorted list of start and end points that is 2 * length of buildings list.
# sort the buildings tuple list on the first x positions.
# Then, initialize the max-heap (priority queue) whose key is height of the building (here we take -ve heights due to max-heap not supported in python).
# We take extra element named [0, inf] while creating the heap to simplify our logic for further steps.
# So, now, whenever we get a element which is start point then we push into heap, and whenever we get end point, we remove that from the heap.
# Also, when removing we check if our last max value of height changed, then we need to add it into result and then also update the max value.
# TIME : 0(N * log(N), space : 0(N)
# -------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        res = [[0, 0]]
        heap = [(0, float("inf"))]
        for pos, negH, R in events:
            while heap[0][1] <= pos:
                heappop(heap)
            if negH:
                heappush(heap, (negH, R))

            if res[-1][1] + heap[0][0]: 
                res += [pos, -heap[0][0]],
        
        return res[1:]
