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
    def __init__(self , bank):
        self.logged_in = False
        self.current_account = None
        self.bank = bank
        self.account_id = None


    def login(self):
        while True:
            name = input("please enter your username: ")
            password =input("please enter your password: ")
            account = self.bank.get_account()
            if account != "this account does not exist" and account.name == name and account.password == password:
                self.account_id = account.account_id
                print(self.account_id)
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
                continue


    @login_required
    def req_balance(self):
        self.bank.balance(self.account_id)

    @login_required
    def req_withdraw(self):
        try:
            amount = int(input("please enter an amount you want to withdraw: "))
        except ValueError:
            print("please enter a number next time")
            return
        self.current_account.block_balance(amount)
        self.current_account.withdraw(amount)
    
    @login_required
    def req_deposit(self):
        try:
            amount = int(input("please enter the amount you want to deposit: "))
        except ValueError:
            print("please enter a number next time")
            return
        self.current_account.deposit(amount)

    @login_required
    def req_loan(self):
        self.bank.loan(self.current_account)

    @login_required
    def logout(self):
        self.logged_in = False
        print("***you have been logged out***")
        
