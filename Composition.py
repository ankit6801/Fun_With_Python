class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self,e):
        self.engine = e  # car Has-A Engine


    def start_car(self):
        self.engine.start()
        print("Car is ready to move.")

e=Engine()
car = Car(e)
car.start_car()