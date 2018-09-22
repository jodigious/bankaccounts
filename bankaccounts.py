## OOP Challenge

class Account:

    def __init__(self, owner, balance):

        # Attributes
        self.owner = owner
        self.balance = balance

    # Methods
    def deposit(self, amt):
        self.balance = self.balance + amt
        return "Deposit Accepted"

    def withdraw(self, amt):

        if self.balance - amt < 0:
            return "There isn't enoguh in this account for that transaction."
        else:
            self.balance = self.balance - amt
            return "Withdraw Accepted"

    def __str__(self):
        return "\nAccount owner: %s\nAccount balance: %s" %(self.owner, self.balance)
