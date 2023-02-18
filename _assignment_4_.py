class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        self.title = title
        self.balance = balance
        self.interestRate = interestRate

savings_acct = SavingsAccount("Ashish", 5000, 5)


print("account holder : ",savings_acct.title)
print("saving account : ",savings_acct.balance)
print("interestRate : ",savings_acct.interestRate)