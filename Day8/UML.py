#uml classes

#parent classes
class bank:
    code = None
    address = None
    def manages(self):
        print("this is a the method manages under bank class")
    def maintains(self):
        print("this is the maintains method under the Bank class")

class ATM:
    location = None
    managedBy = None
    def identifies(self):
        print("identifies method under ATM class")
    def transactions(self):
        print("transaction method under ATM class")

#under atm class
class atmTransaction:
    transactionId = None
    date = None
    type = None
    def update(self):
        print("this is the atm transaction class")

#in association with Bank class
class debitCard:
    cardNo = None
    ownedBy = None
    def access(self):
        print("this is the debit Card class")

class customer:
    name = None
    address = None
    dob = None
    def owns(self):
        print("this is the customer class")

#in association debit card class and customer class and the ATM transaction class.
class savingAccounts:
    accountNo = None
    def debit(self):
        print("print this is the savings account class")
    def credit(self):
        print("this is the checkingAccount class")

class checkingAccount:
    accountNo = None
    def debit(self):
        print("this is the checkingAccount class")
    def credit(self):
        print("this is the checkingAccount class")
