# Program for computing K closest points from origin.
# Given, a list of points on the 2-D plane and an integer K.
# Distance could be Euclidean distance : (x1, y1) and (x2, y2) => sqrt((x2-x1) ^ 2 + (y2-y1) ^ 2)
# -------------------------------------------------------------------------------------
# point = [[3, 3], [5, -1], [-2, 4]], K = 2
# Naive approach is to compute these distances, and then sort it and then return the k points.
# distances = (sqrt(18), sqrt(26), sqrt(20)), sorted : sqrt(18), sqrt(20) => points : [3, 3], [-2, 4]
# -------------------------------------------------------------------------------------
# This would take bound of TIME : 0(N*lg(N)), space : 0(1).
# Can we do better ?
# ----------------------------------------------------------------------------------------
# Another approch as shown below to be use of Priority Queue which is really efficnet for these types
# of applications will do it in (n + k*lg(N))

import math
def Euclidean(x, y):
    return math.sqrt(x ** 2 + y ** 2)

from heapq import heapify, heappop, heappush
def compute_distance(arr, k):
    distances = []
    heapify(distances)
    for i in range(len(arr)):
        heappush(distances, (Euclidean(arr[i][0], arr[i][1]), (arr[i])))

    for i in range(k):
        print(f"[{heappop(distances)[1]}]", end = " ")


if __name__ == '__main__':
    arr = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    compute_distance(arr, k)
