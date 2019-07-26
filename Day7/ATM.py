import datetime

class BankAccount(object):

    def __init__(self, name, pin, balance = 1000000):
        self.name = name
        self.pin =  pin
        self.balance = balance

    def check_user(self, name, pin):
        try:
            if pin != self.pin:
                raise Error
            print("Your pin matches! :)")
        except Error:
            print("Your pin is incorrect!! :(")
            exit(0)

    def string(self):
        return "{}'s bank account with Balance {}".format(self.name, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        try:
            if self.balance >= amount:
            self.balance -= amount
            else:
                raise Error
        except Error:
            print("Insufficient funds! Sorry... :(")

    def check_balance(self):
