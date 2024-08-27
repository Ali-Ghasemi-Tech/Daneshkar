list = ( 1 , 1 , 5 , 2 , 5 , 8 , 9)
new_list = []
dict = {}
for i in list:
    if not i in dict:
        dict[i] = 1
    else:
        dict[i] +=1
for j in dict:
    for _ in range(dict[j]): 
        new_list.append(j)
print(new_list)
print(dict)