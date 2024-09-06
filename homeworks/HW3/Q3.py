"""
assertion error check

"""

def apply_discount(price: int , discount:float=0.0) -> int:
    final_price = int(price*(1-discount))

    assert 0<final_price<= price , "where is error"
    
    return final_price

print(apply_discount(10 , 0.5))

# as the terminal has indicated the problem was a syntaxWarning and it was for parentheses of the assert condition 