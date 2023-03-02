# https://adriann.github.io/programming_problems.html
"""
GAME: GUESSING GAME
Input: user picks a number 
Output: guess again higher/lower | hooray you guessed right 
"""
#  generate random number [1:100] that the suer will guess
import random


def game(secret_number, res=""):

    if res:
        print("res", res)

    # get the users guess
    guess = int(input())

    #  pass case
    if guess == SECRET_NUM:
        return "hooray you guessed right"

    # ask again cases
    if guess > SECRET_NUM:
        res = "guess lower"
        return game(secret_number, res)

    if guess < SECRET_NUM:
        res = "guess higher"
        return game(secret_number, res)


def game2(secret_number):
    print(secret_number)
    guess = int(input())
    lives = 5

    while guess != secret_number:
        if lives == 1:
            return "Your a loser"

        if guess > secret_number:
            res = "guess lower"
        if guess < secret_number:
            res = "guess higher"
        print(res)

        lives = lives - 1
        print(f"You have  {lives} <3 left")
        guess = int(input())

    return "hooray you guessed right"


if __name__ == "__main__":

    SECRET_NUM = random.randint(1, 100)
    # winner = game1(SECRET_NUM)
    # print("WINNER", winner)

    ans = game2(SECRET_NUM)
    print(ans)
