# Check if the given tic tac toe board is in won state (won the game)
# Assuming each cell on the board is " ", "X", "O"

# Design 3 * 3 board

def equal_pisces(p1, p2, p3):
    if p1 == ' ':
        return False 
    
    return p1 == p2 == p3

def has_won(board):
    
    # check for rows and columns
    for i in range(3):
        # check rows 
        if equal_pisces(board[i][0], board[i][1], board[i][2]):
            return True
        # check cols
        if equal_pisces(board[0][i], board[1][i], board[2][i]):
            return True
    
    # check diagonals
    if equal_pisces(board[0][0], board[1][1], board[2][2]):
        return True
    
    if equal_pisces(board[0][2], board[1][1], board[2][0]):
        return True
    
    return False

if __name__ == '__main__':
    board = [['X', 'X', 'O'], 
             ['O', 'X', 'X'], 
             ['O', 'O', 'O']]
    
    print(has_won(board))
    
