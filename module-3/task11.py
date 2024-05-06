'''Write a Python function that takes a list and returns a new list with unique
elements of the first list.'''

mylist=[1,2,3,4,5,6,7,8,9,10,7,8,9]
newlist=[]

for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(" new list with unique elements of the first list : ",newlist)
