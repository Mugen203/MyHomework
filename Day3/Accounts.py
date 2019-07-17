# This is for dictionary of lists
account_1 = ["Kwaku", "Affram", "Loan", 360.00]
account_2 = ["Kojo", "Ansah", "Savings", 9000]
account_3 = ["Evelyn","Essien","Current", 5400]

bal_01 = account_1.pop(3)
bal_02= account_2.pop(3)
bal_03 = account_3.pop(3)

bal_accounts={"001":"account_1", "002":"account_2", "003":"account_3"}
print(bal_accounts)

def deposit_1(bal,amountToDeposit):
	return bal + amountToDeposit
def withdraw_1(bal,amountToWithdraw):
	return bal - amountToWithdraw

acc_01 = deposit_1(bal_01, 10)
acc_001 = withdraw_1(bal_01, 40)
print(acc_01)
print(acc_001)

acc_02 = deposit_1(bal_02, 54)
acc_002 = withdraw_1(bal_02, 47)
print(acc_02)
print(acc_002)

acc_03 = deposit_1(bal_03, 45)
acc_003 = withdraw_1(bal_03, 85)
print(acc_03)
print(acc_003)


#This is for list of dictionaries
account_01 = ["Kwaku", "Affram", "Loan", 360.00]
account_02 = ["Kojo", "Ansah", "Savings", 9000]
account_03 = ["Evelyn","Essien","Current", 5400]

bal_2 = account_1.pop(3)

def deposit(bal_2, amount_to_deposit):
    return bal_2 + amount_to_deposit

deposit_2 = deposit(bal_2, 250.00)
print(deposit_2)

#This is for dictionary of dictionaries
account_001 = ["First_Name":"Kwaku","Last_Name":"Affram","Account_Type":"Loan","Balance":360.00]
account_002 = ["First_Name":"Kojo", "Last_Name":"Ansah", "Account_Type":"Savings", "Balance":9000]
account_003 = ["First_Name":"Evelyn","Last_Name":"Essien","Account_Type":"Current", "Balance":5400]

bal_001 = account_1.get("Balance")
bal_002= account_2.get("Balance")
bal_003 = account_3.get("Balance")

bank_accounts={"001":"account_001", "002":"account_002", "003":"account_003"}
print(bank_accounts)

def deposit(balance,amount_to_deposit):
	return balance + amountToDeposit
def withdraw(balance,amount_to_withdraw):
	return balance - amountToWithdraw

act_01 = deposit(bal_001,54)
act_001 = withdraw(bal_001,36)
print(act_01)
print(act_001)

act_02 = deposit(bal_002,57)
act_002 = withdraw(bal_002,8)
print(act_02)
print(act_002)

act_03 = deposit(bal_003,69)
act_003 = withdraw(bal_003,9)
print(act_03)
print(act_003)
