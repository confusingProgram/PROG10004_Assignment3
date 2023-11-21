from chequing_account import ChequingAccount
from savings_account import SavingsAccount

class Bank:
    def __init__(self, bank_name):
        self._bank_name = bank_name
        self._accounts = []
        self._accounts = [ChequingAccount(1, "Tim"), SavingsAccount(2, "Tim"), ChequingAccount(3, "Jane"), 
                                  SavingsAccount(4, "Jane"), ChequingAccount(5, "Tom"), SavingsAccount(6, "Tom")]

    def open_account(self, type, id, name, starting_balance):
        if type.lower() == "c":
            self._accounts.append(ChequingAccount(id, name, starting_balance, 1.01, 500))
        elif type.lower == "s":
            self._accounts.append(SavingsAccount(id, name, starting_balance, 1.10, 1000))
        
    def create_new_id(self):
        id = 1 # This small block of code searches for an available account number when creating an account.
        while True:
            if self._accounts[id-1].get_account_number != id: # For example, it will check if the ID 1 is available, and check element 0.
                break                                                                 # If element 0 has the ID 1, then the ID number will be incremented, and element 1 will be checked
            id = id + 1                                                               # So on so forth until an ID number is not in use. (Ideally, they are sorted by ID number from least to greatest.)

    def search_account(self, acc_num):
        for account in self._accounts:
            if acc_num == str(account.get_account_number):
                return account
        return ""
    
    def sort(self): # Sorts accounts by account_number from least to greatest.
        new_account_list = []
        for i in range(len(self._accounts)):
            new_account_list.append("") # Creates "empty" new list which will house re-ordered accounts.

        for account_A in self._accounts:
            new_index = len(self._accounts) - 1 # Account_A (account being checked) will be assumed to be last in new list.
            for compare_account in self._accounts:
                if account_A.get_account_number < compare_account.get_account_number: # Account_A is compared to every other account in the pre-sorted list.
                    new_index = new_index - 1 # If account_A has a lower account number than the account being compared, account_A will be placed earlier in sorted list.
            new_account_list[new_index] = account_A # Once comparing is completed, account_A is added to sorted list according to their new index.
        self._accounts = new_account_list
