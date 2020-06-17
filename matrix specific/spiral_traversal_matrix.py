# Program for printing the matrix in spiral form , that means one by one square loops going one by one inside one of each other
# IDEA: logic is very simple, we need to set four boundaries so that we can print one by one all of the four sides of the square loop for each loops
# for that we set : k, l, m, n -> where k is used to set boundary for first row (from left to right),
# n is used to set last column boundary (from top to bottom), m is used to set boundary for last row (from right to left), l is used to set
# boundary for first column (from bottom to top)
# In this way we go from first row -> last column -> last row -> first column in clockwise direction (spiral way)
# Now, going for innner loops, from observation we can see that , k -> incremented, n-> decremented, m -> decremented, l-> incremented
# TIME : 0(M*N) WHERE M, N -> ROWS, COLUMNS AND SPACE : 0(1)

# function to traverse the matrix in spiral way
def matrix_traversal(mat):
    m, n = len(mat), len(mat[0])
    if m == 0 and n == 0:
        return []

    k, l = 0, 0

    # going over every element until one of the pointers exhaust
    while k < m and l < n:
        # printing first row
        for i in range(k, n, 1):
            print(mat[k][i], end = " ")

        k += 1

        # printing last column
        for i in range(k, m, 1):
            print(mat[i][n - 1], end = " ")

        n -= 1
        # printing last row
        if k < m:
            for i in range(n - 1, l - 1, -1):
                print(mat[m - 1][i], end = " ")

            m -= 1

        # printing first column
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(mat[i][l], end = " ")

            l += 1

# Anti-spiral traversal
# We can observe that anti-spiral print is exactly opposite print of spiral
# So, we can use stacks for storing all the elements and then, pop out one by one and print all the elements.


# driver function
if __name__ == '__main__':
    mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

    # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix_traversal(mat)
