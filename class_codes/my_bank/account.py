"""
re doing the Account class

"""
class Account:
    account_number = 0


    def __init__(self , name, password , balance):
        self._name = name
        self._password = password
        self._balance = balance
        self._acc_block_balance = 0

        Account.account_number += 1
        self.closed = False


    def _account_state(self , password , amount):
        if self.closed:
            print("sorry your account is blocked")
            return False
        if password != self._password:
            print("incorrect password")
            return False
        if amount < 0:
            print('your entered number can not be negetive!!!')
            return False
        return True


    def deposit(self , amount , password):
        flag = self._account_state( password , amount)
        if flag:
            self._balance += amount
            print(self.get_balance())
            return
    

    def withdraw(self, amount ,password):
        flag = self._account_state( password , amount)
        if flag and self._balance - amount > 10:
            self._balance -= amount
            self._acc_block_balance -= amount 
            print(self.get_balance())
            return
        print (f"your balance is {self.get_balance()}. you can't withdraw this much (10 dollars should remain in account)")
        


    def get_balance(self):
        return f"your balance is: {self._balance}"
    

    def block_balance(self , amount , password):
        flag = self._account_state(amount , password)
        if flag:
            self.block_balance += amount


    def close_account(self , password):
        if self._account_state(password , 0):
            self.closed = True
            print(f"{self} has been blocked")
            return
        self.closed = False
        print(self.closed)


    def __repr__(self):
        return (f"Account({self._name!r} , {self._password!r} , {self._balance!r})")


# ali = Account('ali' , "tlb" ,1000)

# print(ali.deposit(100 , "tlb"))
# print(ali.block_balance(100 , "tlb"))
# print(ali.get_balance())
# print(ali)