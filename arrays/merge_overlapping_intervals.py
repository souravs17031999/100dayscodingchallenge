# Program for merging overlapping intervals if possible .
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# as we can see, [1, 3] and [2, 6] overlaps, so [[1, 6], [8, 10], [15, 18]]
# output : [[1,6],[8,10],[15,18]]
# --------------------------------------------------------------------------------------------------------------
# Naive solution would be to check for every pair of intervals, if starting point of next interval is smaller than ending point of
# previous interval, so overlap occurs.
# Hence, checking this for every pair would be in 0(N^2).
# Keep appending those which are overallping into a new output array.
# -----------------------------------------------------------------------------------------------------------------
# Can we do better ?
# Yes, we can actually observe that after we sort this on starting times, then it is more logical to checking for the above condition
# and can be done in only one linear pass.
# We start with adding the first interval in the output array and check if the overlap occurs, then we need to update the ending time of
# the interval in the output array, otherwise simply add the next intevral into the output array and update the current interval.
# TIME : 0(N * log(N)), SPACE : 0(N)
# ------------------------------------------------------------------------------------------------------------------
# Why sorting is required in first place ?
# So, there's this mathematical prove that after sorting we get all subintervals to be merged in contiguos runs of sorted list.
# Also, we can visualize this as shown below : 
# [(1, 9), (2, 5), (19, 20), (10, 11), (12, 20), (0, 3), (0, 1), (0, 2)]
#                            ||
#                             ^
# After sorting, 
# [(0, 3), (0, 1), (0, 2), (1, 9), (2, 5), (10, 11), (12, 20), (19, 20)]
#   ______________________________________  ______    ________________
# There are 3 contiguos runs of sorted subintervals which can be merged.
# ---------------------------------------------------------------------------------------------------------------

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x : x[0])
        output = [intervals[0]]
        curr_interval = intervals[0]
        for i in range(1, len(intervals)):
            curr_start, curr_end = curr_interval[0], curr_interval[1]
            if curr_end >= intervals[i][0]:
                curr_interval[1] = max(curr_end, intervals[i][1])
            else:
                curr_interval = intervals[i]
                output.append(curr_interval)
        return output        
