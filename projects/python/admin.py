import json
from modules import isDigit , getDate
class Admin:
    permission = 'admin'
    def add_movie():

        name = input("enter name of the movie: ")
        time = getDate.getdate("enter the time of screening example(1403/01/01 13:30):")
        duration = input("enter the duration of the movie example(3H 16M): ")
        price = isDigit.get_number("enter the price of each ticket: ")
        age = isDigit.get_number("enter the minmum age restriction for this movie: ")
        seats = isDigit.get_number("enter the seats avalible for this movie: ")
        with open("db/movies.json" , "r") as file:
            data = json.load(file)
        n = len(data)
        new_index = n+1
        data[f"{new_index}"] = {}
        data[f"{new_index}"]["name"] = name
        data[f"{new_index}"]["time"] = time
        data[f"{new_index}"]["duration"] = duration
        data[f"{new_index}"]["price"] = price
        data[f"{new_index}"]["age"] = age
        data[f"{new_index}"]["left_tickets"] = seats

        with open("db/movies.json" , "w") as file:
            json.dump(data , file , indent=4)





