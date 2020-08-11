# The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
# For example, following is a solution for 4 Queen problem.
# The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other;
# thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the
# more general n queens problem of placing n non-attacking queens on an n×n chessboard, for which solutions exist for all natural
# numbers n with the exception of n = 2 and n = 3.
# -------------------------------------------------------------------------------------------------------
# As we can understand from problem statement, this a problem of searching for all possible options, therefore it's an exhaustive search
# problem, so we will try all possible solutions using recursion and backtracking solution for it.
# --------------------------------------------------------------------------------------------------------
# Below solution is shown for any valid solution, but we can slightly modify it to print all the solutions for it.
# in the base base, wheneevr we reach there, we will print the current solutiona nd move on by returning true.
# Now, catching part function value will be returned to a var which will be boolean, true or false (initially in every call it is false)
# if solution is valid, then it will recurse for more, otherwise it will be false.
# Modification has been shown using * in comments.
# ---------------------------------------------------------------------------------------------------------

N = 4

# since , we are filling col by col from 0 to col - 1,
# then we can check for left side for attacking queens

def print_board(board):

    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def is_safe(board, row, col):

    # check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check for upper left diagonal elements
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check for lower left diagonal elements
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_board(board, col):

    # if all the queens are placed      # * If all solutions : call here print_board() every time we reach here
    if col >= N:
        return True
    # *  we can keep here res = False
    for i in range(N):
        # if placemnt at this position is valid, then we can place here.
        if is_safe(board, i, col):
            # placing the queen
            board[i][col] = 1
            # recur for other queens
            if solve_board(board, col + 1):   # * if all solutions, then res = solve_board(board, col + 1) or res
                return True

            # if placing queen in board[i][col] doesn't lead to a solution
            board[i][col] = 0

    # after trying all the possibilities, if we come here, then there is no solution
    # so, we return False
    return False   # * if all solutions, then return res 


def solveNQ():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]

    if solve_board(board, 0) == False:
        print ("Solution does not exist")
        return False

    print_board(board)
    return True

solveNQ()
