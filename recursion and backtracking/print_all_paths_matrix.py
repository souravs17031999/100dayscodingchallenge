# pROGRAM FOR PRINITNG ALL PATHS FROM A GIVEN STARTING CORNER (0, 0) TO END CORNER RIGHTMOST OF A matrix

def PrintAllPath(mat, hash, i, j, res=[]):

    # print("current hash :")
    # pretty_print(hash)
    # print(f"current result : {res}\n")
    rows, cols = len(mat), len(mat[0])
    # base case
    if i < 0 or i >= rows or j < 0 or j >= cols or hash[i][j] == 1:
        return

    # we know we have reached the destination
    if i == rows - 1 and j == cols - 1:

        res.append(mat[i][j])
        # print the elements
        for i in range(len(res)):
            print(res[i], end = " ")
        print()
        return

    hash[i][j] = 1
    res.append(mat[i][j])

    PrintAllPath(mat, hash, i, j + 1, res)
    PrintAllPath(mat, hash, i + 1, j, res)
    PrintAllPath(mat, hash, i - 1, j, res)
    PrintAllPath(mat, hash, i, j - 1, res)

    res.pop()
    hash[i][j] = 0


def pretty_print(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = " ")
        print()

if __name__ == '__main__':
    mat = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    rows, cols = len(mat), len(mat[0])

    hash = [[0] * cols for _ in range(rows)]
    PrintAllPath(mat, hash, 0, 0)
