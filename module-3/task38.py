'''Write a Python program to check multiple keys exists in a dictionary'''


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


keys = ['a', 'b','e']

a=True

for i in keys:
    if i not in d:
       a = False
       break





if a:
    print("All keys exist in the dictionary.")
else:
    print("One or more keys do not exist in the dictionary.")

