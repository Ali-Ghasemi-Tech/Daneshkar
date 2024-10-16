def convert(file):
    n = len(file)
    for i in file:
        print(i+ ": " + file[i]['name'])
        print(f"""  
        duration: {file[i]['duration']}
        screening time: {file[i]['time']}
        ticket price: {file[i]['price']}
        seats left: {file[i]['left_tickets']}
                """)
        if int(i) == n:
            print() 