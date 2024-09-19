from bank import Bank
from user import User
import re
banks = {
    "meli": Bank("meli", 22), 
    "blue" : Bank("blue" , 20)
    }

meli = banks.get("meli")
blue = banks.get("blue")
meli.create_account("ali" , 1000 , "ali_pass" , 420420)
with open("./DB/meli_DB.txt" , "r+") as file:
    for line in file:
        account_string = re.split(r'[()]', line)
        try:
          detail_string = re.split(',' , account_string[1])
        except IndexError:
            continue
        meli.create_account(detail_string[0].strip() , int(detail_string[1].strip()) ,detail_string[2].strip() , int(detail_string[3].strip()))
                        

print("*** welcome to the best bank manager of your life *** \n")

print("""please be a good user and input what is wanted from you\n our backend team was a bit in a rush to create this app and did't implement the neccesery tools to check your input ^U^ \n""")
print("""if you don't , we are going to take all your money and close your account UWU \n""")
user_input = input("which bank do you want to work with (meli or blue)? ")
if user_input == "meli":
    bank = meli
elif user_input == "blue":
    bank = blue
else:
    print("wrong input , i told you to put the write input man. ok im just gonna give you the blue bank to work with")
    user_input = "blue"
    bank = blue

user = User(bank)
while True:
    if user.logged_in:
        print(f"""
            welcom {user.current_account.name}
            what do you want to do?
            1. withdraw
            2. deposit
            3. see balance
            4. request loan
            5. logout

        """)
        try:
            command = int(input("enter the task number that you want to do: "))
        except ValueError:
            print("please enter a number next time")
            continue
        match command:
            case 1:
                user.req_withdraw()
                continue
            case 2:
                user.req_deposit()
                continue
            case 3:
                user.req_balance()
                continue
            case 4:
                user.req_loan()
                continue
            case 5:
                user.logout()
                continue
            case _:
                print("your command was not found")
                continue
    else:
        print(f"""
            it seems you are not logged in
            what do you want to do?
            1. open account 
            2. login
            3. close app 
        """)
        try:
            command = int(input("enter the task number that you want to do: "))
        except ValueError:
            print("please enter a number next time")
            continue
        match command:
            case 1:
                bank.open_account()
                continue
            case 2:
                user.login()
                continue
            case 3: 
                print("closing app, Goodby")
                break
            case _:
                print("your command was not found")
                continue

with open("./DB/meli_DB.txt" , "w+") as file:
    data_dict = meli.accounts_id_dict
    for account in data_dict:
        file.write(str(data_dict.get(account)) + "\n")
    file.close()

with open("./DB/blue_DB.txt" , "w") as file:
    data_dict = blue.accounts_id_dict
    for account in data_dict:
        file.write(str(data_dict.get(account)) + "\n")
    file.close()
