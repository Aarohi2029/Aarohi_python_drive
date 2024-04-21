n = int(input("Enter value: "))
value = 65

for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        alphabet = chr(value + j)
        print(alphabet, end=' ')
    print()
