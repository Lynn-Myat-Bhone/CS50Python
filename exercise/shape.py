class Shape:
    
    def area():
        pass
    def perimeter():
        ...
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return ( 3.142 * self.radius **2)
    
    def perimeter(self):
        return (2 * 3.142 * self.radius)
    
class Triangle(Shape):
    def __init__(self,base,side1,side2,side3,height):
        self.base =base
        self.side1= side1
        self.side2= side2
        self.side3= side3
        self.height = height
        
    def area(self):
        return ( 1/2 * self.base * self.height)
    
    def perimeter(self):
        return (self.side1+ self.side2+ self.side3)

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width= width
        self.length = length
       
    def area(self):
        return (self.width* self.length)
    
    def perimeter(self):
        return (2 * (self.width + self.length))
    
# for circle
radius = 7
circle = Circle(radius)
print("Area of circle is ", circle.area())
print("Perimeter of circle is ", circle.perimeter())
print("---------------------")
#  for triangle
triangle = Triangle(5,4,3,5,4)
print("Area of triangle is ", triangle.area())
print("Perimeter of triangle is ", triangle.perimeter())
print("---------------------")
# for Rectangle
rectangle = Rectangle(5,7)
print("Area of rectangle is ", rectangle.area())
print("Perimeter of rectangle is ", rectangle.perimeter())

