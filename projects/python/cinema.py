from modules import isDigit , string_json 
from modules.logger import logger
import json
import datetime
from time import sleep
import jdatetime
from update_user_db import update
from modules.clear import clear


name = None
class Cinema:

    with open('db/movies.json' , 'r') as file:
            data = json.load(file)

    def __init__(self , user_account):
        self.user_account= user_account
        name = self.user_account['user_name']

    def show_movies(self):

        while True:
            sleep(0.5)
            print("*** cinema page ***")
            print("what do you want to watch? ")
            {string_json.convert(Cinema.data)}

            print("6. leave page\n")
            
            user_choice  = isDigit.get_number("enter the number of the movie you want to get ticketa for: ")
           
            if user_choice == None:
                continue
            self.get_tickets(user_choice)
            return self.user_account
                

    def apply_discount(self):
        months_subscribed = jdatetime.datetime.now().date().month  - jdatetime.datetime.strptime(self.user_account['creation_date'] , "%Y-%m-%d").date().month
        print("you can get a discount based on how many months you have been subscribed\n")
        print(f"based on your sunscription date you can get {months_subscribed}% discount")
        apply_discount = input("do you want to apply discount? (Y/n)")
        if apply_discount.lower() == 'y':
            return months_subscribed / 100
        else:
            return None
        
    def get_number_of_tickets(self):
        number_of_tickets =isDigit.get_number("how many tickets do you want for this movie? ")
        print()
        return number_of_tickets
    
    def get_tickets(self , movie_number):
        selected_movie = Cinema.data[str(movie_number)]
       

        if self.check_time(movie_number):
            clear()
            print("this movie is already being screened or has finished screening , you can't get a ticket for it now \n")
            return
        sub_discount = self.check_subscription()
        if not self.check_age(movie_number):
            clear()
            print(f"you'r too young to watch this , sorry come back {selected_movie["age"] - self.user_account["age"]} years later")
            return
        number_of_tickets =self.get_number_of_tickets()
        if self.check_seats( number_of_tickets,movie_number):
            clear()
            logger.info(f"user {name} has requested more tickets than avalible")
            print("there are less seats avalible than you requested!\n")
            return
        if number_of_tickets > selected_movie["left_tickets"]:
            print(f"the seats avalibale for this movie is {selected_movie["left_tickets"]}")
        check_discount=  self.apply_discount()
        
        if self.check_birthday_discount():
            logger.info(f"it's {name}'s birthday")
            selected_movie["price"] /= 2 

        if check_discount:
            total_amount :float  = number_of_tickets * selected_movie['price'] * check_discount
        else:
            total_amount : float = number_of_tickets * selected_movie['price']
            check_discount = 0
        n = len(self.user_account["tickets"]) + 1

        total_amount :float = total_amount * (1 - (sub_discount/100))
        if self.user_account['wallet_balance'] - total_amount > 0:

            selected_movie['left_tickets'] -= number_of_tickets

            self.user_account["tickets"][n] = {"name": selected_movie['name'] , "screening_time": selected_movie['time'] , "duration" : selected_movie['duration'] , "number_of_tickets": number_of_tickets}
            clear()

            if self.user_account["subscription"]["sub"] == "golden":
                self.user_account["tickets"][n]["exteras"] = "one free energy drink"
                print("you can get your free energy drink when coming to watch the movie\n")


            self.user_account["wallet_balance"] -= total_amount
            update(self.user_account , name)

            print("\nyour purchase has been applied , enjoy the movie\n")
            print("you can get your free energy drink when coming to watch the movie\n")
            return True
        else:
            clear()
            print("you don't have enough funds in your wallet\n")
            return

    def check_subscription(self):
        user_sub = self.user_account['subscription']
        match user_sub['sub']:
            case 'bronze':
                return 0
            case 'silver':
                if user_sub['used'] <=3:
                    returning_percent = 20
                    user_sub['used'] += 1
                    return returning_percent
                else:
                     return 0
            case 'golden':
                if (jdatetime.datetime.now().date() - jdatetime.datetime.strptime(user_sub['date'] , "%Y-%m-%d").date() ).days <=30:  
                    returning_percent = 50
                    return returning_percent
                else:
                    return 0
                
    def check_age(self , movie_number):
        age = self.user_account['age']
        if Cinema.data[str(movie_number)]['age'] < age:
            return True
        else :
            return False
        
    def check_birthday_discount(self):
        month_of_birth = jdatetime.datetime.strptime( self.user_account["date_of_birth"] , "%Y-%m-%d").month
        day_of_birth = jdatetime.datetime.strptime( self.user_account["date_of_birth"] , "%Y-%m-%d").day

        now = datetime.datetime.now().date()

        if month_of_birth == jdatetime.date.fromgregorian(date = now).month and day_of_birth == jdatetime.date.fromgregorian(date = now).day:
            print (f"happy birthday {self.user_account["name"]} , since it's your birthday the tickets price are halfed.\n")
            return True 
        else:
            return False
        
    def check_time(self, movie_number):

        movie_time = jdatetime.datetime.strptime(Cinema.data[str(movie_number)]['time'] , "%Y/%m/%d %H:%M")
        now = jdatetime.datetime.now()
        if now > movie_time:
           
            return True
        else:
            return False
        
    def check_seats(self ,request_seat, movie_number):
        if request_seat > Cinema.data[str(movie_number)]['left_tickets']:
            return True
        return False
    

        
# cin = Cinema({
#                 "date_of_birth": datetime.datetime.strptime("2024/9/10" , "%Y/%m/%d").date(),
#                 "name": "ali",
#                 "age": 20,
#                 "creation_date" : datetime.datetime.now().date() ,
#                 "wallet_balance" : 1000,
#                 "subscription" : {"sub" : "silver" , "used" : 4 , "date" : datetime.datetime.strptime("2024/9/10" , "%Y/%m/%d").date()} ,
#                 "tickets": {},
#                 })
# cin.show_movies()

# print(cin.user_account)
