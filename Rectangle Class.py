class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        return perimeter

r = Rectangle(2,3)
print(r.area())
print(r.perimeter())

