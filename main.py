#--------------GLOBAL VARIABLE-------------
#Game printBoard

printBoard=["1","2","3",
            "4","5","6",
            "7","8","9"]

# if game is still going
game_still_going=True

# who win?or tie?
winner=None

#whose turn is it
current_player="X"

#display game
def display_board():

    for i in range (0,9) :
        if printBoard[i] != "-" :
            printBoard[i] = printBoard[i]

    print("      |     |    ")
    print("    "+printBoard[0]+" |  "+printBoard[1]+"  |  "+printBoard[2])
    print("      |     |    ")
    print(" -----+-----+-----")
    print("      |     |    ")
    print("    "+printBoard[3]+" |  "+printBoard[4]+"  |   "+printBoard[5])
    print("      |     |    ")
    print(" -----+-----+-----")
    print("      |     |    ")
    print("    "+printBoard[6]+" |  "+printBoard[7]+"  |   "+printBoard[8])
    print("      |     |    ")

#play a game tic tak toe
def play_game():

    #Display initial printBoard
    display_board()

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner=="X" or winner=="O":
        print(winner+"won.")
    elif winner==None:
        print("Tie.")


#handle a single turn of an arbitrary player
def handle_turn(player):

    print(player+"'s turn.")
    position =  input("choose a position from 1-9:")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid input.>1choose a position from 1-9:")

        position = int(position)-1
        if printBoard[position] != "X" or printBoard[position] != "O":
            valid=True
        else :
            print("you can't go there.go again")

    printBoard[position]=player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # set up global varibles
    global winner

    #check rows
    row_winner=check_rows()

    #check columns
    column_winner=check_columns()

    #check diagonals
    diagonal_winner=check_diagonals()
    if row_winner:
        #there was a win
        winner=row_winner
    elif column_winner:
        #there was a win
        winner=column_winner
    elif diagonal_winner:
        #there was a win
        winner=diagonal_winner
    else:
        #there was no win
        winner=None

    return

def check_rows():
    # set up global varibles

    global game_still_going

    #check if any of the rows have all the same value(and isn't empty)
    row_1=printBoard[0]==printBoard[1]==printBoard[2]
    row_2=printBoard[3]==printBoard[4]==printBoard[5]
    row_3=printBoard[6]==printBoard[7]==printBoard[8]

    #if any row does have a match,flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going=False
    #return the winner (X or O)
    if row_1:
        return printBoard[0]
    elif row_2:
        return printBoard[3]
    elif row_3:
        return printBoard[6]
    return

def check_columns():
    # set up global varibles

    global game_still_going

    # check if any of the rows have all the same value(and isn't empty)
    column_1 = printBoard[0] == printBoard[3] == printBoard[6] 
    column_2 = printBoard[1] == printBoard[4] == printBoard[7] 
    column_3 = printBoard[2] == printBoard[5] == printBoard[8] 

    # if any column does have a match,flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return printBoard[0]
    elif column_2:
        return printBoard[1]
    elif column_3:
        return printBoard[2]
    return

def check_diagonals():
    # set up global varibles

    global game_still_going
    # check if any of the rows have all the same value(and isn't empty)
    diagonal_1 = printBoard[0] == printBoard[4] == printBoard[8] 
    diagonal_2 = printBoard[6] == printBoard[4] == printBoard[2] 


    # if any diagonal does have a match,flag that there is a win
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return printBoard[0]
    elif diagonal_2:
        return printBoard[6]

    return

def check_if_tie():
    
   # temp = False
    global game_still_going
    for i in range (0,9): 
        if printBoard[i] != "X" or printBoard[i] != "O" :
            return

    game_still_going = False
    return
        
def flip_player():
    #global varible we need
    global current_player
    #if the current player was X, then chnge to O
    if current_player=="X":
        current_player="O"
    #if the current_player was O,then chnge to X
    elif current_player=="O":
        current_player="X"
    return

play_game()
