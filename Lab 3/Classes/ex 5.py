class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposit accepted.")
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("Withdrawal accepted.")
        else:
            print("Funds unavailable")

acct = Account("Sh Y", 100)

acct.deposit(50)
acct.withdraw(75)
acct.withdraw(500)



