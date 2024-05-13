'''Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle'''

class Circle:
    def compute_area(self, r):
        self.radius = r
        
        a= self.radius**2*3.14
        print("area = ",a)

    def perimeter(self):
        p= 2*self.radius*3.14
        print("perimeter : ",p)



#rectangle = Rectangle(length, width)
C1 = Circle()
C1.compute_area(5)
C1.perimeter()
