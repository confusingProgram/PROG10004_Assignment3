from account import Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, account_name, interest_rate, minimum_balance):
        super().__init__(account_number, balance, account_name, interest_rate)
                # We'll set the standard interest rate to 1.10 for SavingsAccount.
        self._minimum_balance = minimum_balance # We'll set the standard minimum balance to $1000.00

    def withdraw(self, amount):
        if amount <= (self._current_balance - self._minimum_balance):
            self._current_balance -= amount
            return "True"
        else:
            return amount - self._minimum_balance