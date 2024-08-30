user_input = input("until which number you want to do the calculations? ")
total = 0
text = ''
for i in range(1 ,int(user_input)+1):
    if i % 2  == 0:
        
        text += ' - ' + str(i)
        total -= i
    else:
        if i == 1:
            text += str(i)
        else:
            text += ' + ' + str(i)
        total += i
print(text + " = " + str(total))

    