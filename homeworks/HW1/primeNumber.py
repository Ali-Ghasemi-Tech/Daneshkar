start_number = int(input("enter your starting number: "))
finish_number = int(input("enter your finishing number: "))
prime_numbers = []

while start_number < finish_number:
    isPrime = True
   
    for i in range(2 , start_number):
        if start_number % i == 0 :
            isPrime = False
    
    if isPrime and start_number != 1:
        prime_numbers.append(start_number)
        
    start_number += 1

print(prime_numbers)
