#A package for masking (echoing) user password when entering
import maskpass

user = input("please enter your username: ")
password = maskpass.askpass("please enter your password: ")

if user == "admin" and password == "admin":
    print('Welcome')
elif user == "admin" and password != "admin":
    print('Wrong Data')
else:
    print(f"Hello {user}")
    