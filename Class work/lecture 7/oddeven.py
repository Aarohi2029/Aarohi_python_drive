import random
data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt","r")
odd=open("odd.txt","w")
even=open("even.txt","w")

l=data.read().split(",") [:-1]
for i in l:
    if int(i)%2==0:
       even.write(i+",")
    else:
        odd.write(i+",")

data.close()
odd.close()
even.close()

print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Data File Content")
data=open("even.txt","r")
print(data.read())
data.close()

print("Data File Content")
data=open("odd.txt","r")
print(data.read())
data.close()

prime=open("prime.txt","w")
if data%2!=0:
    for i in range(int(data/2)+1):
        if data%i==0:
           data.write(i+",")
    else:
        prime.write(i+",")
else:
    data.write(i+",")

prime.close()

print("Data File Content")
data=open("prime.txt","r")
print(prime.read())
data.close()



