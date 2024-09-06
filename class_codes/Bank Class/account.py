class Account:
    number_of_created_account = 0

    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self._block_balance = 0
        self.password = password
        Account.number_of_created_account += 1


        self.is_closed = False
        self.account_number = Account.number_of_created_account

    def _check_account_state(self, amount, password):
        if self.is_closed:
            print("Sorry your account is blocked.")

        if password != self.password:
            print("Sorry! incorrect password")
            return False
        
        if amount < 0:
            print("You can not use negative amount")
            return False
        
        return True

    
    def deposit(self, amount, password) -> bool:
        flag = self._check_account_state(amount, password)

        if flag:
            self._balance += amount

        return flag

    def withdraw(self, amount, password):
        flag = self._check_account_state(amount, password)

        if flag:
            self._block_balance -= amount
            self._balance -= amount

        return flag
    

    def block_balance(self, amount, password):
        flag = self._check_account_state(amount, password)

        if flag:
            self._block_balance += amount

        return flag


    def get_balance(self):
        return self._balance - self._block_balance
    
    def close_account(self, password):
        if not self._check_account_state(0, password):
            return False
        
        self.is_closed = True


    def reopen_account(self, password):
        if not self._check_account_state(0, password):
            return False
        
        self.is_closed = False
        
    
    def __str__(self):
        return f"{self.name} {self.get_balance()}"


a1 = Account("Joe", 100, "joe_pass")
a2 = Account("Mary", 12345, "mary_pass")

print(a1)
print(a2)


a1.deposit(100, "joe_pass")
print(a1)

a2.block_balance(100)
# Open back gateway


# response from bank
a2.withdraw(100, "mary_pass")
print(a2)

