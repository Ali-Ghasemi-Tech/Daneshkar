from account import Account

class Bank:
    def __init__(self):
        self._accounts = {}

    def create_account(self, account_name, starting_amount, password):
        print("*** attempt to create an acount ***")
        account = Account(account_name, starting_amount, password)
        self._accounts[account.account_number: account]

        return account



    def open_account(self):
        print("*** Open account ***")
        user_name = input("What is the name for the new user account? ")
        start_amount = int(input("What is the starting amount of this account? "))
        user_pass = input("Enter a password for this account: ")

        user_account = self.create_account(user_name, start_amount, user_pass)
        print(f"Your new account number is: {user_account.account_number}\n" )

    def close_account(self):
        print("**** Close Account ****")

        account_number = input("Enter account number: ")
        password = input("Enter password: ")

        account = self._accounts.get(account_number)

        if not (account):
            print("Account does not exist")
            return

        account.close_account(password)


    def diposit(self):
        print("*** Balance ***")
        account_number = input("Enter account number: ")
        amount = int(input("Enter amount"))
        password = input("Enter password: ")


        account = self._accounts.get(account_number)

        if not account:
            print("Account does not exists")
            return
        
        account.deposit(amount, password)
        

    def withdraw(self):
        pass


    def balance(self):
        pass



b1 = Bank()

