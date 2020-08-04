# Program to compute the minimum number of swaps for sorting the array required in the graph.
# -------------------------------------------------------------------------
# So, basically naive approach could be selection sort => which implicitly gets the minimum
# number of swaps required for sorting but this will asymtodically , 0(N^2) sorting time.
# Since, getting minimum all the time requires atmost all the array.
# -------------------------------------------------------------------------
# can we do better ?
# So, we have to imporove this bottleneck, now we can optimize this using heaps, because
# binary heaps can get the smallest element, each time by popping off.
# First, we can get linear time building heap and getting by popping it off, in 0(N*log(N)).
# Now, also just by using heaps, we can't get the index with which to swap.
# So, for that we can also pair inside heap but we will not be able to update the index every time ,
# and so, we can keep a index mapping and keep it updated whenever swap happens.
# This will take total space upto 0(N).
# ---------------------------------------------------------------------------
# def minSwaps(nums):
#     keyToIndex = dict([(nums[i], i) for i in range(len(nums))])
#     heap = nums[::]
#     heapq.heapify(heap)
#
#     swaps = 0
#     for i in range(len(nums)):
#         smallest = heapq.heappop(heap)
#
#        # check if previous swappes luckily made the array sorted
#         if nums[i] != smallest:
#             currNum = nums[i] # needed to update the dic two lines below
#             nums[i], nums[keyToIndex[smallest]] = nums[keyToIndex[smallest]], nums[i]
#             keyToIndex[smallest], keyToIndex[currNum] = keyToIndex[currNum], keyToIndex[smallest]
#             swaps += 1
#
#     return swaps
# -----------------------------------------------------------------------------
# Can we do better in terms of space efficiency ?
# So, we can visualize this question in terms of graphs, and we can actually understand
# So, we can actually use concept of cycles in graphs and relate them with a pair : (actual index in the sorted array, original index in the unsorted array).
# So, if we are able to keep a track of original index and then final index in sorted array, then
# we can actual think that it forms a cycle like a graph which can be swapped (so there exists a edge from i to j, if the ith element is actually at jth pos after sorting).
# Also, we can observe that no of swaps for any cycles depend on nodes containing them,
# so like cycle with 2 node will contains 1 swap, cycle with 3 node will contains 2 swaps.
# It means if we are able to compute a cycle size, then our result can be cycle size - 1,
# for each swap, and this can keep repeated for all array indices by checking and keeeping a visited
# array so that we donot keep on moving in the loop or cycle.
# TIME : 0(N*log(N)), SPACE : 0(N)
# We are not actually improving the space but in practical terms extra space is less than above solution.
# -----------------------------------------------------------------------------
#
#                 ---------------
#                |    |----|    |
#                4    3    2    1
#                |              |
#                 --------------
# and since after sorting : [1, 2, 3, 4] => [0, 1, 2, 3] so, like 1 should be edged to 4
# (due to index = 0), and 2 should be edged to 3 (due to index = 1)
# -----------------------------------------------------------------------------

def compute_min_swaps(arr, n):

    arr = list(enumerate(arr))
    arr.sort(key=lambda x : x[1])
    vis = [0] * n

    count = 0
    for i in range(n):
        if vis[i] or arr[i][0] == i:
            continue

        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = 1
            j = arr[j][0]
            cycle_size += 1

        if cycle_size > 0:
            count += (cycle_size - 1)

    return count

if __name__ == '__main__':
    arr = [1, 5, 4, 3, 2]
    print(compute_min_swaps(arr, 5))
