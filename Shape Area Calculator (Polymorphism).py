class Shape:
    def area(self):
        pass

class circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print(3.14*self.r*self.r)

class square(Shape):
    def __init__(self,a):
        self.a = a
    def area(self):
        print(self.a*self.a)

class Triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        print(1/2*self.b*self.h)

shapes = [
    circle(5),
    square(2),
    Triangle(10,5)
]

for s in shapes:
    s.area()