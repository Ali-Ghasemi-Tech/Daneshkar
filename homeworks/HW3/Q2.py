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

"""
EAFP will try to run a specific code and if it fails it will throgh an error(exception) which then we can catch it, this approach is good for when we don't know the error or the software we are writing this code for will change. 

LBYL triditional (if then else) statements and is good for when we know what can go wrong and what are conditions are.
"""