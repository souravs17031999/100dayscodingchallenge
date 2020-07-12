# Program for counting the values for a given "K" in a multiplication table of dimension N X N, of given number N.
# If we actually write the multiplication table and observe that the matrix generated is of row wise and col wise sorted order but again there
# is no such invaraint that we can directly apply binary_search.
# Still, we can apply binary_search for each row in the matrix and that would give us (M*Lg(N)) time complexity (Better than N^2).
# But can we do better ?  Yes, we can still apply our stair case search, just trick is that we don't stop if we find the value and continue
# the search.
# so, What we also observe is that search space is reducing from above the index of row at which first occurence is found,
# and also values if repeated are repeated in search space defined by at least lesser than the current column.
# so, we can simply move to next row with same column (or may just a col. less but that wouldn't make significant difference until N is large)
# and we can continue our search with the same stair case algo.
# That would give us overall in same complexity bounds : 0(M+N), and space : 0(1).

import random
def matrix_search_staircase(l, m, n, k):
    # starting from right most upper corner
    i = 0
    j = n - 1
    count = 0
    # check till row index hits max and column index hits min
    while(i <= m - 1 and j >= 0):
        # if smaller then, move to previous column
        if k < l[i][j]:
            j -= 1
        # if greater, then move to next row
        elif k > l[i][j]:
            i += 1
        # otherwise if it is equal, then return true
        else:
            count += 1
            i += 1


    # return false , not found
    return count


# ALTERNATE SOLUTION FOR 0(M*lg(N))

# def binary_search(l, start, end, key):
#     while(start <= end):
#         middle = start + (end - start) // 2
#         if l[middle] < key:
#             start = middle + 1
#         elif l[middle] > key:
#             end = middle - 1
#         else:
#             return 1
#     return 0
#
#
# def matrix_search(mat, n, key):
#     count = 0
#     for i in range(n):
#
#         if binary_search(mat[i], 0, n - 1, key):
#             count += 1
#     return count

def pretty_print(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end = " ")
        print()

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18],
    [4, 8, 12, 16, 20, 24], [5, 10, 15, 20, 25, 30], [6, 12, 18, 24, 30, 36]]
    N = 6
    pretty_print(matrix)
    print(matrix_search_staircase(matrix, N, N, 12))
