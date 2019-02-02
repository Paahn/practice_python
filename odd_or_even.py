# Ask the user for a number. Depending on whether the number is even or odd, print out
# an appropriate message to the user
# If the number is a multiple of 4, print out a different message.

a = int(input("Gimme a number: "))

if a % 4 == 0:
    print("Your number is a multiple of 4")
elif a % 2 == 0:
    print("You have entered an even number")
else:
    print("You have entered an odd number. Odd innit?")

num = int(input("gimme a number: "))
print("Ok, you gave me the number {}".format(num))
check = int(input("gimme another number: "))
print("Ok, you gave me the number {} and {}".format(num, check))

if num % check  == 0:
    print("{} divides evenly into {}.".format(check, num))
else:
    print("{} does not divide evenly into {}.".format(check, num))


