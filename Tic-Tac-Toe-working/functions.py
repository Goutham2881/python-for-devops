def display_rows(row1,row2,row3,row4,row5):
    print(f"{row1[0]} {row1[1]} {row1[2]} {row1[3]} {row1[4]}")
    print(f"{row2[0]} {row2[1]} {row2[2]} {row2[3]} {row2[4]}")
    print(f"{row3[0]} {row3[1]} {row3[2]} {row3[3]} {row3[4]}")
    print(f"{row4[0]} {row4[1]} {row4[2]} {row4[3]} {row4[4]}")
    print(f"{row5[0]} {row5[1]} {row5[2]} {row5[3]} {row5[4]}")

def player_cursor():
    player_choice={"X": " ",
                   "O": " ",
                   "choice": " "}
    choice = input("Player 1 enter your choice(X,O): ")
    while choice not in ('X','O'):
        choice = input("Invalid input.Enter your choice(X,O): ")
    if choice == "X":
        player_choice["X"]="Player1"
        player_choice["O"]="Player2"
        player_choice["choice"]=choice
    elif choice == "O":
        player_choice["X"]="Player2"
        player_choice["O"]="Player1"
        player_choice["choice"]=choice
    return player_choice["choice"]
def position_choice():
    choice = ''
    while choice not in [ '1', '2','3','4','5','6','7','8','9']:
        choice = input("Pick a position(1, 2, 3, 4, 5, 6, 7, 8, 9): ")
        if choice not in [ '1', '2','3','4','5','6','7','8','9']:
            print("Sorry invalid choice!")
    return int(choice)

def gameon_choice():
    choice = ''
    while choice not in ['Y','N']:
        choice = input("Pick choose Y or N")
        if choice == 'Y':
            return True
        else:
            return False

def replacement_choice(position,cursor,game_dict,print_flag):
    # We use pint flag so that it only prints the output 1 time in case of same position is selected
    if position == 1:
        if game_dict['1'][0] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['1'][0] = cursor
    elif position == 2:
        if game_dict['1'][2] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['1'][2] = cursor
        #print(kwargs['1'])
    elif position == 3:
        if game_dict['1'][4] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['1'][4] = cursor
    elif position == 4:
        if game_dict['3'][0] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['3'][0] = cursor
    elif position == 5:
        if game_dict['3'][2] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['3'][2] = cursor
    elif position == 6:
        if game_dict['3'][4] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['3'][4] = cursor
    elif position == 7:
        if game_dict['5'][0] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['5'][0] = cursor
    elif position == 8:
        if game_dict['5'][2] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['5'][2] = cursor
    elif position == 9:
        if game_dict['5'][4] in ['X','O']:
            print("Position already filled please choose another one")
            position = position_choice()
            replacement_choice(position,cursor,game_dict,False)
        else:
            game_dict['5'][4] = cursor
    if print_flag == True:
        return display_rows(game_dict['5'],game_dict['4'],game_dict['3'],game_dict['2'],game_dict['1'])

def check_diagonal_win(game_dict):
    if game_dict['1'][0] == game_dict['3'][2] == game_dict['5'][4]!=' 'or game_dict['5'][0] == game_dict['3'][2] == game_dict['1'][4]!=' ':
        return "True"
def check_vertical_win(game_dict):
    if game_dict['1'][0] == game_dict['3'][0] == game_dict['5'][0]!=' ' or game_dict['1'][2] == game_dict['3'][2] == game_dict['5'][2]!=' ' or game_dict['1'][4] == game_dict['3'][4] == game_dict['5'][4]!=' ':
        return "True"
def check_horizontal_win(game_dict):
    if game_dict['1'][0] == game_dict['1'][2] == game_dict['1'][4]!=' ' or game_dict['3'][0] == game_dict['3'][2] == game_dict['3'][4]!=' ' or game_dict['5'][0] == game_dict['5'][2] == game_dict['5'][4]!=' ':
        return "True"
def check_winner(game_dict):
  if check_diagonal_win(game_dict) == "True" or check_vertical_win(game_dict) == "True" or check_horizontal_win(game_dict) == "True":
      return "Winner"