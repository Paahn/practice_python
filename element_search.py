# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest
# to largest) and another number. The function decides
# whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.

a = [56, 32, 13, 69, 666, 45, 90, 43, 30, 25]
print(sorted(a))

def check_num():
    b = int(input("gimme an integer: "))
    if b in a:
        print("{}, {} is in the list".format(True, b))

    else:
        print("{}, {} is not in the list".format(False, b))


check_num()

