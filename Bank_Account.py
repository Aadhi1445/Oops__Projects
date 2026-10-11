from abc import ABC,abstractmethod
class InsufficientFunds(Exception):
    pass
class BankAccount(ABC):
    def __init__(self,name,balance):
        self.name=name
        if type(balance) is not int:
            raise TypeError('Balance should be number and positive number')
        if balance < 1:
            raise ValueError('Balance should be Positive')
        self.__balance=balance
        self.__mini_statement=[]
        self.__mini_statement.append('Account is Created')
        print('Account Successfully Created')
    @property
    def balance(self):
        return self.__balance
    @abstractmethod
    def deposit(self,amount):
        if  type(amount) is not int:
            raise TypeError('Amount must be an Number and its should be Positive')
        if amount < 1:
            raise ValueError('Amount should be Positive')
        self.__balance+=amount
        print('Amount Successfully Deposited')
        self.__mini_statement.append(f"{amount} is Deposited")
        return self.__balance
    @abstractmethod
    def withdraw(self,amount):
        if  type(amount) is not int:
            raise TypeError('Amount must be an Number and its should be Positive')
        if amount<1:
            raise ValueError('Amount should be Positive')
        if amount>self.__balance:
            raise InsufficientFunds('Insufficient Funds ')
        self.__balance-=amount
        print('Amount Successfully Withdrawn')
        self.__mini_statement.append(f"{amount} is Withdrawn")
        return self.__balance
    # def transaction(self,k):
    #     self.__mini_statement.add(k)
    @property
    def transaction(self):
        return self.__mini_statement.copy()
    def __str__(self):
        return (f"Account Holder's Name : {self.name}\n"
                f"Account Holder's Balance :{self.balance} ")
# account1=BankAccount('Aditya',5000)
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
#     print('Enter Valid Amount')
# except Exception as e:
#     print(e)
# print(account1)
