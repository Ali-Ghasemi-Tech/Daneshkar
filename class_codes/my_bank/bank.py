from account import Account
from random import randint
import re

class Bank:

    def __init__(self, name , loan_intreast):
        self.loan_intreast = int(loan_intreast)
        self.bank_name = name
        self._accounts = {}
        self.accounts_id_dict = {}
        self.loan_budget = 1_000_000



    def get_account(self) -> str | bool:
        """get the accounts object"""
        try:
            account_id = int(input("please enter an account id: "))
        except ValueError:
            print("enter a number next time")
            return False
        if self.accounts_id_dict.get(account_id):
            return self.accounts_id_dict.get(account_id)
        else:
            return "this account does not exist"
        

    def _generate_id(self) -> int:
        """generate a random id for account between 10_000 and 999_999"""
        while True:
            id: int = randint(10_000 , 999_999)
            if not id in self.accounts_id_dict:
                return id
            continue

    def create_account(self, account_name:str, starting_amount: int | float, password : str , account_id = 0) -> Account:
        """create an account based on the name password and then initiate an id to it"""
        print("*** account creation ***")
        if account_id == 0:
            try:
                account_id : int = self._generate_id()
            except ValueError:
                print("enter a number next time")
                return
        
        account = Account(account_name , starting_amount, password , account_id)
        self._accounts[account.account_number]  = account
        self.accounts_id_dict[account_id] = account
        print(account)
        print()
        return account

    

    def open_account(self) -> None:
        """open an account from the user's request"""
        print("*** Open account ***")
        user_name = input("What is the name for the new user account? ")
        for account_id in self.accounts_id_dict:
            account =self.accounts_id_dict.get(account_id)
            account_string = re.split(r'[()]', str(account))
            detail_string = re.split(',' , account_string[1])
            if detail_string[0].strip() == user_name:
                print("this user name already exist in this bank")
                return
        try:
            start_amount = int(input("What is the starting amount of this account? "))
        except ValueError:
            print("please enter a number for starting amount next time , thank you")
            return
        user_pass = input("Enter a password for this account: ")

        user_account = self.create_account(user_name, start_amount, user_pass)
        print(f"Your new account number is: {user_account.account_number}\n" )
        print(f"Your account id is : {user_account.account_id}")
        return

    def close_account(self , account_id) -> None:
        """close the account by it's id"""
        print("**** Close Account ****")

        account = self.accounts_id_dict.get(account_id)

        if not (account):
            print("Account does not exist")
            return

        account.close_account()
    
    def reopen_account(self, account_id) -> None:
        """reopen account with it's id"""
        print("*** reopening account ***")
        account = self.accounts_id_dict.get(account_id)
        if not (account):
            print("Account does not exist")
            return

        account.reopen_account()


    def deposit(self, account_id) -> None:
        """deposit requested money into account"""
        print("*** deposit ***")
        try:
            amount = int(input("Enter amount you want to deposit: "))
        except ValueError:
            print("enter a number next time ")
            return
        print()

        account = self.accounts_id_dict.get(account_id)

        if not account:
            print("Account does not exists")
            return
        
        account.deposit(amount)
        

    def withdraw(self, account_id) -> None:
        """withdraw the amount of money from the account"""
        print("*** withdraw ***")
        try:
            amount = int(input("Enter amount you want to withdraw: "))
        except ValueError:
            print("enter a number next time ")
            return
        print()


        account = self.accounts_id_dict.get(account_id)

        if not account:
            print("Account does not exists")
            return
        account.block_balance(amount)
        account.withdraw(amount)


    def balance(self , account_id) -> None:
        """this will show the balance of an account"""
        print("*** Balance ***")
        print()
        account = self.accounts_id_dict.get(account_id)

        if not account:
            print("Account does not exists")
            return
        
        account.get_balance()
        

    def show_account(self) -> dict:
        """this will show you the details of an account"""        
        account = self.get_account()
        if account == "this account does not exist":
            print("wrong account id")
            return
        account_string = re.split(r'[()]', str(account))
        detail_string = re.split(',' , account_string[1])
        print ({'name':detail_string[0].strip()
                , "balance":detail_string[1].strip()
                , "password": detail_string[2].strip()
                , "account_id" : detail_string[3].strip()})
        return account
        

    def loan(self , account):
        """check user's credit and give loan suggestion based on balance"""
        print("*** loan page ***")
        credit = account.check_credit()
        if credit == 1:
            quilified = True
        else:
            quilified = False
        
        loan_amount = account._balance * 1.5
        if loan_amount > self.loan_budget:
            loan_amount = self.loan_budget
        if quilified:
            print("your account is quilified for a loan")
            print(f"the amount you can get as a loan is : {loan_amount}")
            while True:
                procced = input("do you want to continue (y/n)? ")
                if procced.lower() == 'y':
                    print(f"take note that the loan intreast is {self.loan_intreast}%")
                    try:
                        money_request = int(input("how much money do you request for your loan: "))
                    except ValueError:
                        print("please enter a number next time")
                        continue
                    if money_request > loan_amount:
                        print(f"your max debt can be {loan_amount}")
                    else:
                        account.deposit(money_request)
                        account._debt = money_request * (1 +(self.loan_intreast / 100))
                        self.loan_budget -= money_request
                        print(f'your loan has been confirmed. your account balance is {account._balance}')
                        print(f"your account debt is {account._debt}")
                        print("thanks for choosing our bank")
                        break
                elif procced.lower() == 'n':
                    break
                else:
                    print("incorect input")
                    continue
        else:
            print("you are not qulified for a loan")
        
        






