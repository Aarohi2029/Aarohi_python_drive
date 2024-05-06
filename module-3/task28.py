'''Write a Python program to remove an empty tuple(s) from a list of tuples.'''

listoftuples = [(1, 2), (), (3, 4), (), (), (5, 6), ()]


mylist = []


for i in listoftuples:
    
    if i:
       
       mylist.append(i)


print("remove an empty tuple:", mylist)
