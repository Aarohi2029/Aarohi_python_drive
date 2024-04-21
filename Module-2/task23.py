inputstring = input("Enter the string :")
word = input("Enter the word :")

middleindex = len(inputstring) // 2

newstring=inputstring[:middleindex] + word + inputstring[middleindex:]

print("Result : ",newstring)
