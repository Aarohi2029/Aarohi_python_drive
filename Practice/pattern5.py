n=int(input("Enter value: "))
ascii_value = 65


for i in range(1,n+1):
    for j in range(1,i):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    print()
