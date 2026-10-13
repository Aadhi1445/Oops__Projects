from Bank_Account import *
class CurrentAccount(BankAccount):
    def __init__(self,name,balance,min_bal=1000):
        self.min_bal=min_bal
        super().__init__(name,balance)
    def deposit(self,amount):
        super().deposit(amount)
    def withdraw(self,amount):
        amount=super().validate_amount(amount)
        if amount> self.balance-self.min_bal:
            raise ValueError('Minium Balance Should be Maintained')
        super().withdraw(amount)
