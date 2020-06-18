# IDEAS TO GENERATE ALL POSSIBLE SUBSETS (SUBMATRICES) FOR A GIVEN MATRIX
# More general way = brute force
# TIME : 0(N^6)
# IDEA: logic is to have a way to fix one leftmost top point of the matrix, then fix bottom most right point of the matrix ,
# and then any possible unique rectangular matrix can be drawn (extracted) from these two matrices
# so, two for loops for traversing over every possible element and assuming it to be the topmost left point  ,
# then two for loops for going from just that above cooordinates to last dimension possible which will give all sets of rightmost cooordinates
# In this way we will able to create a tuple (left_x, left_y, right_x, right_y)
# Now, we need two more extra loops for traversing from left_x, left_y to right_x, right_y
# Below shown is naive way
# NOTE : defaultdict is just used for printing it afterwards conveniently otherwise, it doesn't have to do anything in the implementation logic

from collections import defaultdict as dd
d = dd(list)
def generate_submatrix1(mat):
    n = len(mat)
    for left_x in range(n):
        for left_y in range(n):
            for right_x in range(left_x, n):
                for right_y in range(left_y, n):
                    temp = []
                    for i in range(left_x, right_x + 1):
                        for j in range(left_y, right_y + 1):
                            temp.append(mat[i][j])
                    temp_len = len(temp)
                    d[temp_len].append(temp)

    # printing every sub matrix
    for i, j in d.items():
        print(f"{i} : {j}")


# Pythonic way to extract specific part of matrix
def generate_submatrix2(mat, row_s, column_s, row_e, column_e):
    print([x[column_s:column_e + 1] for x in mat[row_s:row_e + 1]])

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(mat)
    generate_submatrix1(mat)
