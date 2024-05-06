'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.'''

mylist=[]

for i in range(1,31):
    mylist.append(i*i)


print("first 5 elements : ",mylist[:5])
print("last 5 elements : ",mylist[-5:])
