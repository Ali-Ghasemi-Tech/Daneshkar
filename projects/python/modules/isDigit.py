def get_initial_amount():
    try:
        return int(input("enter your starting amount: "))
    except ValueError:
        print("please enter a number!!!")
        return get_initial_amount()
    
def get_cvv2():
    try:
        return int(input("enter your cvv2: "))
    except ValueError:
        print("please enter a number!!!")
        return get_cvv2()
    
def number_valid(number):
    try:
        return int(number)
    except ValueError:
        print("please enter a number!!!\n\n")