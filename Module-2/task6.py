
print("**************---Without temp variable---***************")

a=int(input("Enter number1 : "))
b=int(input("Enter number2 : "))

a=a+b
b=a-b
a=a-b

print("After swapping Number1 : ",a)
print("After swapping Number2 : ",b)

print("**************---With temp variable---***************")

a=int(input("Enter number1 : "))
b=int(input("Enter number1 : "))

temp=a
a=b
b=temp

print("After swapping Number1 : ",a)
print("After swapping Number2 : ",b)



