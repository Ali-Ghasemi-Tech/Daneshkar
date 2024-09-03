ostad_input = input('please enter your desired number: ')
def add(number):
    if number % 2 == 0:
        return number
    return 0
    
sum = 0
for i in ostad_input:
    next_number = add(int(i))
    sum += next_number

print(sum)
