from account import Account
class ChequingAccount(Account):
    def __init__(self, account_number, balance, interest_rate, overdraft_limit):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate # We'll set the standard interest rate to 1.01 for ChequingAccount.
        self._overdraft_limit = overdraft_limit # We'll set the standard overdraft_limit to $500

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Transaction cannot be completed.")