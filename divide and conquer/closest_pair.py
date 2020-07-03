# Program for finding the closest pairs in terms of distances, from a given set of points in
# 2-d space.
# IDEA: This is to be thought paradigm , a non trivial divide and conquer approach but is simply observed from 1-d points ,
# if we want to find closest pair, then we can sort it and then do a linear scan of consecutive elements to find the closest pair.
# Now, extending this idea to 2-dimensions, we now have two coordinates,
#-----------------------------
# Idea is to first sort it on basis of x-coordinate
# Then, we need to recursively divide the array into two parts by computing the midpoint and computing distance between closest pairs for those parts
# A base case can be taken care of when we have less than 4 points, by brute force approach (scanning through list two times in 0(N^2))
# Now, when we have completed all the closest pairs from both sides and got minimum, then we need to also consider those pairs whose first part is on
# left side of divided array, and second part is on right side of divided array.
# So, now we need to consider a strip (a column of width of already found minimum so far because beyond this, all will be greater than this)
# To find minimum for this strip, we only need to iterate constant number of times (as it has already been proved = atmost 7 times) for every point
# in the strip, and return the minimum from this strip
# Finally , we can return the already found minimum from left and right all pairs, and the strip pairs returned minimum.
#------------------------------------
# TIME : 0(N*lg(N))

from math import sqrt
import sys
import random

# lambda function to compute distace (euclidean metric to be used here)
distance = lambda p1, p2 : sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# searching one by one for each point, and getting minimum from all pairs, useful for base case
def BruteForce(arr, n):
    min_dist = sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, distance(arr[i], arr[j]))

    return min_dist

# function for getting minimum from the strip formed within the delta region found (where delta is the minimum already found from left and right parts)
def ClosetStrip(strip, n, d):
    min_dist = d
    # sorting the array using comparator on y - coordinate
    strip.sort(key = lambda x: x[1])

    # This is proved that inner loop only runs constant no. of times (atmost 7 times)
    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 7 times

    for i in range(n):
        j = i + 1
        while j < n and strip[j][1] - strip[i][1] < min_dist:
            min_dist = distance(strip[j], strip[i])
            j += 1

    return min_dist

# function for computing distance recursively
def ComputeMinDist(arr, n):

    # base case
    if n <= 3:
        return BruteForce(arr, n)

    mid = n // 2
    midpoint = arr[mid]

    # Consider the vertical line passing
    # through the middle point calculate
    # the smallest distance dl on left
    # of middle point and dr on right side

    dmin_left = ComputeMinDist(arr[:mid], mid)
    dmin_right = ComputeMinDist(arr[mid:], n - mid)

    # this is the minimum of both left and right parts
    dmin = min(dmin_left, dmin_right)

    # Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    strip = []

    for i in range(n):
        if abs(arr[i][0] - midpoint[0]) < dmin:
            strip.append(arr[i])

    # Find the closest points in strip.
    # Return the minimum of d and closest
    # distance is strip[]

    return min(dmin, ClosetStrip(strip, len(strip), dmin))

# main function for computing closest distance , useful for calling the recursive function
def ClosestDist(arr, n):
    # sorting the array using comparator on x - coordinate
    arr.sort(key = lambda x : x[0])
    return ComputeMinDist(arr, n)

if __name__ == '__main__':
    p = [[random.randint(0, 100), random.randint(0, 100)] for _ in range(10)]
    # p = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
    print(p)
    n = len(p)
    print(f"minimum distance : {ClosestDist(p, n)}")
