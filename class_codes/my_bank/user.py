from bank import Bank

def login_required(func):
    def wraper(self, *args , **kwargs):
        if self.logged_in :
            return func(self ,*args , **kwargs)
        else:
            print("account not logged in!")
            return self.login()
    return wraper

class User:
    def __init__(self):
        self.logged_in = False
        self.current_account = None


    def login(self):
        bank_name = input("which bank do you have an account at: ")
        bank = Bank(bank_name)
        bank.create_account("ali", 1253 , "ali_pass")
        while True:
            name = input("please enter your username: ")
            password =input("please enter your password: ")
            account_id = int(input("please enter your account id: "))
            print(bank.accounts_id_dict)
            account = bank.accounts_id_dict.get(account_id)
            if account and account.name == name and account.password == password:
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
        print(f"your balance is {self.current_account._balance} $")

    @login_required
    def req_withdraw(self):
        amount = int(input("please enter an amount: "))
        self.current_account.withdraw(amount)
        

ali = User()
ali.req_balance()
ali.req_withdraw()
ali.req_balance()
