class Account:
    def __init__(self, account_number, current_balance, account_holder_name, interset_rate):
        self._account_number = account_number
        self._current_balance =current_balance
        self._account_holder_name = account_holder_name
        self._interest_rate = interset_rate

    def get_account_number(self):
        return self._account_number

    def get_account_holder_name(self):
        return self._account_holder_name

    def get_interest_rate(self):
        return self._interest_rate

    def get_current_balance(self):
        return self._balance

    def set_account_holder_name(self, new_name):
        self._account_holder_name = new_name

    def set_interest_rate(self, new_interest_rate):
        self._interest_rate = new_interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            print("Invalid deposit amount.")
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        return self._balance * self._interest_rate / 100





