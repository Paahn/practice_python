# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.
# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.
# Print out that many copies of the previous message on separate lines.
import datetime

a = input("Please input your name: ")

print("Ok, your name is {}".format(a))

b = int(input("Please enter your age: "))

print("Hey {0}, you will turn 100 in {1}".format(a, (100 - b) + int(datetime.date.today().strftime("%Y"))))

c = int(input("Also, give me a number and I will print that many copies of the previous message: "))

print("Hey {0}, you will turn 100 in {1}\n".format(a, (100 - b) + int(datetime.date.today().strftime("%Y"))) * c)

