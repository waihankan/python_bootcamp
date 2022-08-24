#!/usr/bin/python
""" Tic-Tac-Toe Game

The game has a grid of 3x3 squares. Each player takes a turn to mark a square
with their symbol (X or O). The first player to get 3 of their symbols in a row
(up, down, across, or diagonally) is the winner. If all 9 squares are marked
and no player has 3 in a row, the game is considered as a draw.
"""

from tabnanny import check


def player():
    """ Generate the player 'X' and 'O' turn by turn """
    while True:
        yield "X"
        yield "O"


def query_button(game, player):
    """ Query the button position

    Arugments:
        game, player
    Returns:
        Position
        1 2 3
        4 5 6
        7 8 9
        
        Button:
    """

    print_button()
    press = int(input())
    check_validity(game, player, press)


def check_validity(game, player, press):
    """ Check if the button is valid (not occupied) """
    x, y = button(press)
    if game[x][y] == "_":
        game[x][y] = player
    else:
        print("Invalid move!")
        query_button(game, player)


def print_button():
    print("Position")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    print("\nButton: ")


def button(press):
    """ Return the position of the button """
    if press == 1: return 0, 0
    if press == 2: return 0, 1
    if press == 3: return 0, 2
    if press == 4: return 1, 0
    if press == 5: return 1, 1
    if press == 6: return 1, 2
    if press == 7: return 2, 0
    if press == 8: return 2, 1
    if press == 9: return 2, 2


def newGame():
    square = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
    ]
    printGame(square)
    return square


def printGame(game):
    for i in game:
        print(i)
    print()


def draw(game):
    """ Check if there is a draw """
    for i in game:
        for j in i:
            if j == "_":
                return False
    return True


def win(game):
    """ Check if there is a winner """
    # horizontal
    if game[0][0] == game[0][1] == game[0][2] != "_":
        return True
    if game[1][0] == game[1][1] == game[1][2] != "_":
        return True   
    if game[2][0] == game[2][1] == game[2][2] != "_":
        return True
    # vertical 
    if game[0][0] == game[1][0] == game[2][0] != "_":
        return True
    if game[0][1] == game[1][1] == game[2][1] != "_":
        return True
    if game[0][2] == game[1][2] == game[2][2] != "_":
        return True
    # diagonal
    if game[0][0] == game[1][1] == game[2][2] != "_":
        return True
    if game[0][2] == game[1][1] == game[2][0] != "_":
        return True
    return False

if __name__ == "__main__":
    game = newGame()
    turn = player()
    while True:
        now = next(turn)
        query_button(game, now)
        printGame(game)
        if win(game):
            print("Winner is: " + str(now))
            break
        if draw(game):
            print("No Winner")
            break
    