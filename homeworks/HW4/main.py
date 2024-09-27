
from users import User
from getpass import getpass
import time


user_account = None
new_user = User()
second_run = False
run_login = False
while True:
    if not second_run:
        print("\n\nWelcome to this awsome user mangament program   (≧ᗜ≦)\n\n")
        second_run = True
    time.sleep(2)
    if new_user.logged_in:
        id  = user_account["user_id"]

        if not run_login:
            print(f"""\n\nwelcome {user_account["user_name"]} ( ͡° ͜ʖ ͡°)""")
            run_login = True
        else:
            print(f"""so what do you want to do next {user_account["user_name"]} (╹ -╹)?""")

        print("""what do you want to do?
            1. show account info
            2. edit account info
            3. change password
            4. logout
            """)
        user_choice = input("enter the number of the task you want to do: (=^ ◡ ^=)\n")
        if user_choice.isdigit():
            user_choice = int(user_choice)
        else:
            print("\n\n!!!!!please enter a number!!!!!! ( ｡ •̀ ᴖ •́ ｡)💢 *#!&\n\n")
            continue
        match user_choice:
            case 1:

                print(new_user.__str__(user_account)+"\n\n")
                continue

            case 2:
                
                print("***changing account info***")
                new_user_name = new_user.get_user_name()
                user_account["user_name"] = new_user_name
                new_user_phone = input("please enter your new phone number here: ")
                user_account["user_phone"] = new_user_phone
                print("\nyour info has been changed\n")
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
                        new_user.update_pass(hashed_new_pass , id)
                        print("\nyour password has been changed succesfully ( •◡-)-♡\n")
                    else:
                        print("\nthe passwords don't match! (≖_≖ )\n")
                        continue
                else:
                    print("\nthe password is not correct! (≖_≖ )\n")

            case 4:
                print("you are logging out")
                run_login = False
                new_user.logged_in = False
                continue

            case _:
                print("\ninvalid input\n")
                continue
            
    else: 
        print("""you are not logged in what do you want to do? ( ╹ -╹)?
              
              0. exit program
              1. create account
              2. login
              
              """)
        user_choice = input("please enter the number of task you want to execute: (=^ ◡ ^=)\n")

        if user_choice.isdigit():
            user_choice = int(user_choice)
        else:
            print("\n\n!!!!!please enter a number!!!!!! ( ｡ •̀ ᴖ •́ ｡)💢 *#!&\n\n")

            continue

        match user_choice:
            case 0:

                print("exiting program")
                print("Goodby , come again soon (>ᴗ•) !")
                break

            case 1:

                user_account = new_user.create_user()
                
                continue

            case 2:

                user_account = new_user.login()
                continue
            
            case _:

                print("\ninvalid input\n")
                continue