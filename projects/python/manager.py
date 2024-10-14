from modules import password
from modules import isDigit
from modules import validBank
from bank_account import BankAccount


class Manager:
    selected_bank_account = None

    def __init__(self , user_account , bank_accounts) -> None:
        self.user_account = user_account
        self.bank_accounts = bank_accounts


    def create_account(self) -> BankAccount:
        bank = validBank.get_bank(self.bank_accounts)
        user_pass = password.get_password()
        hased_pass = password.hash_password(user_pass)
        starting_amount = isDigit.get_initial_amount()
        cvv2 = isDigit.get_cvv2()

        new_bank_account = BankAccount(bank , self.user_account["user_name"] , starting_amount , hased_pass , cvv2)

        self.bank_accounts.append(new_bank_account)
        return new_bank_account
    
    def get_bank_account(self) -> BankAccount:
        bank_choice = input("enter the bank's name you want to work with: ")
        for i in self.bank_accounts:
            if i.bank == bank_choice:
                Manager.selected_bank_account = i
                return i
        print("this bank account does not exist!")
        return self.get_bank_account()
    
    def wallet_funds(self) -> None:
        if self.get_bank_account():
            user_input = input("please enter the amount you want to add to your wallet: ")
            charging_amount =  isDigit.number_valid(user_input)
            Manager.selected_bank_account.withdraw(charging_amount)

            self.user_account["wallet_balance"] += charging_amount
            wallet_balance  = self.user_account["wallet_balance"]
            
            print(f"your wallet balance is {wallet_balance}")
            
            bank_balance = Manager.selected_bank_account.get_balance() - charging_amount
            return bank_balance
        return
        