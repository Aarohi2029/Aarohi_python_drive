n = int(input("Enter value: "))
value = 65

for i in range(n,0,-1):
    print(' ' *(n - i - 1), end=' ')
    for j in range(i,0,-1):
        alphabet = chr(value + j-1)
        print(alphabet, end=' ')
    print(' ')
