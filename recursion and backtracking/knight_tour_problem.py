# Program for checking if the knight can move such that we can move to all the cells once on the board.
# We are required to basically create a tour of all the moves that knight makes if succesfull in covering the entire board.
# Note : we are prohibited to move outside the given board area and can't traverse the already traversed path again.
# -----------------------------------------------------------------------------------------------------------------------
# Naive solution will be to generate all the possible configuration for the board and check with the constraints and output the configuration which
# sets correctly but this gives exponential time complexity.
# Knight tour problem can be efficeintly solved by backtracking which is one of the approaches for solving it but due to very high time
# complexity (exponential) 8^(n * n), we are not able to run it in python most of the times.
# we will see here backtracking method but There are other methods also.
# BOARD SIZE : 8 * 8
# POSSIBLE KNIGHT MOVES IN ALL 8 DIRECTIONS :
#
#                        x,y
#                1,-2             2,1
#
#            -1,-2                    1,2
#
#                -2,-1             -1,2
#                        -2,1
#
#
# -----------------------------------------------------------------------------------------------------------
# # we store the positions by preprocessing the moves already known to us : 
# x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
# y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

def pretty_print(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end = " ")
        print()

def is_safe(board, curr_x, curr_y):
    if curr_x >= 0 and curr_x < 8 and curr_y >= 0 and curr_y < 8 and board[curr_x][curr_y] == -1:
        return True
    return False

def solve(board, curr_x, curr_y, x_moves, y_moves, pos):

    if pos == 64:
        return True

    for i in range(8):

        new_x = curr_x + x_moves[i]
        new_y = curr_y + y_moves[i]

        if is_safe(board, new_x, new_y):

            board[new_x][new_y] = pos
            if solve(board, new_x, new_y, x_moves, y_moves, pos + 1):
                return True

            board[new_x][new_y] = -1

    return False

if __name__ == '__main__':
    board = [[-1 for _ in range(8)] for _ in range(8)]
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1
    if not solve(board, 0, 0, x_moves, y_moves, pos):
        print("FALSE")
    else:
        print("TRUE")
