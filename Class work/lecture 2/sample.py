sname=input("Enter Name : ")
rno=int(input("Roll No : "))
s1=int(input("Enter marks of subject1 :"))
s2=int(input("Enter marks of subject2 :"))
s3=int(input("Enter marks of subject3 :"))

total=s1+s2+s3
per=total/3

print("Enter Name: ",sname)
print("Roll No: ",rno)
print("Total: ",total)
print("Percantage: ",per)

if per>=70:
    print("Distincation")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("pass class")
else:
    print("fail")

