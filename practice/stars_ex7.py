user_input = int((input("enter the number of rows: ")))
for i in range(user_input):
    print('*' * (user_input - i) + (2*i)* ' ' +(user_input - i) * "*")

for j in range( 1 , user_input +1):
    print('*' * (j) + (2*(user_input- j))* ' ' +(j) * "*")
    