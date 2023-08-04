"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to Brian's Guessing Game!")

    # Defining messages
    message_notint = "Not a number, try again."
    message_low = "Too small, try again :'("
    message_high = "Too big, try again :'("

    # Defining the first number
    while True:
        try:
            lowerBound = int(input("Enter a lower bound: "))
            break
        except ValueError:
            print(message_notint)

    # Defining the second number
    while True:
        try:
            upperBound = int(
                input("Now enter a number higher than " + str(lowerBound) + ": ")
            )
            if upperBound <= lowerBound:
                print(message_low)
            else:
                break
        except ValueError:
            print(message_notint)

    # Guessing game starts here
    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = int(input("Guess a number between " + str(lowerBound) + " and " + str(upperBound) + ": "))
            print(f"You guessed {guessedNumber},")
            if guessedNumber == actualNumber:
                print(f"You got it!! It was {actualNumber}")
                guessed = True
            elif guessedNumber < actualNumber:
                print(message_low)
            else:
                print(message_high)
        except ValueError:
            print(message_notint)
    return "You got it!"

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
