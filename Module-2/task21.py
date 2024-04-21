s = input("Enter a string: ")

if len(s) % 4 == 0:
    reversed_string = s[::-1]
    print("Reversed string:", reversed_string)
else:
    print("String length is not a multiple of 4 :", s)
