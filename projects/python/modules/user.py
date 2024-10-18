from getpass import getpass
import uuid
import jdatetime
from . import password
from enum import Enum
import json

def check_login(func):
    def wraper(self, *args , **kwargs):
        if self.logged_in:
            return func(self, *args, **kwargs)
        else:
            print("you are not logged in")
            return self.login()

    return wraper

with open('db/users.json' , 'r') as file:
    data = json.load(file)

class UserPermission(Enum):
    ADMIN = "admin"
    USER = "user"

class User:

    users:dict = data["users"]
    admins:dict = data["admins"]

    def __init__(self , permission) -> None:
        self.permission = permission
        self.logged_in: bool =False


    def id_generator(self) -> str: 
        """id_generator is a function for generating uuid ids 
         
        returns string"""  
        while True:
            id = uuid.uuid4()
            if str(id) in User.users:
                continue
            else:
                return str(id)
    
    def get_user_name(self) -> str :
        """gets user_name from dict and if the user_name already exist then retruns itself until the input user_name does not exist
        
        return string"""
        user_name : str = input("please enter username: ")
        name_exist : bool = self._check_username(user_name)
        if name_exist:
            print("\nthis user_name already exists , please enter another user_name! (╥‸╥) \n")
            return self.get_user_name()
        return user_name
    
    def get_admin_name(self) -> str :
        """gets user_name from dict and if the user_name already exist then retruns itself until the input user_name does not exist
        
        return string"""
        admin_name : str = input("please enter username: ")
        name_exist : bool = self._check_adminname(admin_name)
        if name_exist:
            print("\nthis user_name already exists , please enter another user_name! (╥‸╥) \n")
            return self.get_admin_name()
        return admin_name
    

    def _check_username(self , new_user_name) -> bool:
        """check if the user_name exist in the users
        
        returns boolian"""
        for id in User.users:
            if User.users[id]["user_name"] == new_user_name:
                return True
        
        return False
    
    def _check_adminname(self , new_admin_name) -> bool:
        """check if the user_name exist in the users
        
        returns boolian"""
        for id in User.admins:
            if User.admins[id]["admin_name"] == new_admin_name:
                return True
        
        return False
    
    def create_admin(self):
        """when called it asks admin for admin_name and password , it creates a dict with this information and also adds a random id to it then pushes it to the users dict 
        
        returns dict"""
        admin_name = self.get_admin_name()
        admin_pass = password.get_password()
        admin_phone = input("please enter your phone number (optional): ")
        id = self.id_generator()
        if len(list(admin_phone)) == 0:
            admin_phone = None

        creation_date = jdatetime.datetime.now().date()

        admin = {
                "admin_name": admin_name ,
                "admin_pass": password.hash_password(admin_pass) ,
                "admin_phone": admin_phone ,
                "admin_id": id ,
                "creation_date" : creation_date,
                "bank_accounts" : [],
                "wallet_balance" : 0,
                "permission" : self.permission
                }

        self.logged_in = True
        return admin
    
    def admin_login(self) -> dict:
        """handels login with user_name and password 
        
        returns dict"""
        admin_name = input("please enter your username: ")
        admin_pass = getpass("please enter your passwrod: ")
        hashed_pass = password.hash_password(admin_pass)

        for id in User.admins:
            if User.admins[id]["admin_name"] == admin_name and User.admins[id]["admin_pass"] == hashed_pass:
                self.logged_in = True
                # next line has been used for checking the account and now is commented for account safety
                # print(f"you are loggen into this account {self.show_account(id)}\n")
                return User.admins[id]
            
        print('your user_name or password is wrong (¬_¬") \n')
        return False

    def create_user(self) -> dict:
        """when called it asks user for user_name and password , it creates a dict with this information and also adds a random id to it then pushes it to the users dict 
        
        returns dict"""
        user_name = self.get_user_name()
        user_pass = password.get_password()
        user_phone = input("please enter your phone number (optional): ")
        user_birth = self.get_birthdate()
        age = self.calculate_age(user_birth)
        id = self.id_generator()
        if len(list(user_phone)) == 0:
            user_phone = None

        creation_date = jdatetime.datetime.now().date()

        user = {
                "user_name": user_name ,
                "user_pass": password.hash_password(user_pass) ,
                "user_phone": user_phone , "user_id": id ,
                "date_of_birth" : user_birth ,
                "age" : age ,
                "creation_date" : creation_date,
                "bank_accounts" : [],
                "wallet_balance" : 0,
                "subscription" : {"sub" : "bronze" , "used" : 0 , "date" : creation_date} ,
                "tickets": {},
                "permission" : self.permission
                }

        self.logged_in = True
        return user
    
    def login(self) -> dict:
        """handels login with user_name and password 
        
        returns dict"""
        user_name = input("please enter your username: ")
        user_pass = getpass("please enter your passwrod: ")
        hashed_pass = password.hash_password(user_pass)

        for id in User.users:
            if User.users[id]["user_name"] == user_name and User.users[id]["user_pass"] == hashed_pass:
                self.logged_in = True
                # next line has been used for checking the account and now is commented for account safety
                # print(f"you are loggen into this account {self.show_account(id)}\n")
                return User.users[id]
            
        print('your user_name or password is wrong (¬_¬") \n')
        return False
            
    def show_account(slef , id) -> dict:
        """shows account info with it's id

        gets id
        
        returns dict"""
        try:
            if User.users[id]:
                return User.users[id]
            elif User.admins[id]:
                return User.admins[id] 
        except Exception:
            print(Exception)


    def get_birthdate(self):
        try:
            user_input = input("please enter your date of birth in jalili calander(YYYY/MM/DD): ")
            return jdatetime.datetime.strptime(user_input , "%Y/%m/%d").date()
        except Exception:
            print("wrong format or input. try again")
            return self.get_birthdate()

    def calculate_age(self , date):
        now = jdatetime.datetime.now().date()
        return (now.year - date.year)

    
    @staticmethod
    def update_pass(password , id) -> None:
        """this jsut updates the preivous password to the new one
        
        gets id
        
        returns None"""
        User.users[id]["user_pass"] = password
        return User.users[id]
        
    @staticmethod
    def update_admin_pass(password , id) -> None:
        """this jsut updates the preivous password to the new one
        
        gets id
        
        returns None"""
        
        User.admins[id]["admin_pass"] = password
        return User.admins[id]
    

    @check_login
    def __str__(self , account) -> str:
        if account['permission'] == "user":
            """stringifyin the user info , except password
            
            gets account

            returns string"""
            return  f"\nuser_name: {account["user_name"]}\n user_phone: {account["user_phone"]}\n user_id:{account["user_id"]}\n wallet_balance: {account["wallet_balance"]}\n tickets: {account["tickets"]}\n subscription: {account["subscription"]}\n bank accounts:{account["bank_accounts"]}\n date of birth: {account["date_of_birth"]}\n permission: {account["permission"]}\n"
    
        elif account["permission"] == "admin":
    
            return  f"\nadmin_name: {account["admin_name"]}\n admin_phone: {account["admin_phone"]}\n admin_id:{account["admin_id"]}\n wallet_balance: {account["wallet_balance"]}\n   bank accounts:{account["bank_accounts"]}\n permission: {account["permission"]}\n"