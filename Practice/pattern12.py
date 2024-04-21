n=int(input("Enter value: "))
value = 65


for i in range(n,-1,-1):
    for j in range(i,-1,-1):
        alphabet = chr(value+j)
        print(alphabet, end=" ")
    print()
