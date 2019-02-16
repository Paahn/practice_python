# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say
# whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number

not_found = True
l = 0
r = 100
guesses = 0

while not_found:
    m = int((l + r) / 2)
    answer = input("Is your number {}?".format(m))
    if "high" in answer:
        r = m - 1
        guesses += 1
    elif "low" in answer:
        l = m + 1
        guesses += 1

    elif "yes" in answer:
        guesses += 1
        print("Congrats! You guessed right. It took you {} tries.".format(guesses))
        not_found = False
    else:
        print("Read the rules, try again.")


