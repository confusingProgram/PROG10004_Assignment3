import bank
from bank import Bank

class Application:
    def __init__(self):
        pass
    
    def show_main_menu(self, bank):
        print(f"Thank you for using {bank._bank_name}!")
        while True:
            bank.sort()
            print("------ Main Menu ------")
            print("[0] Exit Application")
            print("[1] Select Account")
            print("[2] Open Account")
            choice = input("Please enter an option: ").strip()

            if choice == "[0]" or choice == "[0" or choice == "0]" or choice == "0":
                break
            elif choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                self.select_account(bank)
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                self.open_account(bank)
            else:
                print("Please enter valid number.")
                print("")
    
    def select_account(self, bank):
        while True:
            print("------ Select Account ------")
            id = input("Please enter the account number, or 0 to exit: ").strip()
            account = bank.search_account(id)
            if id == "0": # Exits if user enters "0", in normal applications, 0 is not that starting number.
                break
            elif account == "": # If the user puts in an account number that does not exist, error message.
                print("Please enter valid account number.")
                continue
            self.show_account_menu(account)

    def open_account(self, bank):
        while True:
            print("------ Open Account ------")
            print("Please select an option:")
            print("[0] Exit Creation")
            print("[1] Chequing Account")
            print("[2] Savings Account")
            choice = input("Please enter an option: ").strip()

            if choice == "[0]" or choice == "[0" or choice == "0]" or choice == "0":
                break # Exit
            elif choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                while True: # Name check loop
                    print("------ Name Entry ------")
                    name = input("Please enter your name or EXIT: ").strip()
                    if name == "":
                        print("Name cannot be blank.")
                        continue
                    break
                if name.upper() == "EXIT":
                        break
                while True:
                    print("------ Starting Balance ------")
                    starting_balance = Application.enter_amount()
                    if starting_balance == 0:
                        break
                    id = bank.create_new_id()
                    print(f"Your chequing account with ID #{id} was created!")
                    bank.open_account("c", id, starting_balance, name) # Open chequing account.
                    break
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                while True:
                    print("------ Name Entry ------")
                    name = input("Please enter your name or EXIT: ").strip()
                    if name == "": # Checks if entry is null.
                        print("Name cannot be blank.")
                        continue
                    break
                if name.upper() == "EXIT":
                        break
                while True:
                    print("------ Starting Balance ------")
                    print("Starting balance must be $1000.00 or higher.")
                    starting_balance = Application.enter_amount()
                    if starting_balance == 0:
                        break
                    id = bank.create_new_id()
                    print(f"Your savings account with ID #{id} was created!")
                    bank.open_account("s", id, starting_balance, name) # Open chequing account.
                    break
            else:
                print("Please enter valid option.")
                print("")

    @staticmethod
    def enter_amount():
        while True:
            amount = input("Enter the amount or 0 to exit: ")
            amount = amount.strip()

            try:
                if float(amount) == 0.00:
                    return 0
            except:
                print('HAHAH')
                print("Please enter a positive, non-zero number.")
                continue
            
            if len(amount) == 0: # Restarts if void entry.
                print("Please enter a positive, non-zero number.")
                continue

            if("-") in amount or amount.count(".") > 1: # Restarts if negative detected or if too many decimals.
                print("Please enter a positive, non-zero number.")
                continue

            valid = True
            array = amount.split(".") 
            for str in array: # Detects if there are any non-digits.
                if str.isdigit() == False:
                    valid = False
                    break

            if valid == False: # Restarts if any non-digits.
                print("Please enter a positive, non-zero number.")
                continue
            
            if len(array) > 1: #Assuming the user inserts a price with a decimal value.
                if len(array[1]) > 2: # Restarts if there are too many decimals.
                    print("Please limit the amount to 2 decimal places.")
                    continue

            if valid == True: # If correct, proceeds.
                return float(amount)
            else: # Final catch statement just in case.
                print("Please enter a positive, non-zero number.")

    def show_account_menu(self, account):
        while True:
            print("------ Account Menu ------")
            print(f"Welcome {account.get_account_holder_name()}! Please select an option:")
            print("[0] Exit Account")
            print("[1] Check Balance")
            print("[2] Deposit")
            print("[3] Withdraw")
            choice = input("Please enter a number: ").strip()

                    
            if choice == "[0]" or choice == "[0" or choice == "0]" or choice == "0":
                break
            elif choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                print(f"Current balance: {Application.format_amount(account.get_current_balance())}")
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                while True:
                    amount = Application.enter_amount()
                    if amount != 0:
                        account.deposit(amount)
                        print(f"New balance: {Application.format_amount(account.get_current_balance())}")
                    break
            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                while True:
                    amount = Application.enter_amount()
                    if amount != 0:
                        result = account.withdraw(amount)
                        if result != "True":
                            if type(account) is bank.chequing_account.ChequingAccount:
                                print(f"Withdraw rejected: {Application.format_amount(result)} past overdraft limit.")
                            elif type(account) is bank.savings_account.SavingsAccount:
                                print(f"Withdraw rejected: {Application.format_amount(result)} past minimum balance.")
                            continue
                        print(f"New balance: {Application.format_amount(account.get_current_balance())}")
                    break
            else:
                print("Please enter a valid number.")
                print("")

    def run(self, bank):
        self.show_main_menu(bank)

    @staticmethod
    def format_amount(amount): # This method fixes the formatting involving negative numbers, dollar signs, and $x.x0, and converts to string
        balance = str(amount)
        balance = balance.replace("-", "-$") 
        if balance.count("$") == 0:
            balance = "$" + balance
        temp = balance.split(".")
        if len(temp) == 1:
            balance += (".00")
        elif len(temp) == 2:
            if len(temp[1]) == 1:
                balance += ("0")
        return balance
        

b1 = Bank("TD")
ap1 = Application()
ap1.run(b1)