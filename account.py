class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class ChequingAccount(Account):
    def __init__(self, account_number, balance, chequing_fee):
        super().__init__(account_number, balance)
        self.chequing_fee = chequing_fee

    def calculate_fee(self):
        return self.chequing_fee

