# Program to solve sudoku using backtracking algorithm which is usually what comes intutitive.
# This problme is similar to N-queen's problem where we try to validate a part of overall solution and then if not validated,
# then we backtrack and recurse for other options, in this way we will be able to fill all the correct positions on the board.
# It is guaranteed that board size will be N * N, here we assume it to be 9 * 9 and squares to be of 3 * 3.
# Now, this ensures we have 9 possibilities to be filled for every position available, hence time : 9^(n * n) and space : N * N
# Not all sudoku configurations are solvable !

def is_used_row(mat, row, num):
    for col in range(len(mat)):
        if mat[row][col] == num:
            return True
    return False

def is_used_col(mat, col, num):
    for row in range(len(mat)):
        if mat[row][col] == num:
            return True
    return False

def is_used_box(mat, row, col, num):
    for i in range(3):
        for j in range(3):
            if mat[i + row][j + col] == num:
                return True
    return False

def is_valid(mat, row, col, num):

    return not is_used_row(mat, row, num) and not is_used_col(mat, col, num) and not is_used_box(mat, row - row % 3, col - col % 3, num)


def find_unassigned_location(mat, l):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                l[0], l[1] = i, j
                return True
    return False


def solve(mat):

    l = [0, 0]

    if not find_unassigned_location(mat, l):
        return True

    row, col = l[0], l[1]

    for num in range(1, 10):

        if is_valid(mat, row, col, num):
            mat[row][col] = num

            if solve(mat):
                return True

            mat[row][col] = 0

    return False

def pretty_print(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end = " ")
        print()

if __name__ == '__main__':

    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
    	[5, 2, 0, 0, 0, 0, 0, 0, 0],
    	[0, 8, 7, 0, 0, 0, 0, 3, 1],
    	[0, 0, 3, 0, 1, 0, 0, 8, 0],
    	[9, 0, 0, 8, 6, 3, 0, 0, 5],
    	[0, 5, 0, 0, 9, 0, 6, 0, 0],
    	[1, 3, 0, 0, 0, 0, 2, 5, 0],
    	[0, 0, 0, 0, 0, 0, 0, 7, 4],
    	[0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if(solve(grid)):
        pretty_print(grid)
    else:
        print("No solution exists")
