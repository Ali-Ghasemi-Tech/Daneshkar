def sum(n, number):
    while n > 0:
        number += 1/n
        return sum(n-1 , number)
    return number

print(sum(100 , 0))