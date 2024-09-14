"""
happy birthday 

"""

from datetime import datetime
import jdatetime

# getting current date & time and birth date & time
now: datetime = datetime.now().date()
now_time = datetime.now().time()
date_input:str = input("please enter your birthday in this format (%Y-%M-%d): \n")
birthday:datetime = datetime.strptime(date_input , "%Y-%m-%d")
birthTime:str = input("please enter the time of day you were born in this format (HH:mm): \n")
birth_time:datetime = datetime.strptime(birthTime , "%H:%M")

diff:datetime = now - birthday.date()

print(f"the amout of days you have been alive is : {diff.days} days\n")

seconds_alive = diff.days * 24 * 60 * 60

print(f"the amount of seconds you have been alive is : {seconds_alive} seconds\n")


def calculate_remaining_days(birthday, now) -> int:
    this_years_birthday = datetime(now.year, birthday.month, birthday.day).date()
    next_years_birthday = datetime(now.year+1, birthday.month, birthday.day).date()
    
    if this_years_birthday > now:
        return (this_years_birthday - now).days-1
    else:
        return (next_years_birthday - now).days-1

def calculate_remainig_minutes(time, now) -> int:
    return ((24 * 60) - (now.hour *60 + now.minute)) + (time.hour *60 +time.minute)

    
remaining_days = calculate_remaining_days(birthday.date() , now)
remaining_minuts = calculate_remainig_minutes(birth_time , now_time)
print(f"remaingin days from your next birthday is: {remaining_days} days and {remaining_minuts} minutes, happy birthday form {remaining_days} days in the future \n")

jalali_year = jdatetime.date.fromgregorian(day=birthday.day , month=birthday.month, year=birthday.year)
print("your birthday in jalali calender is" , jalali_year)