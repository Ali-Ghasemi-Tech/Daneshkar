from account import Account

class Bank:
    _accounts = {}

    def __init__(self):
        pass

    def deposit(self):
        print("*** deposit ***")
        account_number = int(input("enter the account number you want to deposit to: "))
        password = input("please enter the password of the account you want to deposit to: ")
        amount = int(input("please enter the amount you want to deposit: "))
        acc = self._accounts.get(account_number)
        if not acc:
            print("this account does not exist")
            return
        acc.deposit(amount , password)

    def withdraw(self):
        print("*** withdraw ***")
        account_number = int(input("enter the account number you want to withdraw from: "))
        password = input("please enter the password of the account you want to withdraw from: ")
        amount = int(input("please enter the amount you want to withdraw from this account: "))
        acc = self._accounts.get(account_number)
        if not acc:
            print("this account does not exist")
            return
        acc.withdraw(amount , password)

    def close_acc(self):
        print("*** closing account ***")
        account_number = int(input("enter the account number you want to block: "))
        password = input("please enter the password of the account you want to block: ")
        acc =self._accounts.get(account_number)
        if not acc :
            print('this account does not exist')
            return
        acc.close_account(password)

    def open_acc(self):
        print("*** opening account ***")
        user_name = input("please enter a username for your account: ")
        user_pass = input("please enter a passowrd for your account: ")
        starting_amount = int(input("please enter a starting amount for your account: "))
        self.create_acc(user_name , user_pass , starting_amount)

    def create_acc(self, user_name , user_pass , starting_amount):
        print("*** account creation ***")
        account = Account(user_name , user_pass , starting_amount)
        self._accounts[account.account_number]  = account

        print(self._accounts)

    def loan():
        pass


ali = Bank()
behnam = Bank()

acc = ali.create_acc("ali" , "ali_pass" , 1000)
acc2 = behnam.create_acc('behnam' , 'behnam_pass' ,2000)


behnam.deposit()



