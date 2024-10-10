from Modules import isDigit
from Modules import input_getter
from bank_account import BankAccount
class Subscribe:
    def __init__(self , user , account) -> None:
        self.account = account
        self.user = user

    def plan(self):
        while True:
            print("*** subscription page ***")
            print("""plans and their benefits

                    1. Silver: for the next 3 purchases, 20% of the purchase amount will be returned to your wallet only with the price of 300T
                
                    2. Golden: for the next 30 days 50% of your purchase will be returned to your bank account and you will get a energy drink from us only with the price of 500T
                
                    3. leave page
                
                """)
            user_plan = input_getter.get_input("enter the plan you want to subscribe to: ")
            user_plan = isDigit.number_valid(user_plan)
            
            match user_plan:
                case 1: 
                    if self.user["subscription"] == "silver":
                        print("you already have this plan you can update to golden plan with only 300T")
                        continue
                    self.account.withdraw(300)
                    self.user["subscription"] = "silver"
                    print("your plan has been updated to silver")
                    return [self.user , self.account]
                case 2:
                    if self.user["subscription"] == "golden":
                        print("you already have this plan")
                        return
                    if self.user["subscription"] == "silver":
                        self.account.withdraw(300)
                    else:
                        self.account.withdraw(500)
                    self.user["subscription"] = "golden"
                    print("your plan has been updated to golden")
                    return [self.user , self.account]
                case 3:
                    return
                case _: 
                    return


