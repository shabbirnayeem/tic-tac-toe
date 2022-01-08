import os
import time
import random
from art import tictactoe_art
from termcolor import colored
"""

Create the display window for our game.
Draw the grid on the canvas where we will play Tic Tac Toe.
Draw the status bar below the canvas to show which player's turn is it and who wins the game.
When someone wins the game or the game is a draw then we reset the game.

"""

# building the grid
# TODO: Draw the grid on the canvas where we will play Tic Tac Toe.
theBoard = {'7': '', '8': '', '9': '',
            '4': '', '5': '', '6': '',
            '1': '', '2': '', '3': ''}
p1_score = 0
p2_score = 0


def board():
    """
    Draw the Board for the Game.
    """
    print(theBoard['7'] + '   |   ' + theBoard['8'] + '    |  ' + theBoard['9'])
    print('_______________')
    print(theBoard['4'] + '   |   ' + theBoard['5'] + '    |  ' + theBoard['6'])
    print('_______________')
    print(theBoard['1'] + '   |   ' + theBoard['2'] + '    |  ' + theBoard['3'])


def win():
    """
    Match the winning condition and return true if a condition id matched.
    """
    # horizontal winning condition
    if theBoard['7'] == theBoard['8'] and theBoard['7'] == theBoard['9'] and theBoard['7'] != '':
        return True
    elif theBoard['4'] == theBoard['5'] and theBoard['4'] == theBoard['6'] and theBoard['4'] != '':
        return True
    elif theBoard['1'] == theBoard['2'] and theBoard['2'] == theBoard['3'] and theBoard['1'] != '':
        return True
    # vertical winning condition
    elif theBoard['7'] == theBoard['4'] and theBoard['4'] == theBoard['1'] and theBoard['7'] != '':
        return True
    elif theBoard['8'] == theBoard['5'] and theBoard['5'] == theBoard['2'] and theBoard['8'] != '':
        return True
    elif theBoard['9'] == theBoard['6'] and theBoard['6'] == theBoard['3'] and theBoard['9'] != '':
        return True
    # diagonal
    elif theBoard['7'] == theBoard['5'] and theBoard['5'] == theBoard['3'] and theBoard['7'] != '':
        return True
    elif theBoard['9'] == theBoard['5'] and theBoard['5'] == theBoard['1'] and theBoard['9'] != '':
        return True


def tie():
    count = 0
    for num in range(1, 10):
        if theBoard[str(num)] != '':
            count += 1
    if count == 9:
        print("Its a TIE!")
        return True
    else:
        return False


def clear_the_board():
    """
    Clear the board after the game finishes.
    """
    for num in range(1, 10):
        if theBoard[str(num)] != '':
            theBoard[str(num)] = ''


# TODO: Create a AI player
# TODO: Make the AI player smarter
def ai_player():
    """
    Returns random number between 1, 9.
    """
    random_num = random.randrange(1, 10)
    return str(random_num)


# TODO: Create Score Card to Keep Score for each Player
def score_card(score=0):
    final = 0
    final += score
    return final


def game_setup():
    """
    Player choose X, O to play the game.
    """
    not_x_o = True
    while not_x_o:
        user_input = input("Player One Choose your weapons: [X/O] ").upper()
        if user_input == 'X':
            board()
            not_x_o = False
            player1 = user_input
            player2 = 'O'
            print(f"Player One: {player1}")
            print(f"Player Two: {player2}")
            return player1, player2
        elif user_input == 'O':
            board()
            not_x_o = False
            player1 = user_input
            player2 = 'X'
            print(f"Player One: {player1}")
            print(f"Player Two: {player2}")
            return player1, player2


def multi_player():
    global p1_score
    global p2_score
    p1, p2 = game_setup()
    no_winner = True
    while no_winner:
        try:
            player1_move = input('Player One your turn: ')
            if theBoard[player1_move] == '':
                theBoard[player1_move] = p1
                board()
                if win():
                    print('Game Over\nPlayer One Wins!')
                    clear_the_board()
                    no_winner = False
                    p1_score += 1
                    break
                elif tie():
                    clear_the_board()
                    no_winner = False
                    break
                else:
                    correct = False
                    while not correct:
                        try:
                            player2_move = input('Player Two your turn: ')
                            if theBoard[player2_move] == '':
                                theBoard[player2_move] = p2
                                correct = True
                                board()
                            elif theBoard[player2_move] != '':
                                print('Try again')
                                board()
                        except KeyError:
                            print("Use the Number Pad on your keyboard")
                    if win():
                        print('Game Over\nPlayer Two Wins!')
                        clear_the_board()
                        no_winner = False
                        p2_score += 1
                        break
                    elif tie():
                        clear_the_board()
                        no_winner = False
                        break

            elif theBoard[player1_move] != '':
                print('Try again')
                board()
        except KeyError:
            print("Use the Number Pad on your keyboard")


def single_player():
    global p1_score
    global p2_score
    p1, p2 = game_setup()
    no_winner = True
    while no_winner:
        player1_move = input('Player One your turn: ')

        try:
            if theBoard[player1_move] == '':
                theBoard[player1_move] = p1
                board()
                if win():
                    print('Game Over\nPlayer One Wins!')
                    clear_the_board()
                    no_winner = False
                    p1_score += 1
                    break
                elif tie():
                    clear_the_board()
                    no_winner = False
                    break
                else:
                    correct = False
                    while not correct:
                        print('Computers Turn:')
                        time.sleep(1)
                        player2_move = ai_player()
                        if theBoard[player2_move] == '':
                            theBoard[player2_move] = p2
                            correct = True
                            board()
                        elif theBoard[player2_move] != '':
                            print('Try again')
                            board()
                    if win():
                        print('Game Over\nPlayer Two Wins!')
                        clear_the_board()
                        no_winner = False
                        p2_score += 1
                        break
                    elif tie():
                        clear_the_board()
                        no_winner = False
                        break

            elif theBoard[player1_move] != '':
                print('Try again')
                board()
        except KeyError:
            print("Use the Number Pad on your keyboard")


print(tictactoe_art())
time.sleep(2)
os.system('cls')
print('Start the Game')
not_correct_answer = True
while not_correct_answer:
    choice = input("Single / multi player: [S/M] ").upper()
    if choice == "M":
        multi_player()
        # Getting out of the outer while loop
        not_correct_answer = False

        # creating another while loop which keep looping if the player wants to continue playing
        # setting end to True will end the loop
        end = False
        while not end:
            user_choice = input("Do you want to play again? [Y/N]: ").upper()
            if user_choice == 'Y':
                os.system('cls')
                multi_player()
            else:
                print(f"Final Score:\nPlayer One Score: {p1_score}\nPlayer Two score: {p2_score}")
                time.sleep(5)
                end = True
                break
    elif choice == "S":
        single_player()
        # Getting out of the outer while loop
        not_correct_answer = False

        # creating another while loop which keep looping if the player wants to continue playing
        # This will keep asking "Do you want to play again? [Y/N]"
        # setting end to True will end the loop
        end = False
        while not end:
            user_choice = input("Do you want to play again? [Y/N]: ").upper()
            if user_choice == 'Y':
                os.system('cls')
                single_player()
            else:
                print(f"Final Score:\nPlayer One Score: {p1_score}\nPlayer Two score: {p2_score}")
                time.sleep(5)
                end = True
                break
    else:
        print("Did not select the correct option: Try Again!")






