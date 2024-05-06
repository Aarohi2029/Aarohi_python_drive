'''Q.2 How will you remove last object from a list?
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

ans:--To remove the last object from a list in Python,
you can use the pop() method or simply slice the list.'''

mylist=[2, 33, 222, 14, 25]

mylist = mylist[:-1]  # This removes the last item from the list
print("Updated list:", mylist)
