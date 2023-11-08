class Bank:
    def __init__(self, bank_name):
        self._bank_name = bank_name
        self._accounts = []

    def open_account(self, type, name):
        id = 1
        while True:
            if self._accounts[id-1]._account_number != id:
                break
            id = id + 1
            
        if type.lower() == "c":
            #self._accounts.append(Chequing_Account(id, name))
            pass
        elif type.lower == "s":
            #self._accounts.append(#Saving_Account(id, name))
            pass

    def search_account(self, acc_num):
        for account in self._accounts:
            if acc_num == account._account_number:
                return account
        return "null"