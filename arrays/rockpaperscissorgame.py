import random
def computer_choose():
    '''
    parameters : None

    Returns:

    string containing name of choosen object

    '''
    return random.choice(['S', 'P', 'R'])

def player_display(player, option):
    print(f"{player} chose {option}")

def play_game():
    player1 = "You"
    player2 = "Computer"
    scores = {"P":0, "S":1, "R":2}
    leader_board = {player1:0, player2:0}
    for i in range(5):
        print("Your turn... ")
        player1_select = input("Press r for rock, p for paper and s for scissor : ").strip().upper()
        player_display(player1, player1_select)
        print("Compter taking it's turn  : ")
        player2_select = computer_choose()
        player_display(player2, player2_select)
        if scores[player1_select] < scores[player2_select]:
            print(f"{player2} won !")
            leader_board[player2] += 1
            print()
        elif scores[player1_select] > scores[player2_select]:
            print(f"{player1} won !")
            leader_board[player1] += 1
            print()
        else:
            print("Draw")
            print()

    print("Printing final leaderboard : ")
    for i, j in leader_board.items():
        print(i, j)
    if(leaderboard[player1] > leaderboard[player2]):
        print("congrats you won the game !")
    elif(leaderboard[player1] < leaderboard[player2]) :
        print("You lose the game !")
    else:
        print("Game is drawn !")

if __name__ == "__main__":
    print("WELCOME TO ROCK-PAPER-SCISSOR")
    user_input = input("Wanna play game : [Y/N] : ").strip().upper()
    if user_input == 'Y':
        print("Okay, taking you to game.....")
        play_game()
    elif user_input == 'N':
        print("Exiting.....")
    else:
        print("Your option is not understood. Exiting anyway...")
