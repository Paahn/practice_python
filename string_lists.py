# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

a = input("Gimme a string of characters: ")
b = a[::-1]
if a == b:
    print("Hey! The string you gave me is a palindrome!")
else:
    print("That string was not a palindrome.")
