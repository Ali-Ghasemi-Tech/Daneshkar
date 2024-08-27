laptop_stat = []

lowest_price = float('inf')
best_quality = 0

invalid_input = False
finsih = False

while finsih == False:
    laptop_price = int(input("enter the price of the laptop: "))
    laptop_quality = int(input("enter the quality rate of the laptop: "))
    laptop_stat.append([laptop_price , laptop_quality])
    
    finish_list = input("do you want to continue?(Y/n): ")
    if finish_list.lower() != 'y' and finish_list.lower() != 'n':
        print('invalid input err')
        invalid_input = True
        break
    elif finish_list.lower() == 'y':
        continue
    elif finish_list.lower() == 'n':
        finsih = True
    

if invalid_input == False:
    for laptop in laptop_stat:
        if laptop[0] < lowest_price:
            lowest_price = laptop[0]
        if laptop[1] > best_quality:
            best_quality = laptop[1]    

    print(laptop_stat)

    if [lowest_price , best_quality] in laptop_stat:
        print("Founded")
    else:
        print("Not Founded")
