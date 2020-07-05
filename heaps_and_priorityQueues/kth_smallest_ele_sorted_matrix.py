# Program to find kth smallest element in the row and col wise sorted matrix.
# Dimenstions are N*N
# IDEA: Naive solution would be to simply merge every row of sorted matrix, which takes time of n*n*lg(k)
# OPTIMIZED APPROACH :
# We can observe that for any matrix (row and col wise sorted), the leftmost element is the smallest and the most probable chance of next smallest
# matrix would be either on right side, or just below side.
# It means, we need to keep track of just greater than element that the first leftmost element (corner one) for any given submatrix of the matrix.
# This gives intution for building a binary min heap.
# We can simply firstly insert first row in the heap, after that we can start off the corner element and took if off and then insert next two
# (bottom and right one) and keep doing it until we reach kth smallest.
# This takes 0(N + K(lg(N))), SPACE : 0(R), where R is length of row.


from heapq import heappush, heappop, heapify

def KSmallestEle(arr, n, k):
    if k > n * n:
        return

    heap = []
    heapify(heap)
    # visited keeps a track of which indices were already visited in the matrix,
    # takes care of duplicates.
    visited = set()
    for j in range(len(arr[0])):
        heappush(heap, (arr[0][j], 0, j))
        visited.add((0, j))

    res = None
    # iterating k - 1 times,
    for i in range(k):
        # popping off root of heap which is current min
        res, i, j = heappop(heap)
        # check whether we are inside bounds
        if i + 1 < n:
            # checking for just below element
            if (i + 1, j) not in visited:
                heappush(heap, (arr[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            # checking for just right element
            if (i, j + 1) not in visited:
                heappush(heap, (arr[i][j + 1], i, j + 1))
                visited.add((i, j + 1))
    return res

# driver test function
if __name__ == '__main__':
    mat = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [25, 29, 37, 48],
        [32, 33, 39, 50]]

    print(KSmallestEle(mat, 4, 7))
