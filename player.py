# program to determine who wins based on bunch of conditions (simple conditions to break tie on a card game)
def winning_player(winning_suit, suit1, number1, suit2, number2):
    if suit1 == winning_suit:
        if suit2 == winning_suit:
            if number1 > number2:
                return "Player 1 wins"
            elif number2 > number1:
                return "Player 2 wins"
            else:
                return "Draw"
        else:
            return "Player 1 wins"

    elif suit2 == winning_suit:
        return "Player 2 wins"
    else:
        if number1 > number2:
            return "Player 1 wins"
        elif number2 > number1:
            return "Player 2 wins"
        else:
            return "Draw"

if __name__ == '__main__':
    winning_suit = 'B'
    n_rounds = 5
    game_play = [['A', 2, 'B', 1], ['A', 7, 'D', 2], ['B', 5, 'D', 13], ['B', 3, 'B', 1], ['A', 12, 'C', 12]]
    for i in range(0, len(game_play)):
        print(winning_player(winning_suit, game_play[i][0], game_play[i][1], game_play[i][2], game_play[i][3]))
