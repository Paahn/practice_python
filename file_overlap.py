# Given two .txt files that have lists of numbers
# in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers
# under 1000, and the other .txt file has a list of happy numbers up to 1000.

'''This function returns a list containing the elements of the file we give to it'''
def my_func(filename):
    with open(filename, 'r') as f:
        lista = []
        line = f.readline()
        while line:
            lista.append(int(line))
            line = f.readline()
    return lista


prime = my_func('red1.txt')
happy = my_func('happy.txt')

overlap = [i for i in prime if i in happy]
print(overlap)
