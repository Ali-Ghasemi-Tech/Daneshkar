user_input= int(input("enter the size number: "))
for i in range(user_input//2 ,user_input, 2 ):
    for j in range(1 , user_input - i ,2):
         print(end= ' ')
    for j in range(1 ,i+1):
          print(end='*')
    for j in range(1 , user_input - i +1):
         print(end= ' ')
    for j in range(1 ,i+1):
          print(end='*')
    print()
for i in range(user_input ,0 , -1):
     for j in range(i , user_input):
          print(end=' ')
     for j in range(1 , i*2):
          print(end='*')
     print()
     