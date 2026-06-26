class ATM:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Amount.")

    def check_balance(self):
        print(self.__balance)

atm = ATM(1000)

atm.deposite(500)
atm.withdraw(300)
atm.check_balance()