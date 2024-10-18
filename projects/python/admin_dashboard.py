from getpass import getpass
from modules import password
from modules.user import User
from modules.clear import clear
from update_user_db import update
from admin import Admin
from modules.isDigit import get_number
from modules.logger import logger


def run():
    prev_admin_name = None
    updated_temp_admin = None

    second_run = False
    run_login = False

    admin_obj = User("admin")

    clear()
    print("welcome to admin dashboard")
    while True:
        
        if not second_run:
            print("\n\nWelcome to this awsome admin mangament program  (≧ᗜ≦)\n\n")
            second_run = True
        
        
        if admin_obj.logged_in:
            id = updated_temp_admin["admin_id"]

            if not run_login:
                print(f"""\n\nwelcome {updated_temp_admin["admin_name"]} ( ͡° ͜ʖ ͡°)""")
                run_login = True
            else:
                print(f"""so what do you want to do next {updated_temp_admin["admin_name"]} (╹ -╹)?""")

            print("""what do you want to do?
                1. show account info
                2. edit account info
                3. change password
                4. add movies
                5. logout
                """)
            admin_choice = get_number("enter the number of the task you want to do: (=^ ◡ ^=)\n") 
            match admin_choice:
                case 1:
                    logger.info("admin got thier account info")
                    clear()
                    print("***admin info***")
                    print(admin_obj.__str__(updated_temp_admin)+"\n\n")
                    continue

                case 2:
                    clear()
                    print("***changing account info***")
                    admin_obj_name = admin_obj.get_admin_name()
                    updated_temp_admin["admin_name"] = admin_obj_name
                    admin_obj_phone = input("please enter your new phone number here: ")
                    updated_temp_admin["user_phone"] = admin_obj_phone
                    print("\nyour info has been changed\n")
                    admin_obj.users[id] = updated_temp_admin
                    update(updated_temp_admin ,  prev_admin_name)
                    prev_admin_name = updated_temp_admin["admin_name"]

                    logger.info(f"admin has changed thier name: {prev_admin_name}")
                    continue

                case 3:
                    clear()
                    print("***changing password***")
                    old_pass = getpass("please enter your old password: ")
                    hashed_old_pass =password.hash_password(old_pass)
                    if updated_temp_admin["admin_pass"] == hashed_old_pass:
                        new_pass = password.get_password()
                        repeat_new_pass = getpass("repeat new password: ")
                        if new_pass == repeat_new_pass:
                            hashed_new_pass = password.hash_password(new_pass)
                            updated_temp_admin = admin_obj.update_admin_pass(hashed_new_pass , id)
                            print("\nyour password has been changed succesfully ( •◡-)-♡\n")
                            update(updated_temp_admin , prev_admin_name)
                            logger.info("admin has changd thier password")
                        else:
                            print("\nthe passwords don't match! (≖_≖ )\n")
                            logger.error("admin repeted password did not match the new password")
                            continue
                    else:
                        print("\nthe password is not correct! (≖_≖ )\n")
                        logger.error("admin has entered a wrong password")
                        continue
            
                case 4:
                    clear()
                    logger.info(f"admin {prev_admin_name} has attempted adding a new movie")
                    admin_instance = Admin
                    admin_instance.add_movie()
                    clear()
                    print("the movie has been added to movie list")
                    logger.info(f"admin {prev_admin_name} has added a new movie")
                    continue

                case 5:
                    clear()
                    print("you are logging out")
                    logger.info(f"admin {prev_admin_name} has logged out")
                    run_login = False
                    admin_obj.logged_in = False
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
            admin_choice = get_number("please enter the number of task you want to execute: (=^ ◡ ^=)\n") 
            match admin_choice:
                case 0:
                    logger.info("admin has exited admin dashboard")
                    clear()
                    print("exiting program")
                    print("Goodby , come again soon (>ᴗ•) !")
                    break

                case 1:
                    
                    clear()
                    updated_temp_admin = admin_obj.create_admin()
                    prev_admin_name = updated_temp_admin["admin_name"]
                    update(updated_temp_admin,prev_admin_name)
                    logger.info("admin has created and account")
                    continue

                case 2:
                    clear()
                    updated_temp_admin = admin_obj.admin_login()
                    try:
                        prev_admin_name = updated_temp_admin["admin_name"]
                    except TypeError:
                        logger.error(f"admin could not login: {TypeError}")
                        continue
                    logger.info(f"admin{prev_admin_name} has logged into thier account")
                    continue
                
                case _:
                    clear()
                    print("\ninvalid input\n")
                    continue