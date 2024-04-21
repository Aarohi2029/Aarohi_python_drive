s= input("Enter a string: ")

if len(s) >= 3:
    if s.endswith('ing'):
        result = s + 'ly'
    else:
        result = s + 'ing'
else:
    result = s

print("Result:", result)
