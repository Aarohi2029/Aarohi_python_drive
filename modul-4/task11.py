''' Write a Python program to write a list to a file. '''

l = ["L1", "L2", "L3", "L4", "L5"]

with open('task11.txt', 'w') as file:
    
    for i in l:
        file.write(str(i) + '\n')

print("file complete!!!")
