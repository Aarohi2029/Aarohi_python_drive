'''How to Define a Class in Python? What Is Self? Give An Example Of
A Python Class'''

'''ANS : In Python, a class is a blueprint for creating objects (instances). It defines the structure and behavior of those objects.
To define a class in Python, you use the class'''

'''The self keyword in Python is used to refer to the instance of the class. It is a convention in Python to use self as the first parameter in the definition of instance methods. When you call a method on an instance,
Python automatically passes the instance itself as the first argument to the method.'''

class Student:

    def getdata(self,fname,lname):
        print("getdata called")
        self.f=fname
        self.l=lname
    def  putdata(self):
        print("putdat called")
        print("first name : ",self.f)
        print("first name : ",self.l)

s1=Student()
s1.getdata("Aarohi","Gadhavi")
s1.putdata()
