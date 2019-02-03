# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randint

a = randint(1, 9)
ans = int(input("Guess a number between 1 and 9: "))
guesses = 0
while True:
    try:
        if ans == a and guesses == 0:
            print("Wow! You got it right the first time!")
            break
        elif ans < a:
            guesses += 1
            ans = int(input("Too low. Guess again."))
        elif ans > a:
            guesses += 1
            ans = int(input("Too high. Guess again."))
        else:
            guesses += 1
            print("You guessed right! It only took you {} times.".format(guesses))
            break
    except ValueError:
        print("Try again")



