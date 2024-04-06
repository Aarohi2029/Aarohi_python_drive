a=int(input("enter A : "))
b=int(input("enter B : "))
c=int(input("enter C : "))

if a>b:
    if a>c:
        print("A is max")
    else:
         print("C is max")
elif b>c:
    print("B is max")
else:
    print("C is max")
        
