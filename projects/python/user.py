from getpass import getpass
import uuid
from datetime import datetime
import jdatetime
from Modules import password


def check_login(func):
    def wraper(self, *args , **kwargs):
        if self.logged_in:
            return func(self, *args, **kwargs)
        else:
            print("you are not logged in")
            return self.login()

    return wraper


class User:

    users : dict = {}

    def __init__(self) -> None:

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

        creation_date = datetime.now().date()

        user = {
                "user_name": user_name ,
                "user_pass": password.hash_password(user_pass) ,
                "user_phone": user_phone , "user_id": id ,
                "date_of_birth" : user_birth ,
                "age" : age ,
                "creation_date" : creation_date,
                "bank_accounts" : [],
                "wallet_balance" : 0,
                "subscription" : "bronze",
                }

        User.users[id] = user
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
            return User.users[id]
        except Exception:
            print(Exception)


    def get_birthdate(self):
        try:
            user_input = input("please enter your date of birth in jalili calander(YYYY/MM/DD): ")
            return datetime.strptime(user_input , "%Y/%m/%d").date()
        except Exception:
            print("wrong format or input. try again")
            return self.get_birthdate()

    def calculate_age(self , date):
        now = jdatetime.datetime.now().date()
        return (now.year - date.year)

    def get_user_name(self) -> str :
        """gets user_name from dict and if the user_name already exist then retruns itself until the input user_name does not exist
        
        return string"""
        user_name : str = input("please enter username: ")
        name_exist : bool = self._check_username(user_name)
        if name_exist:
            print("\nthis user_name already exists , please enter another user_name! (╥‸╥) \n")
            return self.get_user_name()
        return user_name
    
    def _check_username(self , new_user_name) -> bool:
        """check if the user_name exist in the users
        
        returns boolian"""
        for id in User.users:
            if User.users[str(id)]["user_name"] == new_user_name:
                return True
        
        return False


    @staticmethod
    def update_pass(password , id) -> None:
        """this jsut updates the preivous password to the new one
        
        gets id
        
        returns None"""
        User.users[id]["user_pass"] = password
    
    @check_login
    def __str__(self , account) -> str:
        """stringifyin the user info , except password
        
        gets account

        returns string"""
        return  f"user_name: {account["user_name"]}\n user_phone: {account["user_phone"]}\n user_id:{account["user_id"]}\n wallet_balance: {account["wallet_balance"]}"
    
