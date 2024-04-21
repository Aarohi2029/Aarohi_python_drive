String = input("Enter the string :")
count = 0
 
for i in String:
      count = count + 1
newString = String[:2 ] + String [count - 2: count ] 
 
print("Input string = " + String)
print("New String = "+ newString)
