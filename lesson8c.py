# Bank Account
# properties-> balance() , deposit(), withdraw, get_loan()

# inheritance
# polymorphism
# encapsulation
# Exception Handling

# Database -> A collection of tables with records
# C -> Creating a database/table, Storing data
# R -> Retrieve data from the data
# U -> Update the Data
# D -> Delete the date

# MySQL, Oracle, SqLite, Postgresql
# pymyql library/module
# Xampp/phpMyadmin database interface

class Account:
    def __init__(self, balance, accno, name, branch, status):
        if balance < 0:
            print("Balance cannot be Zero")
        elif len(name) == 0:
            print("Please enter your Name")
        elif len(accno)!= 5:
            print("Invalid Acc No")
        else:
            print("Bank Details Captured")
            self.balance = balance
            self.accno = accno
            self.name = name
            self.branch = branch
            self. status = status

    def check_balance(self):
        print(f'Your balance is {self.balance}')

        return self.balance

    def deposit(self, amount_to_deposit):
        if amount_to_deposit <= 0:
            print("Cannot deposit zero or negative amount")

        elif amount_to_deposit > 335000:
            print("Exceeded the Maximum Deposit Amount")
        else:
            if self.status == "active":
                print("Thank you for Depositing with us")
                print(f'Your Previous Balance was {self.check_balance()}')
                self.balance = self.balance + amount_to_deposit
                print(f'Your Current Balance is {self.balance}')
            else:
                print("your Account is Inactive")

    # Create a method to withdraw Amount
    # Cannot withdraw more than what is in the account
    # Account is Inactive
    # Should retain an initial deposit 100
    # Exception handling in python

    def withdraw(self, cash_withdraw):
        INITIAL_DEPOSIT = 100
        cash_withdraw = int(input("Enter the Amount you wish to Withdraw"))
        if cash_withdraw > self.balance:
            print("You have insufficient balance to transact")
        elif (self.balance-cash_withdraw) < INITIAL_DEPOSIT:
            print("You should retain an initial deposit")



        else:
            if self.status == "active":
                print("Thank you for withdrawing...")
                print("You have withdrawn {}" .format(cash_withdraw))
                self.balance = self.balance - cash_withdraw
                print("Your current Balance is now {}".format(self.balance))
                return self.balance
            else:
                print("Visit the nearest Branch to activate your Account")



account = Account(100, "09876", "James Dudu", "South B", "active")

account.check_balance()
account.deposit(25000)
account.withdraw(1000)


