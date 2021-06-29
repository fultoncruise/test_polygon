#1.Create a Polygon class with a parameter color and num_sides.
import math
class Polygon:
    def __init__(self, color, num_sides):
        self.color = color
        self.num_sides = num_sides
#2. Create a class Triangle that inherits from Polygon, has parameters  base and height and has a method area()
class Triangle(Polygon):
    def __init__(self,color, base, height,num_sides=3):
        super().__init__(color, num_sides)
        self.base = base
        self.height = height
    def area(self):
        return float(0.5*self.base*self.height)
# 3.Create a class Rectangle …
class Rectangle(Polygon):
    def __init__(self, color,base, height,num_sides=4):
        self.base = base
        self.height = height
        super().__init__(color, num_sides)
    def area(self):
        return self.base*self.height
# 4.Create a class Square that inherits from Rectangle ...
class Square(Rectangle):
    def __init__(self, color, base, height=1,  num_sides=4):
        self.base = base
        self.height = height
        super().__init__(color,base, height, num_sides)
    def area(self):
        return self.base*self.base
# 5.Create a class Circle, from the module math use the values math.inf as the number of sides and math.pi to calculate the area.
class Circle(Polygon):
    def __init__(self, color, radius,num_sides=math.inf):
        self.radius = radius
        super().__init__(color, num_sides)
    def area(self):
        return round(math.pi*self.radius*self.radius, 2)
#6. Test your classes:
#a. create a red triangle with base 4 and height 3, verify that the area is 6.
if __name__=="__main__":
    triangle = Triangle("red",4, 3)
    print(triangle.area())
    # b.Create a blue rectangle with base 2.5 and height 2, the area should be 5.
    rectangle = Rectangle("blue", 2.5, 2,)
    print(rectangle.area())
    #c. Create a green square with size 4, the area should be 16.
    square = Square("green", 4)
    print(square.area())
    # d.Create a yellow circle with radius 2, the area should be 12.56… .
    circle = Circle("yellow", 2)
    print(circle.area())
# 7.Save your code as a file name polygon.py
# 8.Import your code in the file paint_calculator.py.