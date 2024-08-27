user_input = input('Enter your positive number: ')

reversed = []
if user_input.isnumeric():
    for num in user_input:
        reversed.insert(0,num)
    print(f"your reversed number is: {int(''.join(reversed))}")
else:
    print('please enter a positive number')

