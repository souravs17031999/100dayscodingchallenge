# Program for computing the maximum sum for row and column wise sorted matrix efficiently.
# IDEA: Naive solution is to iterate for every submatrix and then calculate the maxiumum from every traversal for submatrix
# and already we have seen it can be done in 0(N^4).
# Optimal solution is to think about the sorted thing and observing it will yield the idea that all the majority (bigger elements) will be on the
# rightmost bottom corner elements and all the least valued elements will be on the left most side of the matrix.
# So, the high probability for finding the maxiumum sum will be on the right most corner elements.
# Hence, our problem boils down to finding the range of that maxium submatrix from rightmost bottom side traversal.
# but we need it to do efficiently, hence, we can precompute a suffix-array which will contain sum from (n-1, m-1)th element till (i, j) for (i, j)th element.
# This way, while traversing the suffix array for the matrix, at any point (i, j)th , that value stores the sum from very last element (n-1, m-1)th element.
# and hence if we keep track of max_sum while traversing just this suffix array, we will be able to compute the max_sum for every submatrix.
# TIME : 0(N^2) , SPACE : 0(N^2)

import sys

# PRETTY PRINTING
def pretty_print(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

# function for computing suffix of the array
def compute_suffix(mat):
    n = len(mat)
    # first we go for column wise addition
    for i in range(n - 1, -1, -1):
        for j in range(n - 2, -1, -1):
            mat[i][j] += mat[i][j + 1]

    # now we go for row wise addition
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            mat[i][j] += mat[i + 1][j]

    return mat


# function for computing max_sum for sorted matrix
def compute_sum(mat):
    sum = 0
    # initiliazing max_sum to minimum possible value
    max_sum = - sys.maxsize - 1
    # base case
    if not len(mat):
        return
    # p here is storing suffix sum from (n-1, m-1)th element to (i, j)th element
    p = compute_suffix(mat)
    pretty_print(p)
    n = len(p)
    # traversing the suffix array
    for i in range(n):
        for j in range(n):
            # updating the max_sum obtained so far
            max_sum = max(max_sum, p[i][j])

    return max_sum


if __name__ == '__main__':
    mat = [[-5, -4, -1], [-3, 2, 4], [2, 5, 8]]
    print(compute_sum(mat))
