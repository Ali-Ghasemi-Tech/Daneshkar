list = []
for i in range(5, 9):
    for j in range(5 , 9):
        if i != j:
            for k in range(5 , 9):
                if k != i and k!= j:
                    for h in range(5 ,9):
                        if h != i and h != k and h != j:
                            number = str(i) +str(j) + str (k) + str(h)
                            if number in list:
                                continue
                            list.append(number)
                            list.sort(reverse=True)
print (list)