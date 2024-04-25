#function with no argument & no return value.

def printLine():
    print("*"*60)


printLine()
print("Welcome to user defined function using python.")
printLine()

#function with argument & no return value

def sum(a,b):
    print("sum : ",a+b)

printLine()
x=int(input("Enter value : "))
y=int(input("Enter value : "))

sum(x,y)
printLine()

#function with argument &  return value

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter value : "))
y=int(input("Enter value : "))

#ans=sub(x,y)
print("sub : "sub(x,y))
printLine()



