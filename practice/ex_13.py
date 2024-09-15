def add(number):
    if number % 2 == 0:
        return number
    return 1
    

if __name__ == "__main__":
    ostad_input = input('please enter your desired number: ')
    multi = 1
    for i in ostad_input:
        next_number = add(int(i))
        multi *= next_number

    print(multi)
