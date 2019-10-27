# program for searching over a 2-D matrix efficiently

# first idea is to apply binary search over the matrix in following fashion - firstly applying binary search over matrix rows and finding that row which contains that element
# and then again apply binary search over that found row

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


# main function
if __name__ == '__main__':
    p = list(map(int, input().strip().split()))
    m, n = p[0], p[1]
    l = list(map(int, input().strip().split()))
    mat = [l[i:i+m] for i in range(0, len(l), m)]
    #for i in range(0, len(l), m):
    #    mat.append(l[i:i + m])
    print(mat)
    K = int(input().strip())
    print(matrix_search_staircase(mat, n, m, K))
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
