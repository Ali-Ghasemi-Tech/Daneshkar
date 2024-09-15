class Account:
    number_of_created_account = 0

    def __init__(self, name, balance, password , account_id):
        self.name = name
        self._balance = balance
        self._block_balance = 0
        self.password = password
        self.account_id = account_id
        Account.number_of_created_account += 1


        self.is_closed = False
        self.account_number = Account.number_of_created_account
        self.account_id = account_id

    def _check_account_state(self, amount: int, password: str) -> bool:
        if self.is_closed:
            print("Sorry your account is blocked.")
            return False

        if password != self.password:
            print("Sorry! incorrect password")
            return False
        
        if amount < 0:
            print("You can not use negative amount")
            return False
        
        return True

    
    def deposit(self, amount: int, password:str) -> bool:
        flag = self._check_account_state(amount, password)

        if flag:
            self._balance += amount

        return flag

    def withdraw(self, amount: int, password: str) -> bool:
        flag = self._check_account_state(amount, password)

        if flag:
            self._block_balance -= amount
            self._balance -= amount

        return flag
    

    def block_balance(self, amount: int, password: str) -> bool:
        flag = self._check_account_state(amount, password)

        if flag:
            self._block_balance += amount

        return flag


    def get_balance(self) -> int:
        print(self._balance - self._block_balance)
        return self._balance - self._block_balance
        
    
    def close_account(self, password: str) -> bool:
        if not self._check_account_state(0, password):
            return False
        
        self.is_closed = True
        print(f"the following account has been blocked: {self}")


    def reopen_account(self, password : str) -> bool:
        if not self._check_account_state(0, password):
            return False
        
        self.is_closed = False
        
    def __str__(self) -> str:
        return f'Account({self.name} , {self._balance} , {self.password} , {self.account_id})'

    def __repr__(self) -> str:
        return f'Account({self.name!r} , {self._balance!r} , {self.password!r} , {self.account_id!r})'




