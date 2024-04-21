list = ["apple", "banana", "orange", "strawberry", "kiwi"]

max_length = 0
for i in list:
    if len(i) > max_length:
        max_length = len(i)

print("Length of the longest word:", max_length)
