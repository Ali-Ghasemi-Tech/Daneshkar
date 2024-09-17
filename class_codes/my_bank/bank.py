from account import Account
from random import randint
import re

class Bank:
    loan_budget = 1_000_000

    def __init__(self, name):
        self.bank_name = name
        self._accounts = {}
        self.accounts_id_dict = {}


    def get_account(self) -> str:
        account_id = int(input("please enter a the account id: "))
        if self.accounts_id_dict.get(account_id):
            return self.accounts_id_dict.get(account_id)
        else:
            return "this account does not exist"
        

    def _generate_id(self) -> int:
        while True:
            id: int = randint(10_000 , 999_999)
            if not id in self.accounts_id_dict:
                return id
            continue

    def create_account(self, account_name:str, starting_amount: int | float, password : str) -> Account:
        print("*** account creation ***")
        account_id : int = self._generate_id()
        account = Account(account_name , starting_amount, password , account_id)
        self._accounts[account.account_number]  = account
        self.accounts_id_dict[account_id] = account
        print(account)
        print()
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

        account_id = int(input("Enter account id: "))
        password = input("Enter password: ")

        account = self.accounts_id_dict.get(account_id)

        if not (account):
            print("Account does not exist")
            return

        account.close_account(password)


    def diposit(self) -> None:
        print("*** diposit ***")
        account_id = int(input("Enter account id: "))
        amount = int(input("Enter amount: "))
        password = input("Enter password: ")
        print()

        account = self.accounts_id_dict.get(account_id)

        if not account:
            print("Account does not exists")
            return
        
        account.diposit(amount, password)
        

    def withdraw(self) -> None:
        print("*** withdraw ***")
        account_id = int(input("Enter account id: "))
        amount = int(input("Enter amount: "))
        print()


        account = self.accounts_id_dict.get(account_id)

        if not account:
            print("Account does not exists")
            return
        
        account.withdraw(amount)


    def balance(self) -> None:
        """this will show the balance of an account"""
        print("*** Balance ***")
        account_id = int(input("Enter account id: "))
        print()
        account = self.accounts_id_dict.get(account_id)

        if not account:
            print("Account does not exists")
            return
        
        account.get_balance()
        

    def show_account(self) -> dict:
        """this will show you the details of an account"""
        check_account = int(input("please enter a account id you want to monitor: "))
        
        account = self.get_account(check_account)
        account_string = re.split(r'[()]', str(account))
        detail_string = re.split(',' , account_string[1])
        print ({'name':detail_string[0].strip()
                , "balance":detail_string[1].strip()
                , "password": detail_string[2].strip()
                , "account_id" : detail_string[3].strip()})
        return account
        

    def loan(self):
        print("*** loan page ***")
        account = self.get_account()
        credit = account.check_credit()
        if credit == 1:
            quilified = True
        else:
            quilified = False
        loan_amount = account._balance * 1.5
        if quilified:
            print("your account is quilified for a loan")
            print(f"the amount you can get as a loan is : {loan_amount}")
            
        else:
            print("you are not qulified for a loan")
        
        



meli = Bank("meli")
blue = Bank("blue")

#meli bank
print(f"the load budget for this bank is: {meli.loan_budget}")
print()
meli.create_account("ali", 1253 , "ali_pass")
meli.create_account("mmd", 2564 , "mmd_pass")
meli.create_account("amir", 256 , "amir_pass")
meli.create_account("kiyan", 9862 , "kiyan_pass")
# meli.loan() 
# print(meli.balance())

#blue bank
# blue.loan_budget = 5_000_000
# print(f"the load budget for this bank is: {blue.loan_budget}")
# print()
# blue.create_account("ali", 1253 , "ali_pass")
# blue.create_account("mmd", 2564 , "mmd_pass")
# blue.create_account("amir", 256 , "amir_pass")
# blue.create_account("kiyan", 9862 , "kiyan_pass")

