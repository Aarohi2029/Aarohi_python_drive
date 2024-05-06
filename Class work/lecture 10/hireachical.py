#herichal inheritance

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)

class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)

class C:
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C : ",self.c)

class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D : ",self.d)



b1=D()
b2=B()
b3=C()
b1.getA(10)
b2.getB(20)
b3.getC(30)
b1.getD(40)
b1.putA()
b2.putB()
b3.putC()
b1.putD()
