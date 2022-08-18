import random

#create board
tttboard = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]


#switch players
def switch_player(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    
    return current_player


def show_board(tttboard):
    for row in tttboard:
        for culm in row:
            print(f"{culm} ", end="")
        print()

  
#Check for vaild move
def move_check(move, current_player):
    if move == "1":
        if tttboard[0][0] == "-":
            tttboard[0][0] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "2":
        if tttboard[0][1] == "-":
            tttboard[0][1] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "3":
        if tttboard[0][2] == "-":
            tttboard[0][2] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "4":
        if tttboard[1][0] == "-":
            tttboard[1][0] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "5":
        if tttboard[1][1] == "-":
            tttboard[1][1] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "6":
        if tttboard[1][2] == "-":
            tttboard[1][2] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "7":
        if tttboard[2][0] == "-":
            tttboard[2][0] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "8":
        if tttboard[2][1] == "-":
            tttboard[2][1] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False
    elif move == "9":
        if tttboard[2][2] == "-":
            tttboard[2][2] = current_player
            #check for win
            show_board(tttboard)
            return True
        else:
            print(f"{move} has already been chosen, please try again.")
            return False

#select where to play
def player_move():
    current_player = "X"
    game_running = True
    show_board(tttboard)

    while game_running:
        m = input(f"Player {current_player} select where you want to play using 1 - 9 :") 
        if int(m) in range(1,10):
            if move_check(m,current_player):
                if game_running != win_check():
                    break
                game_running = cat_check(tttboard)
                current_player = switch_player(current_player)
        else:
            print("invalid input, must be value from 0-8\n")

#check for win
def win_check():
    if tttboard[0][0] == tttboard[0][1] == tttboard[0][2] != "-":
        print(f"The Winner is {tttboard[0][0]}!")
        return False
        #returning false to set game_running False and end the game
    elif tttboard[1][0] == tttboard[1][1] == tttboard[1][2] != "-":
        print(f"The Winner is {tttboard[1][0]}!")
        return False
    elif tttboard[2][0] == tttboard[2][1] == tttboard[2][2] != "-":
        print(f"The Winner is {tttboard[2][0]}!")
        return False  
    elif tttboard[0][0] == tttboard[1][0] == tttboard[2][0] != "-":
        print(f"The Winner is {tttboard[0][0]}!")
        return False
    elif tttboard[0][1] == tttboard[1][1] == tttboard[2][1] != "-":
        print(f"The Winner is {tttboard[0][1]}!")
        return False
    elif tttboard[0][2] == tttboard[1][2] == tttboard[2][2] != "-":
        print(f"The Winner is {tttboard[0][2]}!")
        return False
    elif tttboard[0][0] == tttboard[1][1] == tttboard[2][2] != "-":
        print(f"The Winner is {tttboard[0][0]}!")
        return False
    elif tttboard[0][2] == tttboard[1][1] == tttboard[2][0] != "-":
        print(f"The Winner is {tttboard[0][2]}!")
        return False
    else:
        return True


#working on getting this function to check for a cat game.
def cat_check(tttboard):
    
    for row in tttboard:
        for culm in row:
            if culm == "-":
                return True
    
    print(f"Draw! Try playing again")
    return False