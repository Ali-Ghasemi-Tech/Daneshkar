"""
only one number 

"""
greater_than_ten = True
calculation_index = 1
wrong_input = False

user_input = input("enter your desired number: ")

def calculate_sum(arg : str) -> int:
    sumation : int = 0
    for i in arg:
        sumation += int(i)
    print(f"calculation {calculation_index}: {sumation}")
    return sumation

while greater_than_ten == True:
    #checking the user input
    if(user_input.isnumeric()):
        final_number = calculate_sum(user_input)
        calculation_index += 1

        user_input = str(final_number)
        if final_number < 10 :
            greater_than_ten = False
    else:
        wrong_input = True
        break


if wrong_input:
    print('please enter a number')
else:
    print(f"the final sum that is less than 10 is: {final_number}")