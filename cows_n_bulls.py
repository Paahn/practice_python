# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:
# Randomly generate a 4-digit number.
# Ask the user to guess a number. If the number is in the
# randomly generated number add a "cow". Every time the user
# makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes
# throughout the game and tell the user at the end.
import random

j = random.sample(range(10), 4)
cows = 0
bulls = 0
number_of_guesses = 0

def user_guess():
    try:
        guess = int(input("Guess a number: "))
        while cows != 4:
            if guess in j:
                correct()
                user_guess()
            else:
                incorrect()
                user_guess()
    except ValueError:
        print("Oops! try again")


def correct():
    global cows
    global number_of_guesses
    print("You guessed correctly")
    cows += 1
    print("You have {} cows and {} bulls.".format(cows, bulls))
    number_of_guesses += 1
    if cows == 4:
        print(j)
        exit("You win! It took you {} guesses.".format(number_of_guesses))


def incorrect():
    global bulls
    global number_of_guesses
    print("You guessed incorrectly")
    bulls += 1
    number_of_guesses += 1
    print("You have {} cows and {} bulls.".format(cows, bulls))


user_guess()