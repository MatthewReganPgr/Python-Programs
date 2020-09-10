#201278659 Regan_Matthew-CA04
#11/2017
#Four dice rolling game

from random import randint


dice1 = randint (1, 6)
dice2 = randint (1, 6)
dice3 = randint (1, 6)
dice4 = randint (1, 6)
diceRoll = [dice1, dice2, dice3, dice4]


def Dice():
    print("In this game you roll a die four times. \nThe winning rolls from best to worst are: \nFour the same (2,2,2,2), Three the same (5,3,5,5), Run of four(1,3,2,4) \nRun of three with pair(4,5,6,4), Run of three(7,8,9,1),\nTwo pair(3,4,4,3) and a Pair(5,9,9,2)\n\n")
    
    print ("First die roll:",dice1)
    print ("Second die roll:",dice2)    
    print ("Third die roll:",dice3)
    print ("Fourth die roll:",dice4)
    
    print (diceRoll)
    diceOutcome()


def diceOutcome():
#Four the same
    if dice1 == dice2 == dice3 == dice4:
        print("You rolled four the same")

#Three the same
    elif dice1 == dice2 == dice3 or dice1 == dice2 == dice4 or dice2 == dice3 == dice4 or dice1 == dice3 == dice4:
        print("You rolled three of the same")

#FourRun
    elif dice1+1 in diceRoll and dice1+2 in diceRoll and dice1+3 in diceRoll:
        print("You rolled a run of four")
    elif dice2+1 in diceRoll and dice2+2 in diceRoll and dice2+3 in diceRoll:
        print("You rolled a run of four")
    elif dice3+1 in diceRoll and dice3+2 in diceRoll and dice3+3 in diceRoll:
        print("You rolled a run of four")
    elif dice4+1 in diceRoll and dice4+2 in diceRoll and dice4+3 in diceRoll:
        print("You rolled a run of four")

#threeRunWithPair
    elif dice1 == dice2 or dice1 == dice3 or dice1 == dice4 or dice2 == dice3 or dice2 == dice4 or dice3 == dice4:
        if dice1+1 in diceRoll and dice1+2 in diceRoll:
            print("You rolled a run of three with a pair")
        elif dice2+1 in diceRoll and dice2+2 in diceRoll:
            print("You rolled a run of three with a pair")
        elif dice3+1 in diceRoll and dice3+2 in diceRoll:
            print("You rolled a run of three with a pair")
        elif dice4+1 in diceRoll and dice4+2 in diceRoll:
            print("You rolled a run of three with a pair")
        else:
            pair()

#threeRun
    elif dice1+1 in diceRoll and dice1+2 in diceRoll:
        print("You rolled a run of three")
    elif dice2+1 in diceRoll and dice2+2 in diceRoll:
        print("You rolled a run of three")
    elif dice3+1 in diceRoll and dice3+2 in diceRoll:
        print("You rolled a run of three")
    elif dice4+1 in diceRoll and dice4+2 in diceRoll:
        print("You rolled a run of three")

    else:
        print("You rolled nothing")
    MainMenu()


#pair and twoPair   
def pair():
    if dice1 == dice2 and dice3 == dice4:
        print("You rolled two pair")
    elif dice2 == dice3 and dice1 == dice4:
        print("You rolled two pair")
    elif dice1 == dice3 and dice2 == dice4:
        print("You rolled two pair") 

    elif dice1 == dice2 or dice1 == dice3 or dice1 == dice4 or dice2 == dice3 or dice2 == dice4 or dice3 == dice4:
        print("You rolled a pair")
    
  
def MainMenu():
    print("\nMain Menu: \nA. Numbers\nB. Strings\nC. Games\nX. Exit\n\n")

        #Handling of user input on the main menu
    userInput = input("Please enter an option (A, B, C or X ): ").upper() #assigns a name to users input and converts whatever they type to uppercase

    if userInput == "A":
        print("Please choose a different option")
        MainMenu()
                                #If user types A or B they are met with an error message
    elif userInput == "B":
        print("Please choose a different option")
        MainMenu()
                                                    
    elif userInput == "C":                          
        Dice()      #When C is selected the dice procedure is called upon

    elif userInput == "X":  #If users type "X" then the program will terminate
        quit()

    else:
        print("Please enter a valid main menu option (A,B,C or X)")
        MainMenu()
MainMenu()      #Main menu is loaded as soon as the program is run  


input()
