from modules.clear import clear

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
    
def get_number(text):
    try:
        return int(input(text))
    except ValueError:
        clear()
        print("\n\n!!!!!please enter a number!!!!!! ( ｡ •̀ ᴖ •́ ｡)💢 *#!&\n\n")
        return get_number(text)