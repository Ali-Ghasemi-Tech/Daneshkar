from getpass import getpass
import uuid
import hashlib
from typing import Optional


def check_login(func):
    def wraper(self, *args , **kwargs):
        if self.logged_in:
            return func(self, *args, **kwargs)
        else:
            print("you are not logged in")
            return self.login()

    return wraper


class User:

    users = {}

    def __init__(self) -> None:

        self.logged_in =False


    def id_generator(self):   
        while True:
            id = uuid.uuid4()
            if str(id) in User.users:
                continue
            else:
                return str(id)
    
    
    def hash_password(self , password):
       encode_password = password.encode('utf-8')
       hash_object = hashlib.sha256(encode_password)
       hex_dig = hash_object.hexdigest()
       return hex_dig
    
    def create_user(self):
        user_name = input("please enter your username: ")
        user_pass = self.get_password()
        user_phone = input("please enter your phone number (optional): ")
        id = self.id_generator()
        if len(list(user_phone)) == 0:
            user_phone = None

        user = {"user_name": user_name , "user_pass": self.hash_password(user_pass) , "user_phone": user_phone , "user_id": id}

        User.users[id] = user
        self.logged_in = True
        return user
    
    def login(self):
        user_name = input("please enter your username: ")
        user_pass = getpass("please enter your passwrod: ")
        hashed_pass = self.hash_password(user_pass)

        for id in User.users:
            if User.users[id]["user_name"] == user_name and User.users[id]["user_pass"] == hashed_pass:
                self.logged_in = True
                print(f"you are loggen into this account {self.show_account(id)}\n")
                return self.User.users[id]
            else:
                print("your user_name or password is wrong\n")
                return False
            
    def show_account(slef , id):
        try:
            return User.users[id]
        except Exception:
            print(Exception)
    
    def get_password(self):
        user_pass = getpass("please enter your passwrod: ")
        valid_pass = self._check_password(user_pass)

        if not valid_pass:
            print("your password should be atleast 4 charecters long!")
            return self.get_password()
        return user_pass
     
    def _check_password(self , passwrod):
        if len(list(passwrod)) < 4:
            return False
        return True
    
    @check_login
    def __str__(self , account):
        return  f"user_name: {account["user_name"]}\n user_phone: {account["user_phone"]}\n user_id:{account["user_id"]}"

    
ali = User()

