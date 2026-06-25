class Person:
    def __init__(self,age):
        self.__age =age     # private variable

    #Getter
    def get_age(self):
        return self.__age

    #Setter
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")
P = Person(20)

print("Age: ",P.get_age())

P.set_age(25)
print("Updated Age: ",P.get_age())

