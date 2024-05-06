'''Write a Python program to select an item randomly from a list.'''
import random

mylist=[1,2,"a",True,1.2,67,"w",False,"t",4,6]
l=[]

for i in mylist:
    l=random.choice(mylist)

print("randomly from a list":l)
