'''' Write a Python program that checks if a given year is a leap year. If it is, print
"Leap year".'''
year=int(input("Enter year : "))

if(year % 400 == 0) and (year % 100 == 0):
    print("This ",year,"is leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("This ",year,"is leap year")
else:
    print("This",year,"is not leap year")
