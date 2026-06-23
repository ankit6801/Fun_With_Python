from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self,):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        area = 3.14* self.r *self.r
        return area

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(f"Area: ", self.l*self.b)

c = Circle(2)
r = Rectangle(2,3)
print(c.area())
r.area()
