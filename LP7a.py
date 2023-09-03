# 7)A) By using the concept of inheritance write a python program to find the area of triangle, circle and rectangle.

import math
class Shape:
 def area(self,s):
    print("area of ",s,end = ":")
class Triangle(Shape):
 def __init__(self, base, height):
    self.base = base
    self.height = height
 
 def area(self):
    Shape.area(self, 'triangle')
    print(0.5 * self.base * self.height)

class Circle(Shape):
 def __init__(self, radius):
    self.radius = radius
 
 def area(self):
   Shape.area(self, 'Circle')
   print(math.pi * self.radius ** 2)

class Rectangle(Shape):
 def __init__(self, width, height):
    self.width = width
    self.height = height
 
 def area(self):
   Shape.area(self, 'Rectangle')
   print(self.width * self.height)


base = int(input("enter the base : "))
height = int(input("enter the height : "))
t = Triangle(base, height)
t.area()

radius = int(input("enter the radius : "))
c = Circle(radius)
c.area()

w = int(input("enter the width : "))
h = int(input("enter the height : "))
r = Rectangle(w, h)
r.area()

