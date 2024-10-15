from modules import isDigit , string_json
import json

class Cinema:


    def show_movies():
        with open('db/movies.json' , 'r') as file:
            data = json.load(file)

        print("what do you want to watch? ")
        print(f"these are our movies for tonight\n")
        {string_json.convert(data)}
        
        user_choice  = input("enter the number of the movie you want to get a ticket for")
        user_choice = isDigit.number_valid(user_choice)
        match user_choice:
            case 1: 
                #lets instead make a dict of all movies since they should have price and age restrictions
                pass

cin = Cinema
cin.show_movies()