# Program to check if given sudoku configuration is valid or not.
# We need to simply check for the filled values in the configuration and check all the main 3 rules
# that a filled number should not repeat in the its respective row, col and in the 3 * 3 box.

def is_valid_row(mat, row):
    visited = set()
    for col in range(len(mat)):

        if mat[row][col] in visited:
            return False

        if mat[row][col] != '.':
            visited.add(mat[row][col])
    return True

def is_valid_col(mat, col):
    visited = set()
    for row in range(len(mat)):

        if mat[row][col] in visited:
            return False

        if mat[row][col] != '.':
            visited.add(mat[row][col])
    return True

def is_valid_box(mat, row, col):
    visited = set()
    for i in range(3):
        for j in range(3):
            if mat[i + row][j + col] in visited:
                return False

            if mat[i + row][j + col] != '.':
                visited.add(mat[i + row][j + col])
    return True

def is_valid(mat, row, col):

    return is_valid_row(mat, row) and is_valid_col(mat, col) and is_valid_box(mat, row - row % 3, col - col % 3)

if __name__ == '__main__':
    board = [[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],
             [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],
             [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],
             [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],
             [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],
             [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],
             [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],
             [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],
             [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]]

    for i in range(len(board)):
        for j in range(len(board)):
            if not is_valid(board, i, j):
                print("NOT VALID !")

    print("VALID")            
