class Employee:
    def __init__(self,id,name,sal):
        self.id = id
        self._name = name
        self._sal = sal

    def display(self):
        print(f"Name is - {self._name}\n ID:-{self.id}\nSalary:-{self._sal}")


e1 = Employee(101,"Ankit",800000)
e1.display()
print(e1.id)
print(e1._name)
print(e1._sal)