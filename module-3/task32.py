'''Write a Python script to sort (ascending and descending) a dictionary by
value.'''
mytuple=(23,45,2,5,89,56)


#ascending
t1=tuple(sorted(mytuple))

print("ascending : ",t1)


#descending
t2=tuple(sorted(mytuple,reverse=True))

print("descending : ",t2)

