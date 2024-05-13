'''Write a Python program to append text to a file and display the text.'''

file=open("Test.txt","w")
file.write("This is file write operation using python.")
file.close()
print("successfully")
print("*********************************************************")
file=open("Test.txt","r")
print(file.read())
file.close()
print("*********************************************************")
file=open("Test.txt","a")
file.write("This is file append operation using python.")
file.close()
