from account import Account
class ChequingAccount(Account):
    def __init__(self, account_number, balance, account_name, interest_rate, overdraft_limit):
        super().__init__(account_number, balance, account_name, interest_rate)
        # We'll set the standard interest rate to 1.01 for ChequingAccount.
        self._overdraft_limit = overdraft_limit # We'll set the standard overdraft_limit to $500.00

    def withdraw(self, amount):
        if amount <= (self._current_balance + self._overdraft_limit): 
            self._current_balance -= amount
            return "True" # If successful, returns "True" for confirmation purposes.
        else:
            return amount - self._overdraft_limit - self._current_balance # If unsuccessful, return the excess amount.