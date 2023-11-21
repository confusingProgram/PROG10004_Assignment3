from account import Account
class ChequingAccount(Account):
    def __init__(self, account_number, balance, chequing_fee, overdraft_limit):
        super().__init__(account_number, balance)
        self._chequing_fee = chequing_fee
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Transaction cannot be completed.")