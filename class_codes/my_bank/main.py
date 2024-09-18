from bank import Bank
from user import User

banks = {
    "meli": Bank("meli", 22), 
    "blue" : Bank("blue" , 20)
    }

meli = banks.get("meli")
blue = banks.get("blue")

#meli bank
print(f"the load budget for this bank is: {meli.loan_budget}")
print()

meli.create_account("ali", 1253 , "ali_pass")
meli.create_account("mmd", 2564 , "mmd_pass")
meli.create_account("amir", 256 , "amir_pass")
meli.create_account("kiyan", 9862 , "kiyan_pass")
# meli.loan() 
# print(meli.balance())

#blue bank
# blue.loan_budget = 5_000_000
# print(f"the load budget for this bank is: {blue.loan_budget}")
# print()
blue.create_account("ali", 1253 , "ali_pass")
blue.create_account("mmd", 2564 , "mmd_pass")
blue.create_account("amir", 256 , "amir_pass")
blue.create_account("kiyan", 9862 , "kiyan_pass")

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
