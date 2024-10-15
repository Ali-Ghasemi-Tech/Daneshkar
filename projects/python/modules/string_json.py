def convert(file):
    n = len(file)
    for i in file:
        print(i+ ": " + file[i]['name'])
        print(f"""  
        duration: {file[i]['duration']}
        screening time: {file[i]['time']}
        ticket price: {file[i]['price']}
                """)
        if int(i) == n:
            print() 