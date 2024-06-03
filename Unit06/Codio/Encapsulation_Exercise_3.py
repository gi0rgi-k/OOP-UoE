"""Encapsulation Exercise 3"""


# Create the BankAccount class
class BankAccount:
    def __init__(self):
        self.__checking = 0.0
        self.__savings = 0.0

    def get_checking(self):
        return self.__checking

    def set_checking(self, amount):
        self.__checking = amount

    def get_savings(self):
        return self.__savings

    def set_savings(self, amount):
        self.__savings = amount


# Initialize the BankAccount class object
my_account = BankAccount()

# Set and get checking account balance
my_account.set_checking(523.48)
print(my_account.get_checking())  # Expected: 523.48

# Set and get savings account balance
my_account.set_savings(386.15)
print(my_account.get_savings())  # Expected: 386.15

# To verify private attributes directly for testing purposes:
print(my_account._BankAccount__checking)  # Expected: 523.48
print(my_account._BankAccount__savings)   # Expected: 386.15
