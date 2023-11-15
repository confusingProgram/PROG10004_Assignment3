from bank import Bank

class Application:
    def __init__(self):
        pass
    
    def show_main_menu(self, bank):
        print(f"Thank you for using {bank._bank_name}!")
        while True:
            print("------ Main Menu ------")
            print("[1] Select Account")
            print("[2] Open Account")
            print("[3] Exit Application")
            choice = input("Please enter an option: ").strip()

            if choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                self.select_account(bank)
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                self.open_account(bank)
            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                break
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
            print("[1] Chequing Account")
            print("[2] Savings Account")
            print("[3] Exit Creation")
            choice = input("Please enter an option: ").strip()

            if choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                while True:
                    name = input("Please enter a name: ").strip()
                    if name != "": # Checks that entry is not null.
                        bank.open_account("c", name) # Open chequing account.
                        break
                    else:
                        print("Name cannot be blank.")
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                while True:
                    name = input("Please enter a name: ").strip()
                    if name != "": # Checks that entry is not null.
                        bank.open_account("s", name) # Open chequing account.
                        break
                    else:
                        print("Name cannot be blank.")
            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                break # Exit
            else:
                print("Please enter valid option.")
                print("")

    def show_account_menu(self, account):
        while True:
            print("Welcome to account menu! Please select an option:")
            print("[1] Check Balance")
            print("[2] Deposit")
            print("[3] Withdraw")
            print("[4] Exit Account")
            choice = input("Please enter a number: ").strip()

            if choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                if account.get_current_balance() >= 0:
                    print(f"Balance: ${account.get_current_balance()}.")
                else:
                    print(f"Balance: -${account.get_current_balance()}.")
                    
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                account.deposit()
            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                account.withdraw()
            elif choice == "[4]" or choice == "[4" or choice == "4]" or choice == "4":
                break
            else:
                print("Please enter a valid number.")
                print("")

    def run(self, bank):
        self.show_main_menu(bank)

b1 = Bank("TD")
ap1 = Application()
ap1.run(b1)