# program for searching over a sorted 2-D matrix efficiently

# first idea is to apply binary search over the matrix in following fashion - firstly applying binary search over matrix rows and finding that row which contains that element
# and then again apply binary search over that found row

import random
# function for binary search for a single array (a particular row of matrix)
def binary_search(l, start, end, key):
    while(start <= end):
        middle = start + (end - start) // 2
        if l[middle] < key:
            start = middle + 1
        elif l[middle] > key:
            end = middle - 1
        else:
            return 1
    return 0

# function for binary search over matrix
def matrix_bin_search(l, m, n, k):
    '''
    l : matrix
    m : rows
    n : columns
    k : element to be found
    '''
    # starting at first element
    start = 0
    # ending at last element
    end = m - 1
    # going for binary search
    while(start <= end):
        middle = start + (end - start) // 2
        # checking if the element belongs to this row
        if k >= l[middle][0] and k <= l[middle][n-1]:
            # if the element belongs to the row , then simply apply binary search and check if that exists or not
            return (binary_search(l[middle], 0, n - 1, k))

        # otherwise search in upper/lower rows depending on the conditions
        if k < l[middle][0]:
            end = middle - 1
        else:
            start = middle + 1
    return 0

# second logic - stair case algorithm (most efficient , takes 0(n) time for n*n otherwise 0(m + n ))
# idea is here that if matrix is sorted both row wise and column wise then, we can just simply start from rightmost upper corner or leftmost bottom corner and then simply check whether the value to be found is greater or not if greater then go to next row eliminating that entire row and similarly if that is smaller then move to previous column thereby eliminating the need for searching that entire column. This way we keep on moving , mostly in zig zag fashion by changing row and columns and finally we found (if it exists) - staircase algorithm
def matrix_search_staircase(l, m, n, k):
    # starting from right most upper corner
    i = 0
    j = n - 1
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
            return 1
    # return false , not found
    return 0


# Note : NOW, THERE ARE TWO VARIANTS FOR THE PROBLEM, once in which row and col wise sorted but it is not guaranteed, that rightmost
# element is greater than leftmost of next column.
# If that is the case, then we can surelty optimize for the linear time algo (above algo) at the best.
# Now, If it is guaranteed that rightmost of every row is greater than leftmost of its following column, that means
# overall matrix can mentally thought to be a single sorted 1-d array and if we can get actual element through a mapping
# without actually converting 2-d array into 1-d array, then we can do this work in logarithmic time and no extra space.
# Since, total number of elements will be m*n for our "mental 1-d array",
# we can actually map using (i, j) = ((indexin1-d // cols), (indexin1-d % cols)) which then can be used to apply binary_search.
# TIME : 0(lg(M*N)) which is most optimized for this type of variant.

def mat_bin_search(mat, m, n, key):
    start, end = 0, m * n - 1

    while start <= end:
        mid = (start + end) // 2
        row, col = mid // n, mid % n
        if mat[row][col] == key:
            return 1
        elif mat[row][col] < key:
            start = mid + 1
        else:
            end = mid - 1

    return 0


# main function
if __name__ == '__main__':
    matrix = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    M, N, K = 3, 3, 43
    print(mat_bin_search(matrix, M, N, K))
    # 3 3
    #3 30 38 44 52 54 57 60 69
    # 30
    # output : 1
    # 90
    # output : 0

'''
assert matrix_bin_search([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 3, 4, 1) == 1
assert matrix_bin_search([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 3, 4, 90) == 0
assert matrix_bin_search([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 3, 4, 0) == 0
assert matrix_bin_search([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 3, 4, 0) == 0
'''
