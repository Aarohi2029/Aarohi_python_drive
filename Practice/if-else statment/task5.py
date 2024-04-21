'''Write a Python program that checks if a given number is divisible by both 5 and
7. If it is, print "Divisible by 5 and 7" '''

n=int(input("Enter Number : "))

if n%5==0 and n%7==0:
    print("Divisible by 5 and 7")
else:
    print("Not Divisible by 5 and 7")
