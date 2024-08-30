num1= 1
num2 = 1
n = int(input("enter the steps: "))
print(num1)
print(num2)
while n >= 0:
    total = num1 + num2
    num2 = num1
    num1 = total 
    n -= 1 
    print(num1)