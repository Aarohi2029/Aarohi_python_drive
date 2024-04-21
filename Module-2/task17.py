a = input("Enter string 1 : ")
b = input("Enter string 2 : ")

print("Before swap :",a," ",b)

a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]

print("After swap :",a1,b1)
