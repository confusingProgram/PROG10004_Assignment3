from chequing_account import ChequingAccount
from savings_account import SavingsAccount

class Bank:
    def __init__(self, bank_name):
        self._bank_name = bank_name
        self._accounts = []

    def open_account(self, type, name):
        id = 1 # This small block of code searches for an available account number when creating an account.
        while True:
            if self._accounts[id-1].get_account_number != id: # For example, it will check if the ID 1 is available, and check element 0.
                break                                                                 # If element 0 has the ID 1, then the ID number will be incremented, and element 1 will be checked
            id = id + 1                                                               # So on so forth until an ID number is not in use. (Ideally, they are sorted by ID number from least to greatest.)
            
        if type.lower() == "c":
            self._accounts.append(ChequingAccount(id, name))
            pass
        elif type.lower == "s":
            self._accounts.append(SavingsAccount(id, name))
            pass

    def search_account(self, acc_num):
        for account in self._accounts:
            if acc_num == str(account.get_account_number):
                return account
        return ""
    
    def sort_account(self): # Sorts accounts by account_number from least to greatest
        new_account_list = []
        for account in self._accounts:
            new_index = len(self._accounts)-1
            for compare_account in self._accounts:
                if account.get_account_number < compare_account.get_account_number:
                    new_index = new_index - 1
            new_account_list[new_index] = account
        self._accounts = new_account_list
