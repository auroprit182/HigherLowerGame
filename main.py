# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import random
import subprocess

from art import logo, vs
from gamedata import data


def clear():
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120


def rand_number():
    return random.randint(0, len(data) - 1)


def compare_result(accountA, accountB, user_selection):
    if data[accountA]['follower_count'] > data[accountB]['follower_count']:
        return 'a'
    else:
        return 'b'


def user_choice():
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return choice


def play_game():
    score = 0
    result = None
    user_answer = None

    randomA = rand_number()
    randomB = rand_number()
    while result == user_answer:

        if randomA != randomB:
            clear()
            print(logo)
            if score != 0:
                print(f"You're right! Current score: {score}.")
            print(f"Compare A: {data[randomA]['name']}, {data[randomA]['description']}, {data[randomA]['country']}. ")
            print(vs)
            print(f"Against B: {data[randomB]['name']}, {data[randomB]['description']}, {data[randomB]['country']}.")
            user_answer = user_choice()
            if user_answer == 'a' or user_answer == 'b':
                result = compare_result(randomA, randomB, user_answer)
                if result == user_answer:
                    score += 1
                    randomA = randomB
                    randomB = rand_number()

            else:
                clear()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
        else:
            randomB = rand_number()

    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    play_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
