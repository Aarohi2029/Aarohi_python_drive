string = "Aarohi Gadhavi"
count = 0 

for i in range(0,len(string)):
    if (string[i] != " "):
        count = count + 1
        
print("Total Number of characters in string :" + str(count))
