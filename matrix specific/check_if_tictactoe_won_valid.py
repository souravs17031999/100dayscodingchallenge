# Check if the given tic tac toe board is in won state (won the game)
# Assuming each cell on the board is " ", "X", "O"

# Design 3 * 3 board

# ----------------------------- Generate board -----------------------------------------------------------------------
def generate_board():
    board = []    
    for i in range(19683):
        c = i 
        temp = []
        for j in range(9):
            temp.append(int(c%3))
            c /= 3
        board.append(temp)    
    
    return board


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
            return True# Check if the given tic tac toe board is in won state (won the game)
# Assuming each cell on the board is " ", "X", "O"

# Design 3 * 3 board


# ---------------------------- Valid tic-tac-toe board -----------------------------------------------
def check_win_char(board, player):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True   
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True   
    
    if board[0][0] == board[1][1] == board[2][2]  == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False
        
        
def count_char_board(board):
    
    countO, countX = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                countX += 1
            
            elif board[i][j] == 'O':
                countO += 1
    
    return countO, countX
    
def check_valid_board(board):
    
    countO, countX = count_char_board(board)
    
    if countX == countO or countX == countO + 1:
        if check_win_char(board, 'O'):

            if check_win_char(board, 'X'):
                return False

            if countX == countO:
                return True

        if check_win_char(board, 'X') and countX != countO + 1:
            return False

        if not check_win_char(board, 'O'):
            return True

    return False

# ---------------------------- Check tic-tac-toe board winning state -----------------------------------

def convert_board_to_int(board):
    val = 0
    for i in range(3):
        for j in range(3):
            val = 3 * val + ord(board[i][j])
    
    return val

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

# ------------------ Generate tic-tac-toe ---------------------------------------------------------



if __name__ == '__main__':
    
    board = [['X', 'X', 'X'], 
             ['O', 'O', 'X'], 
             ['O', 'O', 'X']]
    
    print(has_won(board))
    print(convert_board_to_int(board))
    print(check_valid_board(board))
    
    
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
    
