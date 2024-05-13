'''Write a Python program to read an entire text file'''

file=open("Test.txt","w")
file.write("This is file write operation using python.")
file.close()
print("successfully")
print("*********************************************************")
file=open("Test.txt","r")
print(file.read())
file.close()
print("*********************************************************")
