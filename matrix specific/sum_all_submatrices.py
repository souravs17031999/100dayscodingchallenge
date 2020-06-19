# Program for computing sum of all SUBMATRICES for a given matrix
# IDEA: So, Naive solution is to generate all possible SUBMATRICES and then sum them up which we have seen in already is done in 0(n^6)
# So, we get an idea about computing prefix sum for the original matrix then, we can apply the formula given that we have top left corner (i, j) and
# right most corner (x, y) => prefix[x][y] + prefix[i - 1][j - 1] - prefix[i - 1][y] - prefix[x][j - 1]
# where every prefix[x][y] stores sum from (0, 0) to (x, y) contained SUBMATRIX and this will be done in 0(n^4) as shown below with additonal 0(n^2) space.
# Now, here there is a problem for boundary values like wherever either of i, j is 0 due to negative indexing it starts taking values from back of matrix.
# So, we need to do some padding here of length = 1 on all sides, we will use here numpy function np.pad() for this and then apply the above formula.
# Let's now move onto most optimal solution.
# Observation : Any (i, j) element when contributing to the overall sum , gets added multiple times to multiple submatrices in the sense that
# that particular (i, j) element is actually involved in multiple submatrices.
# So, if we found out contribution of each (i, j) in the overall sum, then we wil not have to necessarily go to every submatrix to add that element.
# it is to be said as if we are reducing the computations of let's say (i, j)th element for a matrix and let's say that element is "a" so various cells in
# submatrix computation will contains this "a" and so if we are able to know that a will be eventually contributing (1/4)*(overall sum value) value in the
# overall sum, then that will be much better.
# Know it boils down to finding the contribution for each (i, j)th element which is simply mat[i][j] * no of submatrices it is part of
# so, from observations we can see top left area let's say "X" has some cells which has higher probability for becoming top left corners,
# and bottom right area let's say "Y" has higher probability for becoming bottom right corners which will be enveloping this element at (i, j)
# so, X will contain (i + 1)*(j + 1) elements and Y will contain (n - i)*(n - j) elements
# hence, total contribution for (i, j)th : (i + 1)*(j + 1)*(n - i)*(n - j) and sum will be updated as sum += mat[i][j]*S(i, j) where S(i, j) is contribution.
# Time : 0(N^2) with space : 0(1)

def compute_sum_1(mat):
    n = len(mat)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += mat[i][j] * (i + 1) * (j + 1) * (n - i) * (n - j)

    print(sum)



# less optimal Solution with time : 0(n^4) and space : 0(n^2)

import numpy as np
# IDEA: logic for generating prefix sum is simply, firstly we go for row wise and one by one add all the previous elements column wise
# Thereby generating one part of prefix MATRIX
# Now, we traverse column by column and then add the previous elements row wise, thereby generating other half in that same matrix by adding to previous
# half elements which gives us the overall prefix sum for the entire matrix

def compute_prefix(mat):
    n = len(mat)
    for i in range(0, n):
        for j in range(1, n):
            mat[i][j] += mat[i][j - 1]

    for i in range(1, n):
        for j in range(0, n):
            mat[i][j] += mat[i - 1][j]

    return mat

def print_matrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

def compute_sum_2(mat):
    sum = 0  # sum contains overall computed sum, initiliazing it to 0.
    # base case, if matrix is empty
    if not len(mat):
        return
    # p here is storing prefix sum
    p = compute_prefix(mat)
    # padding with lengh  = 1 on all sides => filling with 0
    p = np.pad(p, 1, 'constant')
    n = len(p)
    # two for loops for initiliazing left most corner
    for i in range(n):
        for j in range(n):
            # two for loops for initiliazing every possible right most corner for above generated left most corner points
            for x in range(i, n):
                for y in range(j, n):
                    # now applying this trick to extract the sum for this particular submatrix and this computation is 0(1) time.
                    sum += p[x][y] + p[i - 1][j - 1] - p[i - 1][y] - p[x][j - 1]

    # finally printing the computed overall sum
    print(sum)

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    compute_sum_1(mat)
