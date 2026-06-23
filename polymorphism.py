class Animal:
    def speak(self):
        pass

class Dog:
    def speak(self):
        print("Dog speaks.")

class Cat:
    def speak(self):
        print("Cat meows.")

class Cow:
    def speak(self):
        print("Cow Speaks.")


animals = [Dog(),Cat(),Cow()]
for animal in animals:
    animal.speak()