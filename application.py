from bank import Bank

class Application:
    def __init__(self):
        self.accounts = ["1"]
    
    def show_main_menu(self):
        while True:
            print("Welcome to main menu! Please select an option:")
            print("[1] Select Account")
            print("[2] Open Account")
            print("[3] Exit Application")
            choice = input("Please enter an option: ").strip()
            if choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                self.select_account()
                pass
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                pass
            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                break
            else:
                print("Please enter valid number.")
                print("")

    def select_account(self):
        while True:
            print("------ Account Selection ------")
            id = input("Please enter the account number, or 0 to exit: ").strip()
            for account in self.accounts:
                #if id == account._id:
                if id == account:
                    print("Account found!")
                    self.show_account_menu(id)
            if id == "0":
                break
            else:
                print("Account number not found!")
                print("Please enter valid number.")

    def open_account(self):
        while True:
            print("------ Account Creation ------")
            print("Please select an option:")
            print("[1] Chequing Account")
            print("[2] Savings Account")
            print("[3] Exit Creation")
            choice = input("Please enter an option: ").strip()
            if choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                name = ""
                while True:
                    name = input("Please enter a name: ")
                    if name != "":
                        break
                    else:
                        print("Name cannot be blank.")
                #self.create_chequing(open_id(), name)
                pass
            elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                name = ""
                while True:
                    name = input("Please enter a name: ")
                    if name != "":
                        break
                    else:
                        print("Name cannot be blank.")
                #self.create_savings(open_id() name)
                pass
            elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                break
            else:
                print("Please enter valid number.")
                print("")

    

            


    def show_account_menu(self, id):
        for account in self.accounts:
                #if id == account._id:
                if id == account:
                    while True:
                        print("Welcome to account menu! Please select an option:")
                        print("[1] Check Balance")
                        print("[2] Deposit")
                        print("[3] Withdraw")
                        print("[4] Exit Account")
                        choice = input("Please enter a number: ").strip()
                        if choice == "[1]" or choice == "[1" or choice == "1]" or choice == "1":
                            #account.check_balance()
                            pass
                        elif choice == "[2]" or choice == "[2" or choice == "2]" or choice == "2":
                            #account.deposit()
                            pass
                        elif choice == "[3]" or choice == "[3" or choice == "3]" or choice == "3":
                            #account.withdraw()
                            pass
                        elif choice == "[4]" or choice == "[4" or choice == "4]" or choice == "4":
                            break
                        else:
                            print("Please enter a valid number.")
                            print("")


    def run(self):
        self.show_main_menu()

ap1 = Application()
ap1.run()