# Write a program that asks the user how many
# Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you
# can use functions. Make sure to ask the user
# to enter the number of numbers in the sequence
# to generate.(Hint: The Fibonnaci seqence is a
# sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in
# the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(n):
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

a = int(input("How many fibonacci numbers do you want: "))
for i in range(1, a):
    print(fibonacci(i))