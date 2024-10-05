from modules import password
from modules import isDigit
from modules import validBank
from bank_account import BankAccount
class Manager:
    def __init__(self , user_account , bank_accounts) -> None:
        self.user_account = user_account
        self.bank_accounts = bank_accounts


    def create_account(self):
        bank = validBank.get_bank(self.bank_accounts)
        user_pass = password.get_password()
        hased_pass = password.hash_password(user_pass)
        starting_amount = isDigit.get_initial_amount()
        cvv2 = isDigit.get_cvv2()

        new_bank_account = BankAccount(bank , self.user_account , starting_amount , hased_pass , cvv2)

        updated_bank_accounts = self.bank_accounts.append(new_bank_account)

        return updated_bank_accounts
    
ali = Manager("ali" , [])
ali.create_account()
ali.create_account()
print(ali.bank_accounts)