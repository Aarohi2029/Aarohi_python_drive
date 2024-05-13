''' Write a python program to find the longest words.'''

s = "My name is Aarohi"00
0
words = s.split()

max_word = ""
max_len = 0

for i in words:

    if len(i) > max_len:

        max_word = i

print(max_word)
