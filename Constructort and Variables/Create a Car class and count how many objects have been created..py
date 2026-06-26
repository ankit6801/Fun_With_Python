class Car:
    count = 0   #class variable

    def __init__(self,brand):
        self.brand = brand
        Car.count += 1


    @classmethod
    def total_car(cls):
        print("Total cars:",cls.count)

c1 = Car("Toyota")
c2 = Car("Honda")
c3 = Car("BMW")
Car.total_car()