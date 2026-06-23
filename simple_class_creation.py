class BankAccount:
    def __init__(self,name,bal):
        self.account_holder = name
        self.balance = bal

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Total amount in acount is {self.balance}.")
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f"Total amount is {self.balance}")
        else:
            print("Not Sufficient Amount available.")
    def get_balance(self):
        return self.balance

acc = BankAccount('Ankit',1000000)
print(acc.get_balance())
acc.deposit(2000000)
acc.withdraw(50000)
print(acc.get_balance())