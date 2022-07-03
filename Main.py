# --------- Global Veriables ---------

#get grid
from logging.config import valid_ident


grid = ["_", "_", "_",
         "_", "_", "_", 
         "_", "_", "_"]

# if game is still being played
game_still_going = True

# win or tie?
winner = None

# whos turn
current_player = "X"

#display grid
def display_grid():
    print(grid[0] + " | " + grid[1] + " | " + grid[2])
    print(grid[3] + " | " + grid[4] + " | " + grid[5])
    print(grid[6] + " | " + grid[7] + " | " + grid[8])

# play game of tic tac toe
def play_game():

    # display game grid
    display_grid()

    # while game is still going
    while game_still_going:

        # handle single turn of a player
        handle_turn(current_player)

        # check if game over
        check_if_game_over()
        
        # switch players
        flip_player()

    # the game is over
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Draw.")

# handle a single turn of a player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose # from 1-9 for position: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose # from 1-9 for position: ")

        position = int(position) - 1 #to translate from grid list

        if grid[position] == "_":
            valid = True
        else:
            print("That spot is taken, pick again")

    grid[position] = player

    display_grid()



def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    global winner

    #check rows
    row_winner = check_rows()
    #check column
    column_winner = check_columns()
    #check diag
    diag_winner = check_diag()
    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diag_winner:
        # there was a win
        winner = diag_winner
    else:
        # there was no win
        winner = None
    return

def check_rows():

    # set up global var
    global game_still_going

    # check if any rows are winning rows and aren't empty
    row_1 = grid[0] == grid[1] == grid[2] != "_"
    row_2 = grid[3] == grid[4] == grid[5] != "_"
    row_3 = grid[6] == grid[7] == grid[8] != "_"

    # if any row has match, there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner player
    if row_1:
        return grid[0]
    elif row_2:
        return grid[3]
    elif row_3:
        return grid[6]

def check_columns():

    # set up global var
    global game_still_going

    # check if any cols are winning rows and aren't empty
    col_1 = grid[0] == grid[3] == grid[6] != "_"
    col_2 = grid[1] == grid[4] == grid[7] != "_"
    col_3 = grid[2] == grid[5] == grid[8] != "_"

    # if any col has match, there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False

    # return the winner player
    if col_1:
        return grid[0]
    elif col_2:
        return grid[1]
    elif col_3:
        return grid[2]
    return

def check_diag():

    # set up global var
    global game_still_going

    # check if any diag are winning rows and aren't empty
    diag_1 = grid[0] == grid[4] == grid[8] != "_"
    diag_2 = grid[6] == grid[4] == grid[2] != "_"

    # if any diag has match, there is a win
    if diag_1 or diag_2:
        game_still_going = False

    # return the winner player
    if diag_1:
        return grid[0]
    elif diag_2:
        return grid[6]
    return

def check_if_tie():
    global game_still_going
    if "_" not in grid:
        game_still_going = False
    return


def flip_player():
    #global variables
    global current_player

    # if current player was x make it o
    if current_player == "X":
        current_player = "O"
    
    #if current player is o make it x
    elif current_player == "O":
        current_player = "X"
    return


play_game()