import math

def wind_tempreture(speed , tempreture):
    if tempreture <= 10:
        formula = 33 -(((10* math.sqrt(speed)) -(10 * speed) + 10.5) *(33 - tempreture)) / 22
        return f"the tempreture of the wind is: {formula}"
    return "the tempreture should be less than 10"

speed = int(input('enter the speed of wind: '))
temp = int(input('enter the tempreture of the inviroment: '))

wind_temp = wind_tempreture(speed , temp)
print(wind_temp)