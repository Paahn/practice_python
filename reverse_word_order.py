# Write a program that asks the user
# for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

a = input("Gimme a string containing multiple words:\n")
b = a.split(' ')
print(b[::-1])
