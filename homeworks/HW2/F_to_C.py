"""
fahrenheit to celsius

"""

list_of_temps = [0 , 10 , 12 , 15 , 100]

def calculator(celsius : float) -> int :
    fahrenheit = (celsius *1.8) + 32
    return fahrenheit

fahrenheits = map(calculator , list_of_temps)

print(list(fahrenheits))