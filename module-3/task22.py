'''Write a Python program to check whether an element exists within a
tuple.'''

mytuple = (1, 2, 3, 4, 5)


i = 5


if i in mytuple:
    print("Element",i, "exists in the tuple.")
else:
    print("Element", i, "does not exist in the tuple.")
