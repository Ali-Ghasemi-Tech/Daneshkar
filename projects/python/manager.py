from modules import password
class Manager:
    def __init__(self , user_account) -> None:
        self.user_account = user_account


    def create_account(self):
        user_pass = password.get_password()
        try:
            starting_amount = int(input("enter your starting amount: "))
        except ValueError:
            print("please enter a number")