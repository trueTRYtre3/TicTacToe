import random
from typing import List, Tuple


def create_pieces() -> List[str]:
    places = []
    for i in range(9):
        places.append(str(i))
    return places


def game_board(board: List[str]) -> None:
    """
    Tic Tac Toe game board creation
    """
    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")


def play_again() -> str:
    while True:
        try:
            question = input("Would you like to play again (y/n): ")
            if question.lower() == 'y':
                return 'y'
            elif question.lower() == 'n':
                return 'n'
            raise ValueError()
        except ValueError:
            print('Invalid input. Try again.')


def choose_letter(letter: str) -> str:
    if letter is None:
        while True:
            try:
                question = input("Choose a letter (X or O): ")
                if question.upper() == 'X':
                    return 'X'
                elif question.upper() == 'O':
                    return 'O'
            except ValueError:
                print("Choose from the given options")
            else:
                print("Choose from the given options")
    elif letter == 'X':
        return 'O'
    return 'X'


def place_board(board: List[str], letter: str) -> List[str]:
    """
    Inputs character letter into the board and updates the pre-made game list
    """
    while True:
        try:
            numb = int(input(f"Player {letter}: Enter a number between 0-8: "))
            if (board[numb] != 'X' and board[numb] != 'O') and (8 >= numb >= 0):
                board[numb] = letter
                break
        except ValueError:
            print("Enter an integer.")
        except IndexError:
            print("Enter a number within the given parameters")
        else:
            print("Please enter another number.")
    return board


def place_ai(board: List[str]) -> List[str]:
    random_place = random.randint(0, 8)
    if isinstance(board[random_place], int):
        board[random_place] = 'O'
    return board


def win_conditions(board: List[str], letter: str) -> int:
    """
    Checks if a player won the game
    """
    # Check rows
    for count in range(0, 7, 3):
        if board[count] == board[count + 1] == board[count + 2] == letter:
            return 1

    # Check columns
    for count in range(0, 3):
        if board[count] == board[count + 3] == board[count + 6] == letter:
            return 1

    # Check diagonals
    for count in range(0, 3, 2):
        if count == 0:
            if board[count] == board[count + 4] == board[count + 8] == letter:
                return 1
        elif count == 2:
            if board[count] == board[count + 2] == board[count + 4] == letter:
                return 1

    return 0


def display_score(letterX: int, letterO: int, char_letter: str = None) -> Tuple[int, int]:
    if char_letter == 'X':
        letterX += 1
    elif char_letter == 'O':
        letterO += 1
    print(f"\tPlayer X has a score of {letterX}\n\tPlayer O has a score of {letterO}")
    return letterX, letterO


def game_over() -> Tuple[str, List[str]]:
    question = play_again()
    places = create_pieces()
    return question, places


def game() -> None:
    """
    Initialize functions to play game
    """
    places = create_pieces()

    count = 0
    letter_X = 0
    letter_O = 0
    letter = None

    question = input("Would you like to play Tic-Tac-Toe (y/n): ")

    while question.lower() == 'y':
        letter = choose_letter(letter)
        game_board(places)
        place_board(places, letter)

        if count <= 8:
            winner = win_conditions(places, letter)
            if winner == 1:
                game_board(places)
                print(f'\n\tPlayer {letter} wins!')
                letter_X, letter_O = display_score(letter_X, letter_O, letter)
                count = 0
                question, places = game_over()
        else:
            letter_X, letter_O = display_score(letter_X, letter_O)
            count = 0
            question, places = game_over()
        count += 1


game()
