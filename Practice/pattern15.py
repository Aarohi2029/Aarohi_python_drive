n=int(input("Enter Number: "))

for i in range(0,n+1):
    for j in range(0,i):
        print(i+(j+1),end="")
    print()

