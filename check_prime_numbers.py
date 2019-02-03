# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)

a = int(input("Gimme a number and I'm gonna tell you if it's a prime number."))
if a % 2 != 0 and a % 3 != 0:
    print("{} is a prime number!".format(a))
else:
    print("{} is not a prime number.".format(a))