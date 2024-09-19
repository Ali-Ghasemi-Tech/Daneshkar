from datetime import datetime 

class Account:
    number_of_created_account = 0

    def __init__(self, name, balance, password , account_id):
        self.name = name
        self._balance = balance
        self._blocked_balance = 0
        self.password = password
        self.account_id = account_id
        Account.number_of_created_account += 1
        self._creation_date = datetime.now()
        self._credit = 0
        self._debt = 0


        self.is_closed = False
        self.account_number = Account.number_of_created_account
        self.account_id = account_id

    # the password will be checked when user has logged in .

        
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



