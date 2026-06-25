# class ATM:
#     def __init__(self):
#         self.balance = 1000
#
#
# atm = ATM()
# print(atm.balance)

## Protected Variable
# class ATM:
#     def __init__(self):
#         self._balance  = 2000
#
# atm = ATM()
# print(atm._balance)

## Private Variable
class ATM:
    def __init__(self):
        self.__balance = 5000

atm = ATM()
print(atm.__balance)