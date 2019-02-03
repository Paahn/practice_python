# Write a program that takes a list and returns
# a new list that contains all the elements of the first
# list minus all the duplicates.
# Write two different functions to do this - one using a loop
# and constructing a list, and another using sets.

a = [2, 83, 3, 64, 33, 67, 33, 64, 69, 83, 67, 3, 33, 2]
b = []


def rem_duplicates():
    for i in a:
        if i not in b:
            b.append(i)
    print(b)


def with_set():
    c = list(set(a))
    print(c)

rem_duplicates()
with_set()