class Bank:
    def __init__(self):
        self.balance = 0
        print("welcome to bank")

    def deposit(self):
        amount = float(input("enter the deposit amount: "))
        self.balance += amount
        print("amount deposited",  amount)

    def withdraw(self):
        amount = float(input("enter the withdraw amount: "))
        if self.balance > amount:
            self.balance-= amount
            print("withdraw amount", amount)

    def display(self):
        print("total balance=", self.balance)

s = Bank()
s.deposit()
s.withdraw()
s.display()