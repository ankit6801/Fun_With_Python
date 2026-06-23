class Animal:
    def sound(self):
        print("Animal sound.")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Barks.")

class Cat(Animal):
    def sound(self):
        print("Cat mew.")

d = Dog()
c = Cat()
d.sound()
c.sound()