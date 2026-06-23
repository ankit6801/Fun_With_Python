class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting.")


class  car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print("Car often start with key.")
    def drive(self):
        print(f"{self.brand} car is driving.")

class Bike(Vehicle):
    def ride(self):
        print(f"{self.brand} bike is riding.")

car  = car("Toyota")
Bike = Bike("Honda")
car.start()
car.drive()
Bike.start()
Bike.ride()