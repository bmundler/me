# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0

    # print("\nWelcome to Brian's First Algorithm!")

    # Defining messages
    message_notint = "Not a number, try again."
    message_low = "Too small, try again :'("
    message_high = "Too big, try again :'("

    # # Defining the first number
    # while True:
    #     try:
    #         low = int(input("Enter a lower bound: "))
    #         break
    #     except ValueError:
    #         print(message_notint)

    # # Defining the second number
    # while True:
    #     try:
    #         high = int(
    #             input("Now enter a number higher than " + str(low) + ": ")
    #         )
    #         if high <= low:
    #             print(message_low)
    #         else:
    #             break
    #     except ValueError:
    #         print(message_notint)

    # Binary search starts here
    while True:
        guess = int((high - low) / 2 + low)
        # print(f"You guessed {guess},")
        if guess == actual_number:
            print(
                f"You got it!! It was {guess}. It took you {tries} tries to guess it."
            )
            return {"guess": guess, "tries": tries}
        elif guess < actual_number:
            # print(message_low)
            low = guess + 1
        else:
            # print(message_high)
            high = guess - 1
        tries = tries + 1


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
