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
    """ this class is for loging users in and make thier use of the app more conviniant"""
    def __init__(self , bank):
        self.logged_in = False
        self.current_account = None
        self.bank = bank
        self.account_id = None


    def login(self) -> bool | None:
        """by entering name , password and account id you can log in and stay logged in until you want"""
        while True:
            name = input("please enter your username: ")
            password =input("please enter your password: ")
            account = self.bank.get_account()
            if account != "this account does not exist" and account != False and account.name == name and account.password == password:
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
    def req_balance(self) -> None:
        """request bank for getting user's account balance"""
        self.bank.balance(self.account_id)

    @login_required
    def req_withdraw(self) -> None:
        """request bank for withdrawing money from user's account"""
        self.bank.withdraw(self.account_id)
    
    @login_required
    def req_deposit(self) -> None:
        """request bank for depositing money into the user's account"""
        self.bank.deposit(self.current_account)

    @login_required
    def req_loan(self) -> None:
        """request bank for getting a loan on user's account"""
        self.bank.loan(self.current_account)

    def req_close(self) -> None:
        """request bank for closing the user's account"""
        self.bank.close_account(self.account_id)


    def req_reopen(self) -> None:
        """request bank for reopening user's account"""
        self.bank.reopen_account(self.account_id)

    @login_required
    def logout(self) -> None:
        """logging out of user's account"""
        self.logged_in = False
        print("***you have been logged out***")
        
