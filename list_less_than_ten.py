# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# 1) Instead of printing the elements one by one, make a new list that has all
# the elements less than 5 from this list in it and print out this new list.
# 2) Write this in one line of python.
# 3) Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 1) solution
#
# b = []
# for i in range(len(a)):
#     if a[i] < 5:
#         b.append(a[i])
#
# print(b)

# 2) solution. I used list comprehensions.
b = [n for n in a if n < 5]
print(b)

# 3) solution
num = int(input("Gimme a number: "))
c = [n for n in a if n < num]
print(c)