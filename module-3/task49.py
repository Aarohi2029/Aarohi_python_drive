'''Write a Python function to check whether a number is in a given range'''
def Range(number, start, end):
       return start <= number <= end

number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if Range(number, start, end):
    print(number, "is in the range from", start, "to", end)
else:
    print(number, "is not in the range from", start, "to", end)
