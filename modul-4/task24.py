'''Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle'''
class Rectangle:
    def compute_area(self, length, width):
        self.length = length
        self.width = width
        
        a= self.length * self.width
        print("area = ",a)



#rectangle = Rectangle(length, width)
R1 = Rectangle()
R1.compute_area(100,30)
