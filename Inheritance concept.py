class Shape:
    # def area(self):
    #     print("Area of Shape")

    def rad(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print(area)

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w

    def area(self):
        area = self.l * self.w
        print(area)

c = Circle(2)
r = Rectangle(4,5)

c.area()
r.area()