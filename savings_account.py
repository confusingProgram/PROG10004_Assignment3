from account import Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate, minimum_balance):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate
        self._minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= self.balance - self.minimum_balance:
            self.balance -= amount
        else:
            print("Transaction cannot be completed.")