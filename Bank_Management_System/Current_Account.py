from Bank_Account import *
class CurrentAccount(BankAccount):
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
    def deposit(self,amount):
        return super().deposit(amount)
    def withdraw(self,amount):
        amount=super().validate_amount(amount)
        if amount> self.balance-self.min_bal:
            raise ValueError('Minium Balance Should be Maintained')
        return super().withdraw(amount)
    def calculate_interest(self,amount=None):
        if amount is None:
            interest_rate = 0.02
            interest = self.balance * interest_rate
            return round(interest)
        else:
            amount = super().validate_amount(amount)
            interest_rate = 0.02
            interest = amount * interest_rate
            return round(interest)
    def credit_interest(self):
        interest = self.calculate_interest()
        if interest > 0:
            self.deposit(interest)
        return interest
    def display_details(self):
        return (f"Current Account :--\n"
                f"Account Holder: {self.name}\n"
                f"Account Balance : {self.balance}/-\n"
                f"Minium Balance : {self.min_bal}/-\n"
                f"Interset Rate : 2%\n"
                f"Interest Amount for Existing Balance : {self.calculate_interest()}/-")




