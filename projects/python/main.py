
from user import User
from getpass import getpass
from modules import password
from manager import Manager
from modules import isDigit
from subscribe import Subscribe
from cinema import Cinema
import argparse
from admin import Admin

temp_user_account = None
user_obj = User()
second_run = False
run_login = False
manager_active = False
selected_bank_account =None



parser = argparse.ArgumentParser(description="add new movie as admin")
parser.add_argument(f"--{Admin.permission}" ,  help="welcome to admin dashboard print" , action="store_true")
parser.add_argument("name"  ,nargs=argparse.OPTIONAL, type=str , help="name of the movie")
parser.add_argument("time" ,nargs=argparse.OPTIONAL, type=str , help="time of the screening. format e.g.: '2024/10/16 13:30'")
parser.add_argument("duration" ,nargs=argparse.OPTIONAL, type=str , help="duration of movie. format e.g. '3H 40M' ")
parser.add_argument("price" ,nargs=argparse.OPTIONAL, type=int , help="price of ticket as int")
parser.add_argument("age" ,nargs=argparse.OPTIONAL, type=int , help="age restriction of the movie as int")
parser.add_argument("left_tickets" ,nargs=argparse.OPTIONAL, type=int , help="the number of seats left for selling ticket as int")
args = parser.parse_args()

if args.admin:
    print("welcome to admin dashboard , for learning the arguments required for adding movies to db enter -h")
    Admin.add_movie(args.name , args.time , args.duration , args.price , args.age , args.left_tickets)

else:
    print('for adding a movie you should print --admin before the arguments ')
    print("welcome to user dashboard\n")
    while True:
        if not second_run:
            print("\n\nWelcome to this awsome user mangament program   (≧ᗜ≦)\n\n")
            second_run = True
        
        if user_obj.logged_in and manager_active:
            print("*** bank account manager page ***")
            print("""what do you want to do?
                1. show bank accounts
                2. create a new bank account
                3. add funds to wallet
                4. upgrade your subscription plan
                5. leave page
                """)
            user_choice = input("enter the number of the task you want to do: (=^ ◡ ^=)\n")
            user_choice = isDigit.number_valid(user_choice)
            match user_choice:
                case 1:
                    print(temp_user_account["bank_accounts"])

                    continue
                case 2:
                    print("creating new bank account")
                    manager.create_account()
                    temp_user_account["bank_accounts"] = manager.bank_accounts
                    print("your new account has been created")
                    continue
                
                case 3:
                    print("*** adding funds to wallet ***")
                    manager.wallet_funds()
                    print("funds have been added to your wallet")
                    continue
                
                case 4:
                    selected_bank_account = manager.get_bank_account()     
                    sub = Subscribe(temp_user_account , selected_bank_account)
                    upgrade = sub.plan()
                    temp_user_account = upgrade[0]
                    selected_bank_account = upgrade[1]

                case 5:
                    manager_active = False
                    continue
        
        elif user_obj.logged_in:
            id  = temp_user_account["user_id"]

            if not run_login:
                print(f"""\n\nwelcome {temp_user_account["user_name"]} ( ͡° ͜ʖ ͡°)""")
                run_login = True
            else:
                print(f"""so what do you want to do next {temp_user_account["user_name"]} (╹ -╹)?""")

            print("""what do you want to do?
                1. show account info
                2. edit account info
                3. change password
                4. manage bank accounts
                5. check this week's movies
                6. logout
                """)
            user_choice = input("enter the number of the task you want to do: (=^ ◡ ^=)\n")
            if user_choice.isdigit():
                user_choice = int(user_choice)
            else:
                print("\n\n!!!!!please enter a number!!!!!! ( ｡ •̀ ᴖ •́ ｡)💢 *#!&\n\n")
                continue
            match user_choice:
                case 1:

                    print(user_obj.__str__(temp_user_account)+"\n\n")
                    continue

                case 2:
                    
                    print("***changing account info***")
                    user_obj_name = user_obj.get_user_name()
                    temp_user_account["user_name"] = user_obj_name
                    user_obj_phone = input("please enter your new phone number here: ")
                    temp_user_account["user_phone"] = user_obj_phone
                    print("\nyour info has been changed\n")
                    user_obj.users[id] = temp_user_account
                    continue

                case 3:

                    print("***changing password***")
                    old_pass = getpass("please enter your old password: ")
                    hashed_old_pass =user_obj.hash_password(old_pass)
                    if temp_user_account["user_pass"] == hashed_old_pass:
                        new_pass = user_obj.get_password()
                        repeat_new_pass = getpass("repeat new password: ")
                        if new_pass == repeat_new_pass:
                            hashed_new_pass = password.hash_password(new_pass)
                            user_obj.update_pass(hashed_new_pass , id)
                            print("\nyour password has been changed succesfully ( •◡-)-♡\n")
                        else:
                            print("\nthe passwords don't match! (≖_≖ )\n")
                            continue
                    else:
                        print("\nthe password is not correct! (≖_≖ )\n")
                case 4:
                    manager = Manager(temp_user_account , temp_user_account["bank_accounts"])
                    manager_active = True
                    continue

                case 5:
                    cinema_instance = Cinema(temp_user_account)
                    cinema_instance.show_movies()
                    continue

                case 6:
                    print("you are logging out")
                    run_login = False
                    user_obj.logged_in = False
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

                    temp_user_account = user_obj.create_user()
                    
                    continue

                case 2:

                    temp_user_account = user_obj.login()
                    continue
                
                case _:

                    print("\ninvalid input\n")
                    continue


   