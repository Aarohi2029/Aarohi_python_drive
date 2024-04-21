n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))
n3=int(input("Enter Number 3 : "))

if n1==n2 or n2==n3 or n3==n1:
    print("zero")
else:
    sum=n1+n2+n3
    print("Sum is : ",sum)
