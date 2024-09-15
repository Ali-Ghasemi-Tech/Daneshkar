
def game(total_matches):
    total = total_matches
    while total > 0:
        player1_input = int(input("how many matches do you want to remove from the stack as player1: "))
        if player1_input >= 4:
            print('the maximum number of matches you can remove is 3')
            return
        if total - player1_input >0:
            total -= player1_input
            print(total)
        else: 
            total = 0
            print("player1 lost")
        
        player2_input = int(input("how many matches do you want to remove from the stack as player2:"))
        if player2_input >= 4:
            print('the maximum number of matches you can remove is 3')
            return
        if total - player2_input > 0:
            total -= player2_input 
            print(total)
        else:
            print("player2 lost")
            total =0

if __name__ == "__main__":
    total_matches = int(input("please enter the number of total matches: "))
    game(total_matches)