'''Write a Python program to map two lists into a dictionary'''

keys = ['a', 'b', 'c']
values = [1, 2, 3]


mapped_d = {}


for i in range(min(len(keys), len(values))):
    
    mapped_d[keys[i]] = values[i]


print("Mapped Dictionary:", mapped_d)
