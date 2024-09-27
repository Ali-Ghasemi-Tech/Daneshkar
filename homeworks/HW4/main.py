
from users import User
from getpass import getpass
user_account = None
new_user = User()

while True:
    
    if new_user.logged_in:
        id  = user_account["user_id"]
        print(f"""welcome {user_account["user_name"]}
                what do you want to do?
                1. show account info
                2. edit account info
                3. change password
                4. logout
                """)
        user_choice = int(input("enter the number of the task you want to do: "))
        match user_choice:
            case 1:
                print(new_user.__str__(user_account))
                continue
            case 2:
                print("***changing account info***")
                new_user_name = input("please enter your new user_name here: ")
                user_account["user_name"] = new_user_name
                new_user_phone = input("please enter your new phone number here: ")
                user_account["user_phone"] = new_user_phone
                print("your info has been changed")
                new_user.users[id] = user_account
                continue
            case 3:
                print("***changing password***")
                old_pass = getpass("please enter your old password: ")
                hashed_old_pass =new_user.hash_password(old_pass)
                if user_account["user_pass"] == hashed_old_pass:
                    new_pass = new_user.get_password()
                    repeat_new_pass = getpass("repeat new password: ")
                    if new_pass == repeat_new_pass:
                        hashed_new_pass = new_user.hash_password(new_pass)
                        user_account["user_pass"] = hashed_new_pass
                        print("your password has been changed succesfully")
                    else:
                        print("the passwords don't match!")
                        continue
                else:
                    print("the password is not correct!")
            case 4:
                new_user.logged_in = False
                continue
            case _:
                print("invalid input")
                continue
    else: 
        user_choice = int(input("please enter the number of task you want to execute: "))
        match user_choice:
            case 0:
                print("exiting program")
                break
            case 1:
                user_account = new_user.create_user()
                print(new_user.users)
                continue
            case 2:
                user_account = new_user.login()
                continue
            case _:
                print("invalid input")
                continue