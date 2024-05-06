'''How will you create a dictionary using tuples in python?'''
tuples = [("a", 1), ("b", 2), ("c", 3)]


dictionary = {}


for key, value in tuples:
    dictionary[key] = value


print("Resulting dictionary:", dictionary)
