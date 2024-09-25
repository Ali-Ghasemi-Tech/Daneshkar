
from users import User
from getpass import getpass
while True:
    user_choice = int(input("please enter the number of task you want to execute: "))
    match user_choice:
        case 0:
            print("exiting program")
            break
        case 1:
            new_user = User()
            new_user.create_user()
            print(new_user.users)
            continue