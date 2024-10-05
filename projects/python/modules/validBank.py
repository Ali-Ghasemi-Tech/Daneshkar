def check_bank(bank_account_list , new_bank):
    for bank_account in bank_account_list:
        if new_bank == bank_account.bank:
            return False
    return True

def get_bank(bank_account_list):
    bank = input("enter the name of your bank: ")
    if not check_bank(bank_account_list , bank):
        print("you already have an account in this bank! enter a new bank")
        return get_bank(bank_account_list)
    return bank