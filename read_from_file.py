# Given a .txt file that has a list of a bunch of names,
# count how many of each name there are in the file,
# and print out the results to the screen.

my_dict = {}
with open('nameslist.txt', 'r') as f:
    line = f.readline()
    while line:
        # strip removes the new line characters
        line = line.strip()
        if line in my_dict:
            my_dict[line] += 1
        else:
            my_dict[line] = 1
        line = f.readline()


print(my_dict)
