n=int(input("Enter Number: "))

for i in range(n+1,0,-1):
    for j in range(i,0,-1):
        print(i,end="")
    print()
