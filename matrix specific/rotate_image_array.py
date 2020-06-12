# program to rotate the matrix in-place by 90 degrees anti-clockwise (or clockwise)
# IDEA: There are two algorithms (both efficient, taking similar asymtodic bounds but one (first one) having less computations than the other) and both have been discussed below (first one is more efficient as it takes less computations otherwise both takes same asymtodic bounds)

# function: move in cycles algorithm for rotating N * N array 90 degrees
def rotate_cycle(mat, n):
    # go for cycles
    for i in range(0, n//2):
        # for every cycle, move in groups of n one by one elementwise
        for j in range(i, n - i - 1):
            # store the current value of cell
            temp = mat[i][j]
            # move the rightmost to uppermost
            mat[i][j] = mat[j][n - 1 - i]
            # move the bottommost to rightmost
            mat[j][n - 1 - i] = mat[n - 1 - i][n - 1 - j]
            # move the leftmost to bottommost
            mat[n - 1 - i][n - 1 - j] = mat[n - 1 - j][i]
            # move the stored value to leftmost
            mat[n - 1 - j][i] = temp

# function : transpose the matrix
def transpose(mat, n):
    # traverse only the upper triangular half or lower triangular half of matrix and simply swap the elements
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# function : rotating matrix by first taking transposing and then reversing the rows (for anti-clockwise), otherwise reverse the columns (for clockwise)
def rotate_ac_array(mat, n):
    # transposing the array
    transpose(mat, n)
    # setting two pointers , one at first row and other at last row and move them until they collide
    i = 0
    j = n - 1
    # keep swapping the elements by keeping another pointer to first element of matrix of first column and then incrementing it one by one
    while(i < j):
        # swapping for every column for that two rows
        for k in range(n):
            mat[i][k], mat[j][k] = mat[j][k], mat[i][k]
        i += 1
        j -= 1
    display_matrix(mat, n)

# function : to display the matrix
def display_matrix(mat, n):
    print('modified matrix : ')
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

# main function
if __name__ == '__main__':
    n = int(input().strip())
    mat = []
    for i in range(n):
        l = list(map(int, input().strip().split()))
        mat.append(l)
    rotate_ac_array(mat, n)
