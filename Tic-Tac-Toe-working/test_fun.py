from functions import check_vertical_win, check_horizontal_win

row1 = [' ','|',' ','|',' ']
row2 = ['-','-','-','-','-']
row3 = [' ','|',' ','|',' ']
row4 = ['-','-','-','-','-']
row5 = ['X','|','X','|','X']
game_dict = {'1':row1,'2':row2,'3':row3,'4':row4,'5':row5}

print(check_horizontal_win(game_dict))