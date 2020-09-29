# Program for applying minimax algorithm to tic_tac_toe game.
# Here, we have 9 possible moves from first state which first player can make, then again 8 possible configurations for next player (second player), and so on alternate moves.
# We need to simulate the minimax algorithm.
# So, earlier we have implemented minimax for just two child nodes (two moves) but here there are more than that moves, so everytime we will make a move for a empty cell, 
# then evaulate its score, and update the best we can find there, we undo the ealier made move to trigger next possible path from there.

import sys 
def equal_pisces(p1, p2, p3):
    if p1 == ' ':
        return False 
    
    return p1 == p2 == p3

def evaluate(board):
    
    for i in range(3):
        
        if equal_pisces(board[i][0], board[i][1], board[i][2]):
            if board[i][0] == 'X':
                return 10
            elif board[i][0] == 'O':
                return -10
    
    for i in range(3):
        
        if equal_pisces(board[i][0], board[i][1], board[i][2]):
            if board[0][i] == 'X':
                return 10
            elif board[0][i] == 'O':
                return -10

    if equal_pisces(board[0][0], board[1][1], board[2][2]):
        if board[0][0] == 'X':
                return 10
        elif board[0][0] == 'O':
            return -10
    
    if equal_pisces(board[0][2], board[1][1], board[2][0]):
        if board[0][2] == 'X':
                return 10
        elif board[0][2] == 'O':
            return -10
    
    return 0

def is_move_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    
    return False 

def minimax(board, depth, isMaximizer):
    
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_move_left(board):
        return 0

    if isMaximizer:
        best_val = -sys.maxsize-1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best_val = max(best_val, minimax(board, depth+1, not isMaximizer))
                    board[i][j] = ' '

        return best_val

    else:
        best_val = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best_val = min(best_val, minimax(board, depth+1, not isMaximizer))
                    board[i][j] = ' '

        return best_val
        

# MAIN DRIVER FUNCTION
if __name__ == '__main__':
    
    board = [['X', ' ', 'O'], 
             [' ', 'O', 'O'], 
             [' ', ' ', '']]
    
    print(evaluate(board))
    print(minimax(board, 0, False))
    
    
