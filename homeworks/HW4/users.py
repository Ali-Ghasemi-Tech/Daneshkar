from getpass import getpass
import uuid
import hashlib
from typing import Optional

class User:

    users = {}

    id = 0
    def __init__(self) -> None:

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
        user_pass = getpass("please enter your passwrod: ")
        user_phone = input("please enter your phone number (optional): ")
        user = {"user_name": user_name , "user_pass": self.hash_password(user_pass) , "user_phone": user_phone}
        User.users[self.id] = user
        return user
       
    

# ali = User("ali" , "ali_pass")

# ali.id_generator()