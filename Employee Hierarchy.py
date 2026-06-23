class Employee:

    def salary(self,salary):
        print(f"Base salary is {salary}")
class Developer(Employee):
    def salary(self,salary):
        super().salary(salary)
        print("Dev salary is 7500000.00")

class manager(Employee):
    def salary(self,salary):
        print("salary is 500000.00")

E1 = Employee()
E1.salary(200000)
m1 =  manager()
m1.salary(20000)
d1 = Developer()
d1.salary(2200000)