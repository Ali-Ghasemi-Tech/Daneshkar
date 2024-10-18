from getpass import getpass
from modules import password
from modules.user import User
from manager import Manager
from subscribe import Subscribe
from cinema import Cinema
from modules.clear import clear
from update_user_db import update
from modules.isDigit import get_number
from modules.logger import logger
 


def run():
    prev_user_name = None
    updated_temp_user = None

    second_run = False
    run_login = False
    manager_active = False
    selected_bank_account =None

    user_obj = User("user")

    clear()
    print("welcome to user dashboard")
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
            user_choice = get_number("enter the number of the task you want to do: (=^ ◡ ^=)\n")          
            match user_choice:
                case 1:
                    logger.info(f"user {prev_user_name} has requested their list of bank accounts")
                    clear()
                    print(updated_temp_user["bank_accounts"])
                    continue
                case 2:
                    logger.info(f"user {prev_user_name} has attempted creating a new bank account")
                    clear()
                    print("creating new bank account")
                    manager.create_account()
                    updated_temp_user["bank_accounts"] = manager.bank_accounts
                    update(updated_temp_user,prev_user_name)
                    print("your new account has been created")
                    logger.info(f"user {prev_user_name} has created a new bank account")
                    continue
                
                case 3:
                    logger.info(f"user {prev_user_name} has attempted to add funds to their wallet")
                    clear()
                    print("*** adding funds to wallet ***")
                    updated_temp_user = manager.wallet_funds()
                    update(updated_temp_user,prev_user_name)
                    print("funds have been added to your wallet")
                    logger.info(f"user {prev_user_name} has added funds to their wallet")
                    continue
                
                case 4:
                    logger.info(f"user {prev_user_name} has attempted to upgrade their subscription")
                    clear()
                    selected_bank_account = manager.get_bank_account()     
                    sub = Subscribe(updated_temp_user , selected_bank_account)
                    upgrade = sub.plan()
                    updated_temp_user = upgrade[0]
                    selected_bank_account = upgrade[1]
                    update(updated_temp_user, prev_user_name)
                    logger.info(f"user {prev_user_name} has upgraded their subscription")
                    continue
                case 5:
                    clear()
                    manager_active = False
                    logger.info(f"user {prev_user_name} has left the bank managment page")
                    continue
        
        elif user_obj.logged_in:
            id = updated_temp_user["user_id"]

            if not run_login:
                print(f"""\n\nwelcome {updated_temp_user["user_name"]} ( ͡° ͜ʖ ͡°)""")
                run_login = True
            else:
                print(f"""so what do you want to do next {updated_temp_user["user_name"]} (╹ -╹)?""")

            print("""what do you want to do?
                1. show account info
                2. edit account info
                3. change password
                4. manage bank accounts
                5. check this week's movies
                6. logout
                """)
            user_choice = get_number("enter the number of the task you want to do: (=^ ◡ ^=)\n") 
            match user_choice:
                case 1:
                    logger.info(f"user {prev_user_name} has requested their account info")
                    clear()
                    print("***user info***")
                    print(user_obj.__str__(updated_temp_user)+"\n\n")
                    continue

                case 2:
                    logger.info(f"user {prev_user_name} has attempted changing their account name")
                    clear()
                    print("***changing account info***")
                    user_obj_name = user_obj.get_user_name()
                    updated_temp_user["user_name"] = user_obj_name
                    user_obj_phone = input("please enter your new phone number here: ")
                    updated_temp_user["user_phone"] = user_obj_phone
                    print("\nyour info has been changed\n")
                    user_obj.users[id] = updated_temp_user
                    update(updated_temp_user ,  prev_user_name)
                    prev_user_name = updated_temp_user["user_name"]
                    logger.info(f"user has updated their user_name: {prev_user_name}")
                    continue

                case 3:
                    logger.info(f"user {prev_user_name} has attempted changing their password")
                    clear()
                    print("***changing password***")
                    old_pass = getpass("please enter your old password: ")
                    hashed_old_pass =password.hash_password(old_pass)
                    if updated_temp_user["user_pass"] == hashed_old_pass:
                        new_pass = password.get_password()
                        repeat_new_pass = getpass("repeat new password: ")
                        if new_pass == repeat_new_pass:
                            hashed_new_pass = password.hash_password(new_pass)
                            updated_temp_user = user_obj.update_pass(hashed_new_pass , id)
                            print("\nyour password has been changed succesfully ( •◡-)-♡\n")
                            update(updated_temp_user , prev_user_name)
                            logger.info(f"user {prev_user_name} has changed their password")
                        else:
                            logger.info(f"user {prev_user_name} has entered the repeate password wron")
                            print("\nthe passwords don't match! (≖_≖ )\n")
                            continue
                    else:
                        logger.info(f"user {prev_user_name} has entered their password wrong")
                        print("\nthe password is not correct! (≖_≖ )\n")
                        continue
                case 4:
                    logger.info(f"user {prev_user_name} has requested to go to bank account manager page")
                    clear()
                    manager = Manager(updated_temp_user , updated_temp_user["bank_accounts"])
                    manager_active = True
                    continue

                case 5:
                    logger.info(f"user {prev_user_name} has requested to go to cinema page")
                    clear()
                    cinema_instance = Cinema(updated_temp_user)
                    cinema_instance.show_movies()
                    continue

                case 6:

                    clear()
                    print("you are logging out")
                    run_login = False
                    user_obj.logged_in = False
                    logger.info(f"user {prev_user_name} has logged out")
                    continue

                case _:
                    clear()
                    print("\ninvalid input\n")
                    continue
                
        else: 
            print("""you are not logged in what do you want to do? ( ╹ -╹)?
                
                0. exit program
                1. create account
                2. login
                
                """)
            user_choice = get_number("enter the number of the task you want to do: (=^ ◡ ^=)\n") 

            match user_choice:
                case 0:
                    clear()
                    print("exiting program")
                    print("Goodby , come again soon (>ᴗ•) !")
                    logger.info(f"user has exited the app")
                    break

                case 1:
                    logger.info("user has attempted creating an account")
                    clear()
                    updated_temp_user = user_obj.create_user()
                    prev_user_name = updated_temp_user["user_name"]
                    update(updated_temp_user,prev_user_name)
                    logger.info(f"user {prev_user_name} has created an account")
                    continue

                case 2:
                    logger.info("user has attempted login")
                    clear()
                    updated_temp_user = user_obj.login()
                    try:
                        prev_user_name = updated_temp_user["user_name"]
                    except TypeError:
                        logger.error(f"user could not login: {TypeError}")
                        continue
                    logger.info(f"user {prev_user_name} has logged in")
                    continue
                
                case _:
                    clear()
                    print("\ninvalid input\n")
                    continue