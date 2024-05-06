class Base:
    def show(self):
        print("show from base")
class Derived1(Base):
    def show(self):
        super().show()
        print("show from derived1")
class Derived2(Base):
    def show(self):
        super().show()
        print("show from derived2")
        
class Subderived(Derived1,Derived2):
    def show(self):
        super().show()
        print("show from subderived")

s1=Subderived()
s1.show()
