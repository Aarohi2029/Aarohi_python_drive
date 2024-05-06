'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.'''

s=["Anushka","a","abca",]
count=0

for string in s:
    if len(string)>=2 and string[0]==string[-1]:
        count+=1
print("String Count : ",count)


