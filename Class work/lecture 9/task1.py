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
