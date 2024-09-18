from bank import Bank
import main

def login_required(func):
    def wraper(self, *args , **kwargs):
        if self.logged_in :
            return func(self ,*args , **kwargs)
        else:
            print("account not logged in!")
            return self.login()
    return wraper

class User:
    def __init__(self , bank):
        self.logged_in = False
        self.current_account = None
        self.bank = None
        self.account_id = None


    def login(self):
        bank_name = input("which bank do you have an account at: ")
        if bank_name == "meli":
            self.bank = main.meli
            bank_accounts = main.meli.accounts_id_dict
        elif bank_name == "blue":
            self.bank = main.blue
            bank_accounts = main.blue.accounts_id_dict
        else :
            print("entered bank does not exist!")
        
        while True:
            name = input("please enter your username: ")
            password =input("please enter your password: ")
            print(bank_accounts)
            account = self.bank.get_account()
            
            if type(account) == 'str' and account.name == name and account.password == password:
                self.account_id = account.account_id
                self.logged_in = True
                self.current_account = account
                print("logged in successfuly!")
                break
            else:
                print("invalid username , password or account id!")
                choice = input("do you want to cancel login(y/n): ")
                if choice.lower() == "y":
                    print("login canceled")
                    return False


    @login_required
    def req_balance(self):
        print(f"your balance is {self.bank.balance(self.account_id)} $")

    @login_required
    def req_withdraw(self):
        amount = int(input("please enter an amount you want to withdraw: "))
        self.current_account.block_balance(amount)
        self.current_account.withdraw(amount)
    
    @login_required
    def req_deposit(self):
        amount = int(input("please enter the amount you want to deposit: "))
        self.current_account.deposit(amount)

    @login_required
    def req_loan(self):
        pass
        

ali = User()
ali.req_balance()
ali.req_withdraw()
ali.req_balance()
ali.req_deposit()
