"""
napier number calculation

"""

def factorial(arg: int) ->int:
    num= 1
    for i in range(arg):
        num *= i+1
    return num

def napier_number(number_of_sentences: float , power_of_e: float) -> float:
    final_num = 1.0
    power_of_x= 1

    if number_of_sentences == 0 :
        return 0

    while number_of_sentences > 1 and power_of_e != 0:

        next_num= (power_of_e ** power_of_x) / factorial(power_of_x)
        
        final_num += next_num

        power_of_x += 1
        number_of_sentences -=1
    return final_num

#showing 3 numbers after decimal point
def decimal_numbers(arg) -> float:
    decimal_index = (str(arg)).index('.')
    napier_string = str(arg)
    result = napier_string[:decimal_index + 4]
    return float(result)

#app start
number_of_sentences = int(input("how many sentences do you want to calculate? "))
power_of_e = int(input("what number do you want the e to be powered by? "))

#calculating napier number based on user input
napier = napier_number(number_of_sentences, power_of_e)

#app finish
print(decimal_numbers(napier))

#keep in mind the more sentences you use , the more accurate it gets but it will be slower.