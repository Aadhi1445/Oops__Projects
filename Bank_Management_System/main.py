from Savings_Account import SavingsAccount
from Current_Account import CurrentAccount
accounts={}
next_account_number=1001

def ch1():
    global next_account_number
    name = input("Enter customer name: ")
    try:
        balance = int(input("Enter initial deposit: "))
        if balance <= 0:
            print("Initial deposit must be greater than zero.")
            return
        account = SavingsAccount(name, balance)
        accounts[next_account_number] = account
        print("Savings Account Created Successfully!")
        print("Account Number:", next_account_number)
        print("Customer Name:", name)
        print("Balance:", account.balance)
        next_account_number += 1
    except ValueError as e:
        print('Error: ',e)
def ch2():
    global next_account_number
    name=input('Enter Customer Name: ')
    try:
        balance=int(input('Enter Initial Deposit: '))
        if balance <= 0:
            print("Initial deposit must be greater than zero.")
            return
        account = CurrentAccount(name, balance)
        accounts[next_account_number] = account
        print("Current Account Created Successfully!")
        print("Account Number:", next_account_number)
        print("Customer Name:", name)
        print("Balance:", account.balance)
        next_account_number += 1
    except ValueError as e:
        print('Error: ',e)













if __name__ == '__main__':
    while True:
        print('-'*8,'Bank Management System','-'*8)
        print('''    1. Create Savings Account
        2. Create Current Account
        3. Deposit Money
        4. Withdraw Money
        5. Check Balance
        6. View Transaction History
        7. Calculate and Credit Savings Interest
        8. Exit''')
        choice=input('Enter your Choice: ')
        if choice=='8':
            print('Thank you for using our Banking System')
            break
        if choice == '1':
            print("Create Savings Account")
            ch1()
        elif choice == '2':
            print("Create Current Account")
            ch2()
        elif choice == '3':
            print("Deposit Money")
        elif choice == '4':
            print("Withdraw Money")
        elif choice == '5':
            print("Check Balance")
        elif choice == '6':
            print("View Transaction History")
        elif choice == '7':
            print("Calculate and Credit Savings Interest")
        else:
            print("Invalid choice. Please select between 1 and 8.")


# savings = SavingsAccount("Aditya", 5000)
# print()
# current = CurrentAccount("Rahul", 10000)
# print()
# accounts = [savings, current]
# for account in accounts:
#     print(account)
#     print()
#     # print("Current Balance:", account.balance)
#     # print()