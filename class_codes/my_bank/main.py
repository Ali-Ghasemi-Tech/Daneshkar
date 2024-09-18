from bank import Bank
from user import User

banks = {
    "meli": Bank("meli"), 
    "blue" : Bank("blue")
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
# blue.create_account("ali", 1253 , "ali_pass")
# blue.create_account("mmd", 2564 , "mmd_pass")
# blue.create_account("amir", 256 , "amir_pass")
# blue.create_account("kiyan", 9862 , "kiyan_pass")

