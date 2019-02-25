# In the birthday_dictionaries exercise we created a dictionary
# of famous scientists birthdays. In this exercise,
# modify your program from Part 1 to load the birthday
# dictionary from a JSON file on disk, rather than
# having the dictionary defined in the program.
#
# Bonus: Ask the user for another scientists name and
# birthday to add to the dictionary, and update the JSON
# file you have on disk with the scientists name. If you
# run the program multiple times and keep adding new names,
# your JSON file should keep getting bigger and bigger.

import json

darkthrone_birthdays = {
    "Ted Skjellum": "03/04/1972",
    "Gylve Fenris Nagell": "11/28/1971",
    
}

with open("darkthrone.json", "w") as f:
    json.dump(darkthrone_birthdays, f)


print("Welcome to the Darkthrone birthday dictionary. We know the birthdays of:\n")
for key in darkthrone_birthdays:
    print(key)

while True:
    answer = input("Whose birthday do you want to look up?")
    for key in darkthrone_birthdays:
        if answer in key:
            print("{}'s birthday is {}.".format(key, darkthrone_birthdays[key]))