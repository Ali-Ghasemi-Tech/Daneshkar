from account import Account
from random import randint
import re

class Bank:
    loan_budget= 1_000_000

    def __init__(self):
        self._accounts = {}
        self._accounts_id_dict = {}
 
    def _account_id(self) -> int:
        while True:
            id: int = randint(10_000 , 999_999)
            if not id in self._accounts_id_dict:
                return id
            continue

    def create_account(self, account_name:str, starting_amount: int | float, password : str) -> Account:
        print("*** account creation ***")
        account_id : int = self._account_id()
        account = Account(account_name , starting_amount, password , account_id)
        self._accounts[account.account_number]  = account
        self._accounts_id_dict[account_id] = account
        print(account)
        return account

    

    def open_account(self) -> None:
        print("*** Open account ***")
        user_name = input("What is the name for the new user account? ")
        start_amount = int(input("What is the starting amount of this account? "))
        user_pass = input("Enter a password for this account: ")

        user_account = self.create_account(user_name, start_amount, user_pass)
        print(f"Your new account number is: {user_account.account_number}\n" )
        print(f"Your account id is : {user_account.account_id}")
        return

    def close_account(self) -> None:
        print("**** Close Account ****")

        account_number = int(input("Enter account number: "))
        password = input("Enter password: ")

        account = self._accounts.get(account_number)

        if not (account):
            print("Account does not exist")
            return

        account.close_account(password)


    def diposit(self) -> None:
        print("*** diposit ***")
        account_number = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))
        password = input("Enter password: ")


        account = self._accounts.get(account_number)

        if not account:
            print("Account does not exists")
            return
        
        account.deposit(amount, password)
        

    def withdraw(self) -> None:
        print("*** withdraw ***")
        account_number = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))
        password = input("Enter password: ")


        account = self._accounts.get(account_number)

        if not account:
            print("Account does not exists")
            return
        
        account.withdraw(amount, password)


    def balance(self) -> None:
        """this will show the balance of an account"""
        print("*** Balance ***")
        account_number = int(input("Enter account number: "))


        account = self._accounts.get(account_number)

        if not account:
            print("Account does not exists")
            return
        
        account.get_balance()

    def show_account(self) -> dict:
        """this will show you the details of an account"""
        check_account = int(input("please enter a account id you want to monitor: "))
        if self._accounts_id_dict[check_account]:
            account = self._accounts_id_dict.get(check_account)
            account_string = re.split(r'[()]', str(account))
            detail_string = re.split(',' , account_string[1])
            return {'name':detail_string[0].strip()
                    , "balance":detail_string[1].strip()
                    , "password": detail_string[2].strip()
                    , "account_id" : detail_string[3].strip()}

        return "the account id you entered does not exist"



meli = Bank()
meli.open_account()
meli.balance()