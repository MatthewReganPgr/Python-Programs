#Regan_Matthew-CA07
#12/2017
#A two player game with the aim to form a 2x2 shape using their associated tiles on a 5x5 grid

# Initialises variables and generates the playing board(matrix) for the game
row = 5
item = 5
rowNumber = 0
columnNumber = 0
matrix = [[0] * item for i in range(row)]


# Functions handles and validates the player 1's input 
def player1Move():
    global matrix
    
    print("Player 1's move") 
    rowNumber = int(input("Row: "))
    columnNumber = int(input("Column: "))
    if rowNumber < 1 or rowNumber > 5:
        print("Please enter a row value in the range 1 to 5\n")
        player1Move()

        
    elif columnNumber < 1 or columnNumber > 5:
        print("Please enter a column value in the range 1 to 5\n")
        player1Move()

    elif matrix[rowNumber-1][columnNumber-1] == 2:  # Checks the users input and if it matches that of player 2 then the move is illegal
        print("Player 2's token already occupies this position. Please choose a different one\n")
        player1Move()
        
    else:
        matrix[rowNumber-1][columnNumber-1] = 1     # Ammends the current state of the board and adds the player 1's token
        for row in matrix:
            for item in row:
                print(item, end=" ")
            print("")
        p1WinningState()

#Calculates whether the board is currently in a winning state for player 1
def p1WinningState():
    if 1 == matrix[0][0] == matrix[0][1] == matrix[1][0] == matrix[1][1]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[0][1] == matrix[0][2] == matrix[1][1] == matrix[1][2]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[0][2] == matrix[0][3] == matrix[1][2] == matrix[1][3]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[0][3] == matrix[0][4] == matrix[1][3] == matrix[1][4]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[1][0] == matrix[1][1] == matrix[2][0] == matrix[2][1]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[1][1] == matrix[1][2] == matrix[2][1] == matrix[2][2]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[1][2] == matrix[1][3] == matrix[2][2] == matrix[2][3]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[1][3] == matrix[1][4] == matrix[2][3] == matrix[2][4]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[2][0] == matrix[2][1] == matrix[3][0] == matrix[3][1]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[2][1] == matrix[2][2] == matrix[3][1] == matrix[3][2]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[2][2] == matrix[2][3] == matrix[3][2] == matrix[3][3]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[2][3] == matrix[2][4] == matrix[3][3] == matrix[3][4]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[3][0] == matrix[3][1] == matrix[4][0] == matrix[4][1]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[3][1] == matrix[3][2] == matrix[4][1] == matrix[4][2]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[3][2] == matrix[3][3] == matrix[4][2] == matrix[4][3]:
        print("Well played Player 1, you win!")
    elif 1 == matrix[3][3] == matrix[3][4] == matrix[4][3] == matrix[4][4]:
        print("Well played Player 1, you win!")

    # If no winning state is found after player 1's move then the game moves to the second player's turn
    else:
        player2Move()


# Functions handles and validates the player 2's input 
def player2Move():
    global matrix

    print("Player 2's move")
    rowNumber = int(input("Row: "))
    columnNumber = int(input("Column: "))
    if rowNumber < 1 or rowNumber > 5:
        print("Please enter a row value in the range 1 to 5\n")
        player2Move()

        
    elif columnNumber < 1 or columnNumber > 5:
        print("Please enter a column value in the range 1 to 5\n")
        player2Move()


    elif matrix[rowNumber-1][columnNumber-1] == 1:  # Checks the users input and if it matches that of player 1 then the move is illegal
        print("Player 1's token already occupies this position. Please choose a different one\n")
        player2Move()

        
    else:    
        matrix[rowNumber-1][columnNumber-1] = 2     # Ammends the current state of the board and adds the player 1's token
        for row in matrix:
            for item in row:
                print(item, end=" ")
            print("")
        p2WinningState()


#Calculates whether the board is currently in a winning state for player 1
def p2WinningState():
    if 2 == matrix[0][0] == matrix[0][1] == matrix[1][0] == matrix[1][1]:
        print("Well played Player 2, you win!")
    elif 2 == matrix[0][1] == matrix[0][2] == matrix[1][1] == matrix[1][2]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[0][2] == matrix[0][3] == matrix[1][2] == matrix[1][3]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[0][3] == matrix[0][4] == matrix[1][3] == matrix[1][4]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[1][0] == matrix[1][1] == matrix[2][0] == matrix[2][1]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[1][1] == matrix[1][2] == matrix[2][1] == matrix[2][2]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[1][2] == matrix[1][3] == matrix[2][2] == matrix[2][3]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[1][3] == matrix[1][4] == matrix[2][3] == matrix[2][4]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[2][0] == matrix[2][1] == matrix[3][0] == matrix[3][1]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[2][1] == matrix[2][2] == matrix[3][1] == matrix[3][2]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[2][2] == matrix[2][3] == matrix[3][2] == matrix[3][3]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[2][3] == matrix[2][4] == matrix[3][3] == matrix[3][4]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[3][0] == matrix[3][1] == matrix[4][0] == matrix[4][1]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[3][1] == matrix[3][2] == matrix[4][1] == matrix[4][2]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[3][2] == matrix[3][3] == matrix[4][2] == matrix[4][3]:
        print("Well played Player 1, you win!")
    elif 2 == matrix[3][3] == matrix[3][4] == matrix[4][3] == matrix[4][4]:
        print("Well played Player 1, you win!")
        
    #player 2 can never have the last turn in the game, player 1 goes first and has the last turn
    else:
        player1Move()


# Generates the empty 5x5 board
def initiliseGame():
    print("The aim of the game is to have 4 of your number in a block shape.\nTo place your number first type a row number (1 - 5) followed by a column number (1 - 5)")
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print("")
    player1Move()
        



def MainMenu():
    print("\nMain Menu: \nA. Numbers\nB. Strings\nC. Games\nX. Exit\n\n")

    #Handling of user input on the main menu
    userInput = input("Please enter an option (A, B, C or X ): ").upper()

    if userInput == "A":
        print("Please choose a different option")
        MainMenu()                    #If user types A or B they are met with an error message
    elif userInput == "B":
        print("Please choose a different option")
        MainMenu()   
                                                
    elif userInput == "C":
        initiliseGame()      #When C is selected the game board is initialised
 
    elif userInput == "X":  #If users type "X" then the program will terminate
        quit()

    else:
        print("Please enter a valid main menu option (A,B,C or X)")
        MainMenu()
MainMenu()      #Main menu is loaded as soon as the program is run

input()
