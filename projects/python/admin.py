import json
import argparse
from human import Human
class Admin(Human):
    permission = 'admin'
    def add_movie(name , time , duration , price , age ,seats):
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

    def admin_dashboard():
        
        parser = argparse.ArgumentParser(description="add new movie as admin")
        parser.add_argument(f"--{Admin.permission}" ,  help="welcome to admin dashboard print -h for help" , action="store_true")

        parser.add_argument("name" , type=str , help="name of the movie")
        parser.add_argument("time" , type=str , help="time of the screening. format e.g.: '2024/10/16 13:30'")
        parser.add_argument("duration" , type=str , help="duration of movie. format e.g. '3H 40M' ")
        parser.add_argument("price" , type=int , help="price of ticket as int")
        parser.add_argument("age" , type=int , help="age restriction of the movie as int")
        parser.add_argument("left_tickets" , type=int , help="the number of seats left for selling ticket as int")
        args = parser.parse_args()

        if args.admin:
            Admin.add_movie(args.name , args.time , args.duration , args.price , args.age , args.left_tickets)
        else:
            print('for adding a movie you should print --admin before the arguments ')


