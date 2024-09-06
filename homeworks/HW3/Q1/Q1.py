"""
read the zen file then write the updated version into a new txt file

"""



numbers_dict: dict = {"one":1 , "two" : 2 , "three":3 , "four":4 , "five":5 , "six": 6 , "seven":7 , "eight": 8 , "nine": 9 , "ten":10 , "eleven": 11 , "tewelve": 12 , "thirteen": 13 , "fourteen": 14 , "fifteen":15 , "sixteen":16 , "seventeen":17 , "eighteen":18 , "nineteen":19 , "tewenty":20}

# read and find the words, put them in a new variable , replace the words in the new variable without changing the values in the OG file
with open("Zen.txt" , 'r') as file:
    data :str = file.read()
    for word in data.split(' '):
        if word in numbers_dict:
            new_text = str(numbers_dict[word])
            data = data.replace(word, new_text)
           

print(data)
# create a new file in this directory and write the updated new variable 
with open("updated_file.txt" , 'w') as file:
    file.write(data)