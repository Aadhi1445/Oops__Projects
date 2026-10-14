from Bank_Account import *
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, min_bal=1000):
        if type(min_bal) is not int:
            raise TypeError("Minimum balance must be an integer")
        if min_bal < 0:
            raise ValueError("Minimum balance cannot be negative")
        if type(balance) is not int:
            raise TypeError("Balance must be an integer")
        if balance < min_bal:
            raise ValueError("Initial balance must meet the minimum balance")
        self.min_bal = min_bal
        super().__init__(name, balance)
    def deposit(self, amount):
         return super().deposit(amount)
    def withdraw(self, amount):
        amount=super().validate_amount(amount)
        if amount > self.balance - self.min_bal:
            raise ValueError('Minium Balance Should be Maintained')
        return super().withdraw(amount)

    def calculate_interest(self, amount=None):
        if amount is None:
            interest_rate = 0.05
            interest = self.balance * interest_rate
            return round(interest)
        else:
            amount = super().validate_amount(amount)
            interest_rate = 0.05
            interest = amount* interest_rate
            return round(interest)

    def credit_interest(self):
        interest = self.calculate_interest()
        if interest > 0:
            self.deposit(interest)
        return interest
    def display_details(self):
        return (f"Saving's Details :--\n"
                f"Account Holder: {self.name}\n"
                f"Account Balance : {self.balance}/-\n"
                f"Minium Balance : {self.min_bal}/-\n"
                f"Interset Rate : 5%\n"
                f"Interest Amount for Existing Balance : {self.calculate_interest()}/-")
# account1=SavingsAccount('Aditya',5000)
# try:
#     account1.deposit(500)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print('Enter Valid Amount')
# except Exception as e:
#     print(e)
# try :
#     account1.withdraw(500)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# print(account1)
# print(account1.transaction)
# print(account1.calculate_interest())
# print(account1.display_details())