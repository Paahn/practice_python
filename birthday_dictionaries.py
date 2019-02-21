# For this exercise, we will keep track of
# when our friends birthdays are, and be able
# to find that information based on their name.
# Create a dictionary (in your file) of names and
# birthdays. When you run your program it should
# ask the user to enter a name, and return the
# birthday of that person back to them.
# The interaction should look something like this:
#
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

birthdays = {
    "Harrison Ford": "07/13/1942",
    "Carrie Fisher": "10/21/1956",
    "Mark Hamill": "09/25/1951",
    "Alec Guinness": "04/02/1914",
    "Peter Cushing": "05/26/1913",
    "Peter Mayhew": "05/19/1944",
    "Anthony Daniels": "02/21/1946",
    "Christopher Lee": "05/27/1922",
    "Frank Oz": "05/25/1944",
    "Billy Dee Williams": "4/6/1937",
    "James Earl Jones": "1/17/1931",
    "Warwick Davis": "2/3/1970",
    "David Prowse": "7/1/1935",
    "Denis Lawson": "10/27/1947"
}

print("Welcome to the Star Wars birthday dictionary. We know the birthdays of:\n")
for key in birthdays:
    print(key)

while True:
    answer = input("Whose birthday do you want to look up?")
    for key in birthdays:
        if answer == key:
            print("{}'s birthday is {}.".format(key, birthdays[key]))
