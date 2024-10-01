from functions import player_cursor, replacement_choice, position_choice, display_rows, check_winner

row1 = [' ','|',' ','|',' ']
row2 = ['-','-','-','-','-']
row3 = [' ','|',' ','|',' ']
row4 = ['-','-','-','-','-']
row5 = [' ','|',' ','|',' ']
game_continue = "Y"
cursor = player_cursor()
if cursor =='X':
    player_2_cursor = 'O'
else:
    player_2_cursor = 'X'
print(f"Player 2 cursor: {player_2_cursor}")
display_rows(row1,row2,row3,row4,row5)
while game_continue == "Y":
    print("Player 1 turn")
    position = position_choice()
    game_dict = {'1':row1,'2':row2,'3':row3,'4':row4,'5':row5}
    new_game_dict = (replacement_choice(position,cursor,game_dict,True))
    if check_winner(game_dict) == "Winner":
        print(f"Player 1 wins!")
        break
    print("Player 2 turn")
    position = position_choice()
    new_game_dict = (replacement_choice(position,player_2_cursor,game_dict, True))
    if check_winner(game_dict) == "Winner":
        print(f"Player 2 wins!")
        break