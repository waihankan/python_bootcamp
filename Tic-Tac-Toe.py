def startGame():
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
    
    
def player():
    while True:
        yield "X"
        yield "O"


def query_button(game, player):
    print_button()
    print("Button: ")
    press = int(input())
    x, y = button(press)
    if valid(game[x][y]):
        game[x][y] = player
    else: 
        print("Enter a valid button!")
        query_button(game, player)
    


def valid(position):
    return position == "_"


def print_button():
    print("Position")
    print("123")
    print("456")
    print("789")
    print()


def button(press):
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
    for i in game:
        for j in i:
            if j == "_":
                return False
    return True

def win(game):
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
