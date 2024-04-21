str = input("Enter the string :")
str= str.split()
i=0
count=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count = count+1
    
    print("Word",str[i],"Present",count," times in sentence")

    i=i+1
