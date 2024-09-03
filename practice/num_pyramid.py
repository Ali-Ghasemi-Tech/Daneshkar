user_input= int(input("enter your number: "))
for i in range(1 ,user_input+1):
    print(end='*')
    for j in range(1 ,i+1):
        print(end=str(j))
        print(end=' ')
    for j in range(i-1 , 0 ,-1):
        print(end=str(j))
        if j != 1:
            print(end=' ') 
    print(end='*')
    print()

for i in range(user_input-1 , 0 , -1):
    print(end='*')
    for j in range(1 ,i+1):
        print(end=str(j))
        print(end=' ')
    for j in range(i-1 , 0 ,-1):
        print(end=str(j)) 
        if j != 1:
            print(end=' ')
    print(end='*')
    print()