'''Write a Python program to convert a list of tuples into a dictionary.'''

tuples = [("a", 1), ("b", 2), ("c", 3)]


dictionary = {}


for key, value in tuples:
    dictionary[key] = value


print("Resulting dictionary:", dictionary)

