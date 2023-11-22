import chequing_account
from chequing_account import ChequingAccount
import savings_account
from savings_account import SavingsAccount

class Bank:
    def __init__(self, bank_name):
        self._bank_name = bank_name # Hard-coded chequing account and saving account belonging to Tim, Jane, and Hank.
        self._accounts = [ChequingAccount(1, -200,"Tim", 1.01, 500), SavingsAccount(2, 2000, "Tim", 1.10, 1000), 
                                   ChequingAccount(3, 1100.39,"Jane", 1.01, 500), SavingsAccount(4, 2575, "Jane", 1.10, 1000),
                                   ChequingAccount(5, 500.67,"Hank", 1.01, 500), SavingsAccount(6, 6000, "Hank", 1.10, 1000)]

    def open_account(self, type, id, starting_balance, name):
        if type.lower() == "c":
            self._accounts.append(ChequingAccount(id,  starting_balance, name, 1.01, 500))
        elif type.lower() == "s":
            self._accounts.append(SavingsAccount(id, starting_balance, name,  1.10, 1000))
        
    def create_new_id(self): # This method searches for an available ID number in the bank when creating an account.
        id = 1 
        while True:
            if self._accounts[id-1].get_account_number() != id: # For example, it will check if the ID 1 is available, and check element 0.
                return id    # So on so forth until an ID number is not in use. (Ideally, they are sorted by ID number from least to greatest.)
            elif id == len(self._accounts):
                return id + 1         # If the entire list is exhausted, for example if element 0 has ID 1, and there is only element 0, return ID = 2.
            id = id + 1           # If element 0 has  ID 1, then the ID number will be incremented to 2, and element 1 will be checked

    def search_account(self, acc_num): # This method compares requested account number to existing accounts in the list of accounts.
        for account in self._accounts:
            if acc_num == str(account.get_account_number()):
                return account # If a match is found, return the account.
        return "" # Otherwise, return null.
    
    def sort(self): # Sorts accounts by account_number from least to greatest.
        new_account_list = []
        for i in range(len(self._accounts)):
            new_account_list.append(i) # Creates "empty" new list which will house re-ordered accounts.

        for account_A in self._accounts:
            new_index = len(self._accounts) - 1 # Account_A (account being checked) will be assumed to be last in new list.

            for compare_account in self._accounts:
                if account_A.get_account_number() < compare_account.get_account_number(): # Account_A is compared to every other account in the pre-sorted list.
                    new_index = new_index - 1 # If account_A has a lower account number than the account being compared, account_A will be placed earlier in sorted list.
            new_account_list[new_index] = account_A # Once comparing is completed, account_A is added to sorted list according to their new index.

        self._accounts = new_account_list # The list of accounts is defined as the new list.
