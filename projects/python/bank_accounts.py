import hashlib
import jdatetime
from getpass import getpass
class Account:

    accounts= {}

    def __init__(self , name):
        self.is_closed = False
        self.name = name


    def create_account(self):
        print("\n\n*** account creation page ***\n\n")
        user_name = self.name
        bank = input("please enter the name of the bank your account is at: ")
        user_pass = self.get_password()
        try:
            cvv2 = int(input("enter your cards CVV2 code: "))
            balance = int(input("please enter your initial balance: "))
        except ValueError:
            print("wrong input, please enter a number next time!!!")
            return 
       
        id = len(Account.accounts) + 1
        
        #this does not work fix it
        creation_date = jdatetime.datetime.now().date()
       

        account = {
                "bank": bank ,
                "user_name": user_name ,
                "user_pass": self.hash_password(user_pass) ,
                "balance": balance,
                "cvv2": cvv2,
                "creation_date" : creation_date,
                }
        Account.accounts[id] = account
        return Account.accounts


    def get_password(self) -> str :
        """handels getting password from user and checking it. if the password is not valid then it returns itself
        
        returns string"""
        user_pass: str = getpass("please enter passwrod: ")
        valid_pass: function = self._check_password(user_pass)

        if not valid_pass:
            print("\nyour password should be atleast 4 charecters long! –_–)#\n")
            return self.get_password()
        return user_pass
    
    def hash_password(self , password) -> str:
       """this is a function for getting password as input and then hashes it using hashlib 
       
        gets password

       returns string"""
       encode_password = password.encode('utf-8')
       hash_object = hashlib.sha256(encode_password)
       hex_dig = hash_object.hexdigest()
       return hex_dig
    
    def _check_password(self , passwrod) -> bool:
        """checking if password is atleast 4 charectors long
        
        returns boolian"""
        if len(list(passwrod)) < 4:
            return False
        return True
    
    def _check_amount(func) -> bool:
        def wraper(*args):
            if args[1] < 0:
                print("You can not use negative amount")
                return False
            return func(*args)
        return wraper

    def _check_closed(func) -> bool:
        def wraper(*args):
            if args[0].is_closed:
                print("Sorry your account is blocked.")
                return False
            return func(*args)

            
        return wraper   
    
    @_check_closed
    @_check_amount
    def deposit(self, amount: int) -> bool:
        self._balance += amount
        print("your deposit was succesful\n")
        return True


    @_check_closed
    @_check_amount
    def withdraw(self, amount: int) -> bool:
        if self._balance - amount > 10:
            self._blocked_balance -= amount
            self._balance -= amount
            print("your withdraw was succesful\n")
            return True
        print("could't withdraw\n")
        return False

    
    @_check_closed
    @_check_amount
    def block_balance(self, amount: int) -> bool:

        self._blocked_balance += amount
        return True


    def get_balance(self) -> int:
        balance = self._balance - self._blocked_balance
        print(f"the balance of this account is: {balance}$")
        return balance
        

    @_check_closed
    def close_account(self) -> bool:
       
        self.is_closed = True
        print(f"the following account has been closed: {self}")
        return True

    @_check_closed
    def reopen_account(self) -> bool:
        self.is_closed = False
        return True
    
    def check_credit(self):
        # hard coded this account age so you can see the loan method in action
        account_age = 31
        if account_age > 30:
            if self._balance > 1000 and self._debt == 0 : 
                self._credit = 1
                return self._credit
            else:
                print("insufficient balance for getting credit")
                return self._credit
        else:
            print(f"too new for getting credit. try again in {30 - account_age} day(s)")
 
        
    def __str__(self) -> str:
        return f'Account({self.name} , {self._balance} , {self.password} , {self.account_id})'

    def __repr__(self) -> str:
        return f'Account({self.name!r} , {self._balance!r} , {self.password!r} , {self.account_id!r})'
    
ali = Account("ali")
ali.create_account()
for i in ali.accounts:
    for j in ali.accounts[i]:
        print(f"{j} : {ali.accounts[i][j]}")