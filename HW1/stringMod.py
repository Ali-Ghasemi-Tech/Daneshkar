user_input = input("enter your string here: ")
vowels = 'aeiouAEIOU'
output = []
for i in user_input:
    if i == ' ':
        i = ''
        output.append(i)
    elif i in vowels:
        i = '.'
        output.append(i)
    elif i.upper() == i:
        i = i.lower()
        output.append(i)
    elif i.lower() == i:
        i = i.upper()
        output.append(i)
print(''.join(output))