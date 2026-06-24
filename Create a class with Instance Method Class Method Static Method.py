class Employee:
    company = "TCS"

    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")
    @classmethod
    def show_company(cls):
        print(f"Company Name: {cls.company}")

    # @classmethod
    # def set_company(cls,company):
    #     cls.company = company

    @staticmethod
    def greet():
        print("Welcome to the company.")

e1 = Employee("Ankit Kumar")
e1.display()
Employee.company = "Infosys"  #Instance Method
Employee.show_company() #class Method
Employee.greet()        #Static Method