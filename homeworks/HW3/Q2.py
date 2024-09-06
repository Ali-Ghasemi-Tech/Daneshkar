"""
LBYL vs EAFP

"""
import math

def LBYL(numerator:int , denominator:int) ->int | float:
    if denominator == 0:
       return "inf"
    else:
        return numerator/denominator
    
def EAFP(numerator:int , denominator:int) -> int | str:
    try:
        return numerator/denominator
    except Exception as e:
        return f"{e}: inf"

print(f"the LBYL style value is: {LBYL(1,0)}")
print(f"the EAFP style value is: {EAFP(1,0)}")