class ATM:
    def __init__(self,balance):
        self.__balance = balance       #private Variable

    def deposit(self,amount):
        self.__balance += amount    #private varibale
        print("Deposit: ",amount)

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw: ",amount)
        else:
            print("Insuficient Balance.")

    def check_balance(self):
        print("Available Balance",self.__balance)

atm = ATM(1000)
atm.deposit(300)
atm.check_balance()