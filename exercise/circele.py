class circle:
    PI = 3.142
    @classmethod
    def area(cls,radius):
        area = cls.PI * radius*radius # radius **2 is also  radius square
        return area
    @classmethod
    def perimeter(cls,radius):
        perimeter = 2 * cls.PI * radius
        return perimeter

radius = float(input("Input a radius of circle : "))
print("Area of a circle is ", circle.area(radius))
print("Perimeter of a circle is ",circle.perimeter(radius))