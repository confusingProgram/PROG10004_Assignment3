import bank
from bank import Bank

class Application:
    def __init__(self):
        pass
    
    def show_main_menu(self, bank):
        print(f"Thank you for using {bank._bank_name}!")
        while True:
            bank.sort()
            print("")
            print("------ Main Menu ------")
            print("[0] Exit Application")
            print("[1] Select Account")
            print("[2] Open Account")
            choice = input("Please enter an option: ").strip() # strip() removes heading and trailing whitespace.

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
            print("")
            print("------ Select Account ------")
            id = input("Please enter the account number, or 0 to exit: ").strip()
            account = bank.search_account(id)
            if id == "0": # Exits if user enters "0", in normal applications, 0 is not the starting number.
                break
            elif account == "": # If the user puts in an account number that does not exist, error message.
                print("Please enter valid account number.")
                continue
            self.show_account_menu(account) # Assuming a correct ID is found, this will not break this loop, only a "0" will.

    def open_account(self, bank):
        while True:
            print("")
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
                    print("")
                    print("------ Name Entry ------")
                    name = input("Please enter your name or 0 to exit: ").strip()
                    if name == "": # Checks if entry is null.
                        print("Name cannot be blank.")
                        continue
                    break

                try:
                    if float(name) == 0.00: # If input is equal to 0, goes back to ---- Open Account ---- menu.
                        continue
                except:
                    pass

                while True:
                    print("")
                    print("------ Starting Balance ------")
                    starting_balance = Application.enter_amount() # enter_amount() is a method that controls how numbers are entered, i.e., normal "money" amount.
                    if starting_balance == 0: # If input is equal to 0, goes back to ---- Open Account ---- menu.
                        break
                    id = bank.create_new_id() # create_new_id() is a method that searches the bank list of accounts for an available ID number.
                    print(f"Your chequing account with ID #{id} was created!")
                    bank.open_account("c", id, starting_balance, name) # Open chequing account, "c" for chequing.
                    break

            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                while True:
                    print("")
                    print("------ Name Entry ------")
                    name = input("Please enter your name or 0 to exit: ").strip()
                    if name == "": # Checks if entry is null.
                        print("Name cannot be blank.")
                        continue
                    break

                try:
                    if float(name) == 0.00:
                        continue
                except:
                    pass

                while True:
                    print("")
                    print("------ Starting Balance ------")
                    print("Starting balance must be $1000.00 or higher.") 
                    starting_balance = Application.enter_amount()
                    if starting_balance == 0:
                        break
                    if starting_balance < 1000: # The default minimum balance for savings accounts is $1000.00.
                        print("Please enter $1000.00 or higher.")
                        continue
                    id = bank.create_new_id()
                    print(f"Your savings account with ID #{id} was created!")
                    bank.open_account("s", id, starting_balance, name) # Open saving account.
                    break
            else:
                print("Please enter valid option.")
                print("")

    def show_account_menu(self, account):
        while True:
            print("")
            print("------ Account Menu ------")
            print(f"Welcome {account.get_account_holder_name()}! Please select an option:")
            print("[0] Exit Account")
            print("[1] Check Balance")
            print("[2] Deposit")
            print("[3] Withdraw")
            choice = input("Please enter a number: ").strip()
                    
            if choice == "[0]" or choice == "[0" or choice == "0]" or choice == "0":
                break # Exits to ---- Main Menu -----
            elif choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                print(f"Current balance: {Application.format_amount(account.get_current_balance())}") 
                            #format_amount() is a method that controls how money amounts are displayed.

            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                    amount = Application.enter_amount()
                    if amount != 0:
                        account.deposit(amount)
                        print(f"New balance: {Application.format_amount(account.get_current_balance())}")

            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                while True: # Withdraw loop.
                    amount = Application.enter_amount()
                    if amount != 0:
                        result = account.withdraw(amount) 
                        # account.withdraw returns either "True" if successful, or an amount that exceeds the overdraft limit or minimum balance.
                        if result != "True": # If the withdraw was rejected, i.e., returns an amount, the message displayed depnds on account.
                            if type(account) is bank.chequing_account.ChequingAccount: # Checks if account is a Chequing Account.
                                print(f"Withdraw rejected: {Application.format_amount(result)} past overdraft limit.")
                            elif type(account) is bank.savings_account.SavingsAccount: # Checks if account is a Chequing Account.
                                print(f"Withdraw rejected: {Application.format_amount(result)} past minimum balance.")
                            continue # Continue forces user to enter a different amount.
                        print(f"New balance: {Application.format_amount(account.get_current_balance())}")
                        # If all is successful, the new balance is displayed, then the withdraw loop is broken.
                    break
            else:
                print("Please enter a valid number.")
                print("")

    def run(self, bank):
        self.show_main_menu(bank)   

    @staticmethod
    def enter_amount(): # Used when inputting a money amount. Controls and makes sure that inputs are proper.
        while True:
            amount = input("Enter the amount or 0 to exit: ")
            amount = amount.strip()

            try:
                if float(amount) == 0.00: # If the amount entered is equal to 0, then a 0 will be returned (used for exiting loops).
                    return 0
            except:
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

    @staticmethod
    def format_amount(amount): # This method fixes the formatting involving negative numbers, dollar signs, and $x.x0, and converts to string.
        balance = str(amount)

        balance = balance.replace("-", "-$")  # Changes "-100" to "-$100" for example, i.e. negative amounts.
        if balance.count("$") == 0:
            balance = "$" + balance # Changes "100" to "$100", i.e. positive amounts.

        temp = balance.split(".") # Attempts to split amount by decimal. i.e., dollar amount and cent amount.

        if len(temp) == 1: # If there is no decimal, there will only be one array (i.e., only dollar amount).
            balance += (".00") # Changes "$1" to "$1.00"
        elif len(temp) == 2: # If there are also cent amount...
            if len(temp[1]) == 1: # Changes "$1.1" to "$1.10" for example.
                balance += ("0")

        return balance # Returns string of properly formatted money amount,
        

b1 = Bank("TD")
ap1 = Application()
ap1.run(b1)