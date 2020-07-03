# Program to naively multiply two matrices
# TIME : 0(M*N*K) AND SPACE : 0(K^2) , WHERE M , N , K ARE DIMENSIONS OF FIRST MAT, SECOND MAT AND RESULTANT PRODUCT MATRIX RESPECTIVELY.
# WE CAN IMPROVE THIS BY USING DIVIDE AND CONQUER APPROACH BY USING STRASEEN ALGORITHM OR KARATSUBA ALGORITHM (DISCUSSED IN DAC SECTION).

def product(mat1, mat2):
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    if cols1 != rows1:
        raise Exception (f"Dimensions ERROR , mat1 : [{rows1} x {cols1}] mat2 : [{rows2} x {cols2}]")

    res = [[0] * cols2 for _ in range(rows1)]
    print(res)
    for i in range(rows1):
        for j in range(cols2):
            for k in range(len(res)):
                res[i][j] += mat1[i][k] * mat2[k][j]

    print(res)


# DRIVER TEST FUNCTION
if __name__ == '__main__':

    M = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

    N = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

    product(M, N)
