"""
assertion error check

"""

def apply_discount(price: int , discount:float=0.0) -> int:
    final_price = int(price*(1-discount))
    
    # this code will not be checked on optimized mode
    assert 0<final_price<= price , "the condition has not been met"

    # this code will be checked on optimized mode
    if not 0<final_price<= price:
        return "the condition has not been met"

    return final_price

print(apply_discount(10 , -0.5))

# when we put prantices infront of the assert it will see that as a tuple and when it has something inside it , it will always return true

# also when the command is running with -O it will not catch any assetion errors in the code , it does that beacause it will see the code as a well rounded code and optimized and ready to go. so no assertion should even be raised when you run your code in optimized mode. (!be careful with this) , if you want to check conditions in your optimized code use if else statements


# conclusion : using assertion is great for development and catching up to errors early and it is only used for that reason , you can't make any changes to the code with assertion
