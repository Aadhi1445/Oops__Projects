from Bank_Account import *
class SavingsAccount(BankAccount):
    def deposit(self,amount):
        return super().deposit(amount)
    def withdraw(self,amount):
        return super().withdraw(amount)
account1=SavingsAccount('Aditya',5000)
try:
    account1.deposit(500)
except TypeError as e:
    print(e)
except ValueError as e:
    print('Enter Valid Amount')
except Exception as e:
    print(e)
try :
    account1.withdraw(500)
except TypeError as e:
    print(e)
except ValueError as e:
    print('Enter Valid Amount')
except Exception as e:
    print(e)
print(account1)
print(account1.transaction)