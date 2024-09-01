user_input = 8

for i in range(1 ,user_input +1):
    for j in range(1 ,user_input+1):
        if i == 1 or j ==1 or i ==user_input or j == user_input or i == j or i +j == user_input+1:
            print(end='*')
        else:
            print(end=" ")
    print()