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

        new_bank_account = BankAccount(bank , self.user_account["user_name"] , starting_amount , hased_pass , cvv2)

        self.bank_accounts.append(new_bank_account)
        return new_bank_account
