""" 
zip_code verification

"""

finish : bool = False 
verified_zip_codes : list = []

#input checking funciton 
def is_zip_code(param: str) -> bool:
    if '-' in param and len(param) == 11:
        zip_code_numbers : list = param.split('-')

        #check if input is only numbers
        for i in param:
            if i != '-':
                if i in '123456789':
                    continue
                else:
                    return False

        if len(zip_code_numbers) != 2:
            return False
        else:
            for number in zip_code_numbers:
                if len(number) != 5 :
                    return False
                else:
                    return True
    else:
        return False

#running application
while finish == False:
    user_input : str = input("please enter the zip code you want to check: ")

    if is_zip_code(user_input) == True:
        verified_zip_codes.append(user_input)
    
    proceed : str = input("do you want to continue?(y/n) ")
    if proceed.lower() == "y":
        continue
    elif proceed.lower() == 'n':
        finish = True
    else:
        print("worng input for this question \n we assume you don't want to continue")
        finish = True

#finish app
if len(verified_zip_codes) == 0:
    print('there were no verified zip_codes')
else:
    print(f"verified zip_codes are: {verified_zip_codes}")

