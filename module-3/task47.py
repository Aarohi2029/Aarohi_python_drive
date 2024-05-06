'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource''''


string = 'w3resource'


count = {}


for char in string:
   
    if char in count:
        count[char] += 1
   
    else:
        count[char] = 1

print(count)

