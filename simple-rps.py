# Project: Rock, Paper, Scizors!
import random


def play():
    user = input("'r' - for rock \n'p' - for paper \n's' - scissiors \nChoice:  ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a Tie~"
    if is_win(user, computer):
        return "You Won!"

    return "Your a loser!"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
