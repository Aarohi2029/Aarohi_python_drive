class Base:
    def show(self):
        print("show from base")
class Derived(Base):
    def show(self):
        super().show()
        print("show from derived")
class Subderived(Derived):
    def show(self):
        super().show()
        print("show from subderived")

s1=Subderived()
s1.show()
