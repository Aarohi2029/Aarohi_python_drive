'''Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?'''

'''Inheritance:-the object of one class can aquire the properties of oobject of
another class is called inheritanceor creating a new class from
existing class is called inheritance.'''

'''In Python, a constructor is a special method that is called when an object is created.
The purpose of a python constructor is to assign values to the data members within the
class when an object is initialized. The name of the constructor method is always __init__.'''

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)


b1=B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()
