from account import Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate # We'll set the standard interest rate to 1.10 for SavingsAccount.
        self._minimum_balance = minimum_balance # We'll set the standard minimum balance to $1000.00

    def withdraw(self, amount):
        if amount <= self.balance - self.minimum_balance:
            self.balance -= amount
        else:
            print("Transaction cannot be completed.")