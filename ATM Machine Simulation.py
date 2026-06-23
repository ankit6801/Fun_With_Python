class ATM:
    def __init__(self,account):
        self.account = account

    def withdraw_money(self,amount):
        self.account.withdraw(amount)

    def deposit_money(self, amount):
        self.account.deposit(amount)

    def check_balance(self):
        self.account.balance_check()


class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance -amount
            print(f"Available amount after withdrawal is {self.balance}")
        else:
            print("Insufficient Balance.")

    def deposit(self,amount):
        self.balance +=amount
        print(f"Amount deposited. New balance is {self.balance}")


    def balance_check(self):
        print(f"Current balance is {self.balance}")


acc = BankAccount(1000)
atm = ATM(acc)
atm.check_balance()
atm.deposit_money(500)
atm.withdraw_money(300)
atm.check_balance()