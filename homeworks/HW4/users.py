from getpass import getpass
import uuid
import hashlib
from typing import Optional


def login(func):
    def wraper(self, *args , **kwargs):
        if self.logged_in:
            return func(self, *args, **kwargs)
        else:
            print("you are not logged in")
            return self.login()

    return wraper


class User:

    users = {}

    id = 0
    def __init__(self) -> None:
        self.logged_in =False
        self.id = self.id_generator()

    def id_generator(self):   
        while True:
            id = uuid.uuid4()
            if id in User.users:
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
        user = {"user_name": user_name , "user_pass": self.hash_password(user_pass) , "user_phone": user_phone}
        User.users[self.id] = user
        return user
    
    def login(self):
        user_name = input("please enter your username: ")
        user_pass = getpass("please enter your passwrod: ")
        hashed_pass = self.hash_password(user_pass)
        for id in User.users:
            if User.users[id]["user_name"] == user_name and User.users[id]["user_pass"] == hashed_pass:
                self.logged_in = True
                print(f"you are loggen into this account {self.show_account(id)}\n")
                return True
            else:
                print("your user_name or password is wrong\n")
                return False
            
    def show_account(slef , id):
        try:
            return User.users[id]
        except Exception:
            print(Exception)

    def __str__(self , pram):
        return  str(pram)
    
    def get_password(self):
        user_pass = getpass("please enter your passwrod: ")
        valid_pass = self.check_password(user_pass)
        if not valid_pass:
            print("your password should be atleast 4 charecters long!")
            return self.get_password()
        return user_pass
     
    def check_password(self , passwrod):
        if len(list(passwrod)) < 4:
            return False
        return True
    
# ali = User("ali" , "ali_pass")

# ali.id_generator()