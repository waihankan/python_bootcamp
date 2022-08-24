def start_game():
    word = "b e a u t i f u l "
    blank = ""
    for i in range(len(word)//2):
        blank += "_ "
    life = hang()
    next(life)
    while blank != word:
        print()
        print(blank)
        print("Guess Letter: ")
        letter = input()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    blank = blank[:i] + letter + blank[i+1:]
        else:
            try:
                next(life)
            except StopIteration:
                return
    print("Word is: beautiful")
    print("Congratulation!!! :)")


def hang():
    print("  ____")
    print(" |   |")
    print(" |   |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("_____|__")
    yield None
    print("  ____")
    print(" |   |")
    print(" |   |")
    print(" O   |")
    print("     |")
    print("     |")
    print("     |")
    print("_____|__")
    yield None
    print("  ____")
    print(" |   |")
    print(" |   |")
    print(" O   |")
    print(" |   |")
    print("     |")
    print("     |")
    print("_____|__")
    yield None
    print("  ____")
    print(" |   |")
    print(" |   |")
    print(" O   |")
    print("/|   |")
    print("     |")
    print("     |")
    print("_____|__")
    yield None
    print("  ____")
    print(" |   |")
    print(" |   |")
    print(" O   |")
    print("/|\  |")
    print("     |")
    print("     |")
    print("_____|__")
    yield None
    print("  ____")
    print(" |   |")
    print(" |   |")
    print(" O   |")
    print("/|\  |")
    print("/    |")
    print("     |")
    print("_____|__")
    yield None
    print("  ____")
    print(" |   |")
    print(" |   |")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("     |")
    print("_____|__")
    print("You Lose :(")


start_game()