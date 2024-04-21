n=int(input("Enter value: "))
value = 65


for i in range(n):
    for j in range(i+1):
        alphabet = chr(j+value)
        print(alphabet, end=" ")
    print()
