# Program for optimizing the product of two matrices using strassen algorithm in 0(n^2.8074) which is better than 0(n^3)
# Logic is to use some tricky equations which are useful to compute the products in 7 recursive calls instead of 8 recursive calls (in traditional method)
# for every 2*2 matrices, we compute the product using 7 recursive calls.
# For every n * n matrices, we divide n/2 * n/2 sub matrices, using divide and conquer approach.
# Base case is when we only have 1 element, then we return product of that two elements.

import numpy as np

# splitting the matrix into quadrants (breaking down 2*2 matrix into one element atmost product wise)
def split(mat):

    row, col = mat.shape
    row2, col2 = row//2, col//2
    return mat[:row2, :col2], mat[:row2, col2:], mat[row2:, :col2], mat[row2:, col2:]

# function for strassen algorithm
def strassen(x, y):

    if len (x) == 1:
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively
    # untill the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    # now finally, computing the values for resultant matrices
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c

# driver test function
if __name__ == '__main__':
        M = np.array(
        [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
        )

        N = np.array(
        [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
        )
        if not M.shape[0] & 1 and not M.shape[1] & 1:
            print(strassen(M, N))
        else:
            # padding needs to be done for making it to nearest power of 2.
