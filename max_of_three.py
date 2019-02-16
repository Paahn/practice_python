# Implement a function that takes
# as input three variables, and returns the
# largest of the three. Do this without using the Python max() function!


def my_func(a, b, c):
    print("You've given me the numbers {}, {} and {}.".format(a, b, c))
    if a > b and a > c:
        print("{} is the largest number of those three.".format(a))
    elif b > a and b > c:
        print("{} is the largest number of those three.".format(b))
    elif c > a and c > b:
        print("{} is the largest number of those three.".format(c))



my_func(6, 666, 66)
