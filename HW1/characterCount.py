def count(input):
    word_map = {}
    for i in input:
        if i in word_map:
            word_map[i] += 1
        else: 
            word_map[i] = 1
    print(word_map)


#user_input = input("enter your string: ")
#count(user_input)

count("www.google.com")