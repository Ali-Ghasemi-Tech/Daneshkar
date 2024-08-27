"""
the sum of all numbers should be less than 10

"""

greater_than_ten = True

user_input = input("enter your desired number: ")

def calculate_sum(arg : str) -> int:
    sumation : int = 0
    for i in arg:
        sumation += int(i)
    return sumation

while greater_than_ten == True:
    final_number = calculate_sum(user_input)

    user_input = str(final_number)
    if final_number < 10 :
        greater_than_ten = False

print(final_number)